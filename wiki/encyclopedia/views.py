from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    print(request)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    
    print(util.get_entry(request))
    return render(request, "encyclopedia/index.html")