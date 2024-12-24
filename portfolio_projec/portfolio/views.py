from django.shortcuts import render
from .models import project

def projects(request):
    projects = project.objects.all()  # Recupera todos los proyectos
    return render(request, 'portfolio/projects.html', {
        'projects': projects  # Pasa los proyectos al template
    })
    
def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def contact(request):
    return render(request, 'portfolio/contact.html')