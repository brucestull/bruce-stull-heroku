from django.shortcuts import render

from config.settings.common import THE_SITE_NAME


def blog(request):
    """
    View for the `blog.Blog` list view.
    """
    context = {
        'the_site_name': THE_SITE_NAME,
        'page_title': 'Blog',
    }
    return render(request, 'blog/blog.html', context)
