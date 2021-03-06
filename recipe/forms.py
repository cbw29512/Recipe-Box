from django import forms 
from recipe.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorAddForm(forms.ModelForm):
        class Meta:
            model = Author
            fields = [
                'name',
                'bio',
            ]
        username = forms.CharField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


"""
Author model:
    Name (CharField)
    Bio (TextField)

Recipe Model:
    Title (CharField)
    Author (link, ForeignKey)
    Description (TextField)
    Time Required (Charfield) (for example, "One hour")
    Instructions (TextField)
"""
