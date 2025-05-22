from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'New Contact Form Submission'
            body = (
                f"First Name: {form.cleaned_data['first_name']}\n"
                f"Last Name: {form.cleaned_data['last_name']}\n"
                f"Email: {form.cleaned_data['email']}\n"
                f"Phone: {form.cleaned_data['phone']}\n\n"
                f"Message:\n{form.cleaned_data['message']}"
            )
            send_mail(
                subject,
                body,
                form.cleaned_data['email'],  # From
                ['tigrarest@gmail.com'],     # To
                fail_silently=False,
            )
            return redirect('contactus')
    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})
