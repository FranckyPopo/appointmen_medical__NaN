from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from user.forms import FormService
from user.models import Service

class UserAddService(LoginRequiredMixin, View):         
    template_name = "user/pages/add_service.html"
    form_class = FormService
    
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
            messages.add_message(
                request, 
                messages.SUCCESS, 
                f"Vous venez d'ajouter le service {name}"
            )
            return redirect("user_list_services")
        return render(request, self.template_name, context=context)
            
class UserListService(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            "services": Service.objects.filter(user=request.user, active=True).order_by("name"),
        }
        
        return render(request, "user/pages/list_services.html", context=context)
        
class UserDeleteService(LoginRequiredMixin, View): 
    def post(self, request, pk_service):
        service = get_object_or_404(Service, pk=pk_service, active=True, user=request.user)
        service.delete()
        return HttpResponse("")

class UserEditService(LoginRequiredMixin, View):
    template_name = "user/pages/edit_service.html"
    form_class = FormService
    model = Service

    def get(self, request, pk_service):
        service = get_object_or_404(self.model, pk=pk_service, user=request.user, active=True)
        context = {
            "form": self.form_class(instance=service),
            "pk_service": service.pk,
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, pk_service=None):
        service = get_object_or_404(self.model, pk=pk_service, user=request.user, active=True)
        form = self.form_class(request.POST, instance=service)
        context = {
            "form": form,
            "pk_service": service.pk,
        }
        
        if form.is_valid():
            service.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                f"Vous venez de modifier le service {service.name}"
            )
            return redirect("user_list_services")
        return render(request, self.template_name, context=context)

