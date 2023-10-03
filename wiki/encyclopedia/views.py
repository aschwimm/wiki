from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
from . import util


def index(request):
    print(request)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def check(request, name):
    title = util.get_entry(name)
    markeddown = Markdown()
    title = markeddown.convert(title)
    print(title)
    return HttpResponse(f"path works: {name}")