from django.shortcuts import render, redirect

from .forms import ContactForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            return redirect('tasks')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'pages/contact.html', context)