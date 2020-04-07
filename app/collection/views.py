from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
# from django.http import HttpResponseRedirect
from django.views import generic, View

from core.models import Collection, Figure


class CollectionListView(generic.ListView):
    # model = Collection  # nahradil jsem queryset = ...
    template_name = 'collection/collection_list.html'
    # context_object_name = 'collection_list'  # neni treba, nechci-li zmenit

    queryset = Collection.objects.all().order_by('name')

    # neni potreba, pokud nechci upravit:
    # def get_queryset(self):
    #     """Return all published collections"""
    #     return Collection.objects.all()


class CollectionDetailView(generic.DetailView):
    model = Collection
    template_name = 'collection/detail.html'

    # this adds also all figures to the context:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['figure_list'] = Figure.objects.all()  # nepouzito
        
        # this adds also figures not included in the collection
        pk = self.kwargs['pk']
        context['not_in_collection_figure_list'] = \
            Figure.objects.exclude(collection=pk).\
                order_by('name')
        
        return context


class GreetingView(View):
    greeting = "Hello, budy."

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningView(GreetingView):
    greeting = "Mornin', man."


# --
# def detail(request, collection_id):
#     try:
#         c = Collection.objects.get(pk=collection_id)
#     except Collection.DoesNotExist:
#         raise Http404("Collection does not exist.")
#     context = {
#         'figures': c.figures.order_by('name')
#     }
#     return render(request, 'collection/detail.html', context)

# def detail(request, collection_id):
#     c = get_object_or_404(Collection, pk=collection_id)
#     context = {
#         'figures': c.figures.order_by('name')
#     }
#     return render(request, 'collection/detail.html', context)
