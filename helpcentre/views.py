from django.shortcuts import render
from django.views.generic import (DetailView, FormView)
from .forms import CommentForm,ReplyForm, BookingForm
from django.urls import reverse_lazy
from .models import *

# Create your views here.

def helpcentre_home(request):
    bookings = Booking.objects.all()
    comments = Comment.objects.all()
    replies = Reply.objects.all()

    context = {
        'bookings': bookings,
        'comments': comments,
        'replies': replies,
    }
    return render(request, 'helpcentre/index.html', context)


class BookingDetailView(DetailView, FormView):
    context_object_name = 'bookings'
    model = Booking
    template_name = 'helpcentre/booking_detail.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(BookingDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    # add here form submit logic and what happens after 
         
