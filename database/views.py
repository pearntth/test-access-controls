from django.shortcuts import render, redirect
from database.models import Contact, ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    data = { 'contacts' : contacts }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'index.html', data)
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST,  user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(user=request.user)

    data = {'form': form}
    return render(request, 'create_contact.html', data)

@login_required
def view_contact(request, id):
    contact = Contact.objects.get(id=id)
    data = {'contact': contact}
    return render(request, 'view_contact.html', data)

@login_required
def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    if contact.added_by != request.user:
        raise PermissionDenied
    else:
        if request.method == "POST":
            form = ContactForm(instance=contact, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ContactForm(instance=contact)

    data = {'form': form}
    return render(request, 'update_contact.html', data)

@login_required
def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    if contact.added_by != request.user:
        raise PermissionDenied
    else:
        contact.delete()
        return redirect('index')

@login_required
def members(request):
    return render(request, 'members.html')