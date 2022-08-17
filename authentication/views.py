from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

from authentication.forms import AuthenticationFormRegister, AuthenticationFormLogin
from authentication.models import AccountVerification

class AuthenticationRegister(View):
    template_name = "authentication/register.html"
    form_class = AuthenticationFormRegister

    def get(self, request):
        context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Compte créé")
        return HttpResponse("Impossible de créé le Compte")
    
class AuthenticationLogin(View):
    template_name = "authentication/login.html"
    form_class = AuthenticationFormLogin

    def get(self, request):
        context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            print(authenticate)
            user = authenticate(
                request,
                email=request.POST.get("email", ""),
                password=request.POST.get("password", ""),
            ) 
            print(user)

            if user:
                #logint(request, user)
                return HttpResponse("connection réussite")
        return HttpResponse("connection echoué")
            
    
class AuthenticationVerificationAccount(View):
    def get(self, request, token): 
        user = get_object_or_404(
            AccountVerification, 
            token=token
        ).user
        user.is_verification_account = True
        user.save()
        
        return HttpResponse("Compte activé")
    
