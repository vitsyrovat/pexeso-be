from django.views import generic

from core.models import Figure


class FigureDetail(generic.DetailView):
    model = Figure
    template_name = 'figure/detail.html'
