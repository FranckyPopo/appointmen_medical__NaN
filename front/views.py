from django.shortcuts import render
from django.views import View


class FrontIndex(View):
    template_name = "front/pages/index.html"

    def get(self, request):
        return render(request, self.template_name)
    
class FrontContact(View):
    template_name = "front/pages/contact.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    
