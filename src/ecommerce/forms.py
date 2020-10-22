from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class ContactForm(forms.Form):

  fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "your name"}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': "your email"}))
  content = forms.CharField(widget= forms.Textarea(attrs= {"class":"form-control", 'placeholder': "your content"}))


  def clean_email(self):
    email = self.cleaned_data.get('email')
    if 'gmail.com' not in email:
      raise forms.ValidationError("the email is not valid")



class LoginForm(forms.Form):

   UserName = forms.CharField()
   Password = forms.CharField(widget = forms.PasswordInput())



class RegisterForm(forms.Form):
   UserName = forms.CharField()
   email = forms.EmailField()
   Password = forms.CharField(widget = forms.PasswordInput())
   Password2 = forms.CharField(label = "confirm password", widget = forms.PasswordInput())
   Address = forms.CharField()
   Phone = forms.CharField()

   def clean_UserName(self):

     username = self.cleaned_data.get('UserName')
     qs = User.objects.filter(username=username)
     print('printing')
     print(qs.exists())
     if qs.exists():
        raise forms.ValidationError("user already exists")
     return username

   def clean_email(self):

     email = self.cleaned_data.get('email')
     qs = User.objects.filter(email=email)
     if qs.exists:
        raise forms.ValidationError("email already exists")
     return email

   def clean(self):
     data = self.cleaned_data
     password = self.cleaned_data.get('Password')
     password2 = self.cleaned_data.get('Password2')

     if password != password2:
       raise forms.ValidationError("two password muss match")
     return data

class UserInfoForm(forms.Form):
   UserName = forms.CharField()
   Address = forms.CharField()
   Phone = forms.CharField()
