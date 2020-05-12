from django.shortcuts import render


def project_home(request):
    context = {'apps': ['polling', 'blogging']}
    return render(request, 'home.html', context)