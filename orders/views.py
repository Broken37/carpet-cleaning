from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def example_view(request):
    template = loader.get_template("example.html")
    context = {
        "message": "this is message",
    }
    return HttpResponse(template.render(context, request))
