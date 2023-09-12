from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Raisa Fadilla',
        'class': 'PBP KI'
    }

    return render(request, 'main.html', context)
