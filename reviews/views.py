from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review 
from django.views import View
# Create your views here.


class ReviewView(View):

    def get(self,request):
        form = ReviewForm()

        return render(request,"reviews/review.html",{
            "form": form
            })

    def post(self,request):
        
        form =ReviewForm(request.POST)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect("/thank-you")

        return render(request,"reviews/review.html",{
            "form": form
            })


# def reviews(request):
#     if request.method =="POST":
#         form =ReviewForm(request.POST)

#         if form.is_valid():
#             #cleandata in built function in forms 

#             # review = Review(
#             #                 user_name= form.cleaned_data['user_name'],
#             #                 review_text = form.cleaned_data['review_text'],
#             #                 rating= form.cleaned_data['rating'])
#             # review.save()

#             form.save()            
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you")
#     else:
#         #we passing the validated form with  message
#         form = ReviewForm()

#     return render(request,"reviews/review.html",{
#         "form": form
#     })

def thank_you(request):
    return render(request,"reviews/thank_you.html")