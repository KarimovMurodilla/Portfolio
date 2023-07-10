from django.views.generic import ListView, CreateView

from .models import *
from .forms import TestimonialForm

# Create your views here.
class PortfolioView(ListView):
    model = About
    queryset = About.objects.filter(id=1).values("my_name", "excerpt", "description").first()
    template_name = 'app/about_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.filter(id=1).all().first()
        context['career'] = Career.objects.all()
        context['education'] = Education.objects.all()
        context['prog_skills'] = ProgrammingSkills.objects.all()
        context['skills'] = Skills.objects.filter(id=1).values("description").first()['description']
        context['works'] = Works.objects.all()
        context['testimonial'] = Testimonial.objects.all()

        return context


class TestimonialView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'app/testimonial.html'
    success_url = '/thank-you/'