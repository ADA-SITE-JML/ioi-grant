from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from .forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import *


class AboutTemplateView(TemplateView):
    template_name = 'visualizations/views/about_template_view.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['about'] = AboutPage.objects.first()
        context['site'] = SiteSetting.objects.first()
        context['navbar'] = Navbar.objects.first()
        context['body'] = Body.objects.first()
        context['logo'] = Logos.objects.first()

        return context


class GraphsListView(ListView):
    model = Graphs
    context_object_name = 'graphs'
    template_name = 'visualizations/views/graphs_list_view.html'

    def get_queryset(self):
        return Graphs.objects.filter(category=SiteSetting.objects.first().category)

    def get_context_data(self, **kwargs):
        context = super(GraphsListView, self).get_context_data(**kwargs)

        context['site']  = SiteSetting.objects.first()
        context['navbar'] = Navbar.objects.first()
        context['body'] = Body.objects.first()
        context['logo'] = Logos.objects.first()

        return context


@csrf_exempt
def post_layout(request):

    if request.is_ajax() and request.method == "POST":
        for index in range(len(request.POST) // 3):
            Graphs.objects.filter(pk=request.POST[f'data[{index}][id]']).update(top=request.POST[f'data[{index}][top]'], left=request.POST[f'data[{index}][left]'])

    return JsonResponse({}, status=200)

