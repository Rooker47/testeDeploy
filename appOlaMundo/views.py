from django.views.generic import TemplateView

class OlaMundo(TemplateView):
    template_name = 'appOlaMundo/index.html'
