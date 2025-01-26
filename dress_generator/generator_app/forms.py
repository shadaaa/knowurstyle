from django import forms

class DressGenerationForm(forms.Form):
    prompt = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe your dress design...'}),
        label="Dress Design Prompt"
    )
