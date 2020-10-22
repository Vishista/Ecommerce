from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm, UserInfoForm
from django.contrib.auth import login, authenticate, get_user_model
from userdetails.models import UserInfo


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
       'title': "this is contact",
       'content': "welcome contact dep",
       'form' : contact_form
       
    }
    if contact_form.is_valid():
       print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #   print(request.POST)
    #   print(request.POST.get('fullname'))
    #   print(request.POST.get('email'))
    #   print(request.POST.get('content'))
        #return HttpResponse(request.POST.get('fullname'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    print(request.user.is_authenticated())
    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("UserName")
        password = form.cleaned_data.get("Password")
        user = authenticate(request, username = username, password = password)
        print(request.user.is_authenticated())
        if user is not None:
             login(request,user)
             print(request.user.is_authenticated())
             #context['form'] = LoginForm()
             return redirect("/login")
        else:
            print("error") 
    return render(request, 'auth/login.html',context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
     
    context = {
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("UserName")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("Password")
        address = form.cleaned_data.get("Address")
        phone = form.cleaned_data.get("Phone")
        
        NewUser = User.objects.create_user(username,email,password)
        InfoUser = UserInfo.objects.create_userinfo(username,email,address,phone)
        
       # print(NewUser)
    return render(request, 'auth/register.html',context)

def user_info(request):
        print(request.POST)
        userinfo= UserInfo()
        userinfo.username = request.POST.get('UserName')
        userinfo.email = request.POST.get('email')
        userinfo.address = request.POST.get('Address')
        userinfo.phone = request.POST.get('Phone')
       # InfoUser = UserInfo.objects.create(userinfo)
        userinfo.save()

def about_page(request):
    context = {
       'title': "this is about",
       'content': "welcome about dep"
    }
    return render(request, 'home.html', context)

def home_page(request):
    print(request.session.get('username', "unknown"))
    context = { 
       'content' : "home sweet home",
       'new_content' : "logged in"
       }
    #if request.user.is_authenticated():
        #context['new_content'] = "loggeg in"
     # context = { 
     #   'content' : "home sweet home",
     #   'new_content' : "not so sweet"
     #   }
    return render(request, 'home.html', context)


def home_page_old(request):
    html_ = """
    
    """
    return HttpResponse(html_)
