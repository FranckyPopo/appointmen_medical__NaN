from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages

from authentication import forms, models, backends

class AuthenticationRegister(View):
    template_name = "authentication/register.html"
    form_class = forms.AuthenticationFormRegister

    def get(self, request):
        context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        message = "Un email de confirmation vous a été envoyé"
        form = self.form_class(request.POST)
        context = {
            "form": form
        }

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCES, message)
            return redirect("authentication_login")
        return render(request, self.template_name, context=context)
    
class AuthenticationLogin(View):
    template_name = "authentication/login.html"
    form_class = forms.AuthenticationFormLogin

    def get(self, request):
        context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = backends.MyBackend.authenticate(
                self,
                email=request.POST.get("email", ""),
                password=request.POST.get("password", ""),
            ) 

            if user:
                #logint(request, user)
                return HttpResponse("connection réussite")
        return HttpResponse("connection echoué")
            
    
class AuthenticationVerificationAccount(View):
    def get(self, request, token): 
        user = get_object_or_404(
            models.AccountVerification, 
            token=token
        ).user
        user.is_verification_account = True
        user.save()
        
        return HttpResponse("Compte activé")
    
