from django.shortcuts import render, redirect


def index(request):
    return redirect('/blog/')


def about_me(request):
    return render(
        request,
        'basecamp/about_me.html'
    )
