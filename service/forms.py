from django import forms
from service import models



class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'txt'}),
            'phone':forms.TextInput(attrs={'class':'txt'}),
            'text':forms.TextInput(attrs={'class':'txtarea'}),
        }
        
class AddRequestOfLeaveForm(forms.ModelForm):
    class Meta:
        model=models.RequestOfLeave
        fields='__all__'
        widgets = {
            'phone':forms.TextInput(attrs={'class':'txt'}),
        }


