from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, View


from .forms import CreateGlucoseRecordForm
from .models import GlucoseRecord



class LoginView(View):
    template_name = "login.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("glucose_records")

        return render(request, self.template_name)
    


    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("glucose_records")
        
        else:
            return render(request, self.template_name, {"error": _("Invalid email or password")})

class CreateGlucoseRecord(LoginRequiredMixin, CreateView):
    form_class = CreateGlucoseRecordForm
    template_name = "create_glucose_record.html"
    success_url = reverse_lazy("glucose_records")
    message = _("Glucose measure added succesfully!")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        messages.success(self.request, message=self.message)
        
        return response


class UpdateGlucoseRecord(CreateGlucoseRecord, UpdateView):
    template_name = "update_glucose_record.html"
    model = GlucoseRecord
    message = _("Glucose measure modified succesfully!")

class DeleteGlucoseRecord(LoginRequiredMixin, DeleteView):
    template_name = "delete_glucose_record.html"
    model = GlucoseRecord
    success_url = reverse_lazy("glucose_records")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, message=_("Glucose measure removed succesfully!"))
        
        return response

class ListGlucoseRecord(LoginRequiredMixin, ListView):
    template_name = "list_glucose_record.html"
    
    def get_queryset(self):
        return GlucoseRecord.objects.filter(user__pk=self.request.user.pk).order_by("date")
