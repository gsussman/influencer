from django import forms

from models import Email, User, Profile

class PostForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email',)
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')