from django import forms



class FeedbackForm(forms.Form):

    name = forms.CharField(

        label= 'Name' ,
        widget= forms.TextInput(

            attrs= {

                'class' :'form-control' ,
                'placeholder' :'your name'
            }
        )
    )


    ratings = forms.IntegerField(

    label='Ratings',
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'your ratings'
            }
        )
    )


    feedback = forms.CharField(

    label='Feedback',
    widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'your ratings'
            }
        )
    )










