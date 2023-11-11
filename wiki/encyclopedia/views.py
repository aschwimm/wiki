from django.shortcuts import render
from django import forms
from markdown2 import Markdown
from django.http import HttpResponse
from django.shortcuts import redirect
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, min_length=1 ,max_length=250)
    content = forms.CharField(widget=forms.Textarea, min_length=1)

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
def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create-page.html", {
            "form": NewPageForm
        })
    elif request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(request, "encyclopedia/error-for-entry.html", {
                    "entry": title
                })
            else:
                util.save_entry(title, content)
                return redirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/index.html")
    
def edit_wiki(request, name):
    if request.method == "GET":
        return render(request, "encyclopedia/edit-page.html", {
            "title": name
        })