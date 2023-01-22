from django.shortcuts import render

from config.settings.common import THE_SITE_NAME
from projects.models import Project


def projects(request):
    """
    View for the `projects.Project` list view.
    """
    projects = Project.objects.all()
    context = {
        'the_site_name': THE_SITE_NAME,
        'page_title': 'Projects',
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    """
    View for the `projects.Project` detail view.
    """
    project = Project.objects.get(pk=pk)
    context = {
        'the_site_name': THE_SITE_NAME,
        'page_title': project.title,
        'project': project,
    }
    return render(request, 'projects/project.html', context)
