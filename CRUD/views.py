from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def create_contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'addContact.html', {'form': form, 'action': 'add'})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'ContactList.html', {'contacts': contacts})

def update_contact(request, pk):
    student = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=student)
    return render(request, 'addContact.html', {'form': form, 'student': student, 'action': 'update'})

def delete_contact(request, pk):
    try:
        student = Contact.objects.get(pk=pk)
        student.delete()
        return redirect('contact_list')
    except Contact.DoesNotExist:
        return redirect('contact_list')