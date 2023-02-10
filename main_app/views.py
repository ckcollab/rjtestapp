
# Create your views here.

from django.shortcuts import render
#from django.http.response import HttpResponse
from django.views.generic import TemplateView,FormView,CreateView, DetailView, ListView
#from main_app.forms import ContactForm
from .models import Book




class home_view(TemplateView):
    template_name = 'main_app/home.html'

#class aboutme_view(TemplateView):
#    template_name = 'main_app/aboutme.html'
    


class readings_view(ListView):
    model = Book
    template_name = 'main_app/readings.html'
    paginate_by = 25

    

class bookdetail_view(DetailView):
    model = Book
    template_name = 'main_app/book_details.html'



#class travel_view(ListView):
#    model = Post
#    template_name = 'main_app/travel.html'

#class traveldetail_view(DetailView):
#    model = Post
#    template_name = "main_app/travel_details.html"




#class projects_view(TemplateView):
#    template_name = 'main_app/projects.html'


#class thankyou_view(TemplateView):
#    template_name = 'main_app/thank_you.html'

#class ContactFormView(FormView):
#    form_class = ContactForm
#    template_name = 'main_app/contact.html'

        # URL NOT a Template.html
#    success_url = "/main_app/thank_you/"
#    
#    def form_valid(self,form):
#        print(form.cleaned_data)
#        return super().form_valid(form)

