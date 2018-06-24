from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'deft/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'ABL Electrical Engineering'
        context['description'] = ''
        return context
