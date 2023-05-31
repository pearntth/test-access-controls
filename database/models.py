from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Contact(models.Model):
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='added_by')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('added_by',)
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'phone_number' : 'Phone Number'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.added_by = user
