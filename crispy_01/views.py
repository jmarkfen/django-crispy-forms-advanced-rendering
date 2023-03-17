from django.views.generic import TemplateView, FormView
from . import forms

class TestView(TemplateView):
    template_name = "form.html"

class TestForm(FormView):
    template_name = 'form.html'
    form_class = forms.AddressForm
    success_url = '/'
    