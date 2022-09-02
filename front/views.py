from django.shortcuts import render, redirect
from django.views import View

from user.forms import UserContactForm


class FrontIndex(View):
    template_name = "front/pages/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def http_method_not_allowed(self, request):
        return redirect('front_index')
    
class FrontContact(View):
    class_form = UserContactForm
    template_name = "front/pages/contact.html"
    
    def get(self, request):
        return render(
            request,
            self.template_name,
            context={"form": self.class_form},
        )

    def http_method_not_allowed(self, request):
        return redirect('front_index')
    
    
