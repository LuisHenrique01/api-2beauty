from django.views.generic import TemplateView


class Docs(TemplateView):
    template_name = 'index.html'
