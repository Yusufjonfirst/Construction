from django.shortcuts import render

from pages.models import OurWorkModel


def home_pages_view(request):
    return render(request, 'main.html')


def about_pages_view(request):
    return render(request, 'about.html')


def contact_pages_view(request):
    return render(request, 'contact.html')


def blog_pages_view(request):
    return render(request, 'blog.html')


def project_pages_view(request):
    return render(request, 'project.html')


def services_pages_view(request):
    return render(request, 'service.html')


def single_pages_view(request):
    return render(request, 'single.html')


def our_works_view(request):
    all_works = OurWorkModel.objects.all()
    context = {
        "project_list": all_works
    }
    return render(request, 'main.html', context)
