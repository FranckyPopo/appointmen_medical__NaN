from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse

from authentication.forms import AuthenticationFormRegister
from authentication.models import AccountVerification

class AuthenticationRegister(View):
    template_name = "user/register.html"
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
    
    
class AuthenticationVerificationAccount(View):
    def get(self, request, token): 
        user = get_object_or_404(
            AccountVerification, 
            token=token
        ).user
        user.is_verification_account = True
        user.save()
        
        return HttpResponse("Compte activé")
    
    
    
    
    
    
