from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(reauest):
    templates = 'pages/rules.html'
    return render(reauest, templates)
