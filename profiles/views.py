from django.shortcuts import render


def profile(request):
    """ View to show the users profile page """
    template = 'profile/profile.html'
    context = {}

    return render(request, template, context)
