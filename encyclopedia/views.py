from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })