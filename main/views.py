from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'Welcome to Alhikam Mart',
        'name': 'M. Azmy Arya Rizaldi M.',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)