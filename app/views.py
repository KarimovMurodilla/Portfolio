from django.views.generic import ListView

from .models import *

# Create your views here.
class PortfolioView(ListView):
    model = About
    queryset = About.objects.filter(id=1).values("my_name", "excerpt", "description").first()
    template_name = 'app/about_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.all()
        context['career'] = Career.objects.all()
        context['education'] = Education.objects.all()
        context['prog_skills'] = ProgrammingSkills.objects.all()
        context['skills'] = Skills.objects.all()
        context['feedbacks'] = Feedbacks.objects.all()

        return context