from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

import json

from user.forms import FormService, UserFormAppoitmen, UserContactForm
from user.models import Service, Appointmen
from user.utils import format_date_appointment
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
        form = self.form_class(request.POST, request.FILES)
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        
        if not user.fields_valid():
            messages.add_message(
                request, 
                messages.ERROR, 
                f"""Vous devez remplir certaint champ dans
                les paramétres du profile avant d'ajouter un service."""
            )
            return render(request, self.template_name, context={"form": form})
             
        if form.is_valid():
            if Service.objects.filter(name__icontains=name, user=user):
                messages.add_message(
                    request, 
                    messages.ERROR, 
                    f"Le service n'a été crée cas il existe déjà."
                )
                return render(request, self.template_name, context={"form": form})
            
            f = form.save(commit=False)
            f.user = user
            f.save()
            messages.add_message(
            
                request, 
                messages.SUCCESS, 
                f"Vous venez d'ajouter le service {name}"
            )
            return redirect("user_list_services")
        return render(request, self.template_name, context={"form": form})
            
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
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "service_delete": None
                })
            }
        )
        
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
        form = self.form_class(request.POST, request.FILES, instance=service)
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
            qs = get_user_model().objects.filter(is_active=True, is_verification_account=True)
        else:
            qs = get_list_or_404(get_user_model(), town__slug=slug_town, is_active=True, is_verification_account=True)
        
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
        date_appointment = request.POST.get("date_appointmen", "")
        _format_date_appointment = None
        user = get_object_or_404(get_user_model(), slug=slug_user)
        service = get_object_or_404(Service, pk=pk_service, user=user)
        form = self.form_class(request.POST)
        
        context = {
            "center": user,
            "services": user.service_user.all(),
            "form": form,
        } 
        if form.is_valid():
            context = {
                "center": user,
                "services": user.service_user.all(),
                "form": self.form_class,
            } 
            f = form.save(commit=False)
            f.user = user
            f.service = service
            f.date_appointmen = format_date_appointment(date_appointment)
            f.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                f"Vôtre rendez-vous a été pris avec success."
            )
            return render(request, self.template_name, context=context)

        return render(request, self.template_name, context=context)

class UserAppoitment(LoginRequiredMixin, View):
    template_name = "user/pages/appoitment.html"

    def get(self, request):
        context = {
            "appointmens": request.user.appointmen_user.all(),
        }
        return render(request, self.template_name, context=context)
       
class UserAppoitmentDetail(LoginRequiredMixin, View):
    template_name = "user/pages/appoitment_content.html"

    def get(self, request, pk_appointmen):
        appointmen = get_object_or_404(Appointmen, pk=pk_appointmen, user=request.user)
        content_appointmen = render_to_string(self.template_name, {"appointmen": appointmen})
        
        return HttpResponse(content_appointmen)

class UserAppoitmentDelete(LoginRequiredMixin, View):
    def post(self, request, pk_appointment: int) -> HttpResponse:
        user = request.user
        appointments = user.appointmen_user.all()
        appointment = get_object_or_404(
            appointments,
            pk=pk_appointment
        )
        appointment.delete()
        number_appointment = len(user.appointmen_user.all())
        return HttpResponse(
            "",
            headers={
                "HX-Trigger": json.dumps({
                    "appoitment_delete": {"number_appointment": number_appointment},
                })
            }
        )
    
class UserContact(View):
    class_form = UserContactForm
    template_name = "front/pages/contact.html"

    def post(self, request):
        form = self.class_form(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                """La demande de contact contact
                été envoyé avec success"""
            )
            return redirect("front_contact")

        return render(
            request, 
            self.template_name, 
            context={"form": form}
        )

    def http_method_not_allowed(self, request):
        return redirect('front_index')

    