from django import forms 

from .models import Review


# class ReviewForm(forms.Form):
#     user_name =forms.CharField(label="Your Name",max_length=50,error_messages={
#         "required":"Your name must not be empty",
#         "max_length":"Please enter a shorter name!"

#     })

#     review_text =forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200, required=False)   
#     rating = forms.IntegerField(label="Your Rating", min_value=1,max_value=5)   

#instead of writing the whole forms fields we can use the models class to create the form

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ='__all__'
        # exclude = ['owner_comment']

        labels ={
            "user_name" : "Your Name",
            "review_text" : "Your Feedback",
            "rating" : "Your rating"
        }
        error_messages = {
            "user_name" : {
              "required":"Your name must not be empty",
             "max_length":"Please enter a shorter name"
        }}