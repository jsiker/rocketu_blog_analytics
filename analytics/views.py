from django.shortcuts import render

from analytics.models import Page, View


def analytics(request):
    return render(request, 'analytics.html',{
        'pages': Page.objects.order_by('-url'),
        'views': Page.views

    })