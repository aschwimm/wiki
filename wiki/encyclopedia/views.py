from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import Markdown
from . import util


def index(request):
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
    print(name)
    return render(request, "encyclopedia/wiki-page.html", {
        "entry": title,
        "name": name
    })
def search(request):
    test = request.GET.get('q')
    check_search = util.get_entry(test)
    all_entries = util.list_entries()
    matched_entries = []
    if check_search:
        markeddown = Markdown()
        check_search = markeddown.convert(check_search)
        return render(request, "encyclopedia/wiki-page.html", {
            "entry": check_search,
            "name": check_search
        })
    for i in all_entries:
        if test in i:
            matched_entries.append(i)
    return render(request, "encyclopedia/search-page.html", {
        "entries": matched_entries
    })