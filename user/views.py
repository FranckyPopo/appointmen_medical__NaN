from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from user.forms import FormAddService
from user.models import Service


class UserAddService(View):         
    template_name = "user/pages/add_service.html"
    form_class = FormAddService
    
    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context=context)
        
    def post(self, request):
        form = self.form_class(request.POST)
        user = request.user
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        context = {
            "form": form,
        }
        
        if form.is_valid():
            if Service.objects.filter(name__icontains=name, user=user):
                return HttpResponse("Le service existe déjà")
            
            Service.objects.create(name=name, price=price, description=description, user=user)
            return HttpResponse("Service Ajouté")
        return render(request, self.template_name, context=context)
            
            
            
            
            
            
            
            
            
            
