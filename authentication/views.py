from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.core.mail import EmailMessage

from authentication import forms, models, backends

class AuthenticationRegister(View):
    template_name = "authentication/register.html"
    form_class = forms.AuthenticationFormRegister

    def get(self, request):
        context = {
            "form": self.form_class,
            "towns": models.Town.objects.filter(active=True),
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        message = "Un email de confirmation vous a été envoyé"
        form = self.form_class(request.POST)
        pk_town = request.POST.get("town")
        town = get_object_or_404(models.Town, pk=pk_town)
        
        if form.is_valid():
            f = form.save(commit=False)
            f.town = town
            f.save()
            messages.add_message(request, messages.SUCCESS, message)
            return redirect("authentication_login")
        return render(request, self.template_name, context={"form": form})
    
    def http_method_not_allowed(self, request):
        return redirect('front_index')
    
class AuthenticationLogin(View):
    template_name = "authentication/login.html"
    form_class = forms.AuthenticationFormLogin

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class,})
    
    def post(self, request):
        form = self.form_class(request.POST)
        message = "Les identifiants que vous avez entrer son incorrect."

        if form.is_valid():
            user = backends.MyBackend.authenticate(
                self,
                email=request.POST.get("email", ""),
                password=request.POST.get("password", ""),
            ) 

            if user:
                login(request, user)
                return redirect("user_list_services")
        messages.add_message(request, messages.ERROR, message)
        return redirect("authentication_login")
            
    def http_method_not_allowed(self, request):
        return redirect('front_index')
            
    
class AuthenticationVerificationAccount(View):
    def get(self, request, token): 
        message = "Vôtre compte a été activé avec success"
        user = get_object_or_404(
            models.AccountVerification, 
            token=token
        ).user
        user.is_verification_account = True
        user.save()
        messages.add_message(request, messages.SUCCESS, message)
        return redirect("authentication_login")
    
    def http_method_not_allowed(self, request):
        return redirect('front_index')
    
    
class AuthenticationEditProfile(LoginRequiredMixin, View):
    template_name = "user/pages/edit_user_profile.html"
    form_class = forms.AuthenticationFormEditUser

    def get(self, request):
        context = {
            "countries": models.Country.objects.filter(active=True),
            "cities": models.City.objects.filter(active=True),
            "Towns": models.Town.objects.filter(active=True),
            "form": self.form_class(instance=request.user),
        }
        
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                f"Les modifications on été appliqué avec success."
            )
            return redirect("authentication_edit_profile")
        
        messages.add_message(
            request, 
            messages.ERROR, 
            f"""Impossibilité d'appliquer les changements. Veuillez vérifier les valeurs entrées"""
        )
        return render(request, self.template_name, context={"form": form})
        
    def http_method_not_allowed(self, request):
        return redirect('front_index')

class AuthenticationPasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('authentication_change_passwor_done')

class AuthenticationPasswordResetDone(LoginRequiredMixin, PasswordResetDoneView):
    template_name = 'authentication/password_change_done.html'     
        
    def get(self, request):
        body = f"""
        Vous venez de modifier vôtre mot de passe. Si vous n'ête pas 
        a l'origine de cette modification veuillez contact l'administrateur
        du site en cliquand sur le lien http://127.0.0.1:8000/{reverse_lazy("front_contact")} pour 
        récupérer vôtre compte. Sinon ignorer Se message.
        """
        # Envoie email    
        email = EmailMessage('Modification du mot de passe', body, to=[request.user.email])
        email.send()
        
        return render(request, self.template_name)
    
    def http_method_not_allowed(self, request):
        return redirect('front_index')

class AuthenticationLogout(LoginRequiredMixin, View):  
    def get(self, request):
        logout(request)
        return redirect("authentication_login")
    
    def http_method_not_allowed(self, request):
        return redirect('front_index')
    
        
        
        
        