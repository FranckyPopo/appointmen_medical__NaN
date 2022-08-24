from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from user.forms import FormService, UserFormAppoitmen
from user.models import Service
from authentication.models import Town
from authentication.forms import AuthenticationFormEditUser

class UserAddService(LoginRequiredMixin, View):         
    template_name = "user/pages/add_service.html"
    form_class = FormService
    
    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context=context)
        
    def post(self, request):
        user = request.user
        form_profile = AuthenticationFormEditUser(instance=user)
        form = self.form_class(request.POST)
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        context = {
            "form": form,
        }
        
        if not user.fields_valid():
            messages.add_message(
                request, 
                messages.ERROR, 
                f"""Vous devez remplir certaint champ dans
                les paramétres du profile avant d'ajouter un service."""
            )
            return render(request, self.template_name, context=context)
             
        if form.is_valid():
            if Service.objects.filter(name__icontains=name, user=user):
                return HttpResponse("Le service existe déjà")
            
            Service.objects.create(name=name, description=description, user=user)
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

class UserHealthCenters(View):
    template_name = "front/pages/health_centers.html"
    
    def get(self, request, slug_town):
        if slug_town == "all":
            qs = get_user_model().objects.filter(is_active=True)
        else:
            qs = get_list_or_404(get_user_model(), town__slug=slug_town)
                
        context = {
            "centres": qs,
            "towns": Town.objects.filter(active=True),            
        }
        return render(request, self.template_name, context=context)

class UserHealthCenterDetail(View):
    template_name = "user/pages/health_centers_details.html"
    form_class = UserFormAppoitmen
    
    def get(self, request, slug_user):
        center = get_object_or_404(get_user_model(), slug=slug_user)
        context = {
            "center": center,
            "services": center.service_user.all(),
            "form": self.form_class,
        }    
        
        return render(request, self.template_name, context=context)
    
    def post(self, request, slug_user):
        pk_service = request.POST.get("service", "")
        user = get_object_or_404(get_user_model(), slug=slug_user)
        service = get_object_or_404(Service, pk=pk_service, user=user)
        form = self.form_class(request.POST)
        
        context = {
            "center": user,
            "services": user.service_user.all(),
            "form": form,
        } 
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.service = service
            f.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                f"Vôtre rendez-vous a été pris avec success."
            )

        return render(request, self.template_name, context=context)


