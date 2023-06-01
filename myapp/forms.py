from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':'','candidate1': '','candidate2': '','candidate3': '','candidate4': '','candidate5': '','candidate6': '','backgroundimg':'','footerimg':'','footerbg':''}
        
        
from django import forms

class VoteForm(forms.Form):
    candidate = forms.ChoiceField(choices=(
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
        ('option5', 'Option 5'),
        ('option6', 'Option 6'),
    ), widget=forms.RadioSelect)