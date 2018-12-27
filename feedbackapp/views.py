from django.shortcuts import render , redirect
from .models import FeedbackData
from .forms import FeedbackForm


def home(request):
    if request.method ==  'POST' :
        form  = FeedbackForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('ratings')
            feedback = request.POST.get('feedback')

            data = FeedbackData(

                name= name.title() ,

                rating= rating ,

                feedback= feedback
            )

            data.save()
            return redirect('/feedback/')

    else:
        fbs = FeedbackData.objects.all()
        form = FeedbackForm()
        return  render(request , 'feedback.html' , { 'form' :form  , 'fbs' : fbs })












