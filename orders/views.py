from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def example_view(request):
    template = loader.get_template("create.html")
    context = {
        "test_list": list(range(5)),
    }
    return HttpResponse(template.render(context, request))
