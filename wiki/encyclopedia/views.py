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
    if not title:
        return render(request, "encyclopedia/error-message.html", {
            "name": name
        })
    markeddown = Markdown()
    title = markeddown.convert(title)
    print(title)
    return render(request, "encyclopedia/wiki-page.html", {
        "entry": title,
        "name": name
    })