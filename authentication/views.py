from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from authentication.forms import AuthenticationFormRegister

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