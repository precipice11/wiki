from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    content = util.get_entry(title)

    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"The entry '{title}' does not exist."
        })

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    query = request.GET.get("q", "").strip()
    entries = util.list_entries()
    matches = []

    if query in entries:
        return render(request, "encyclopedia/entry.html", {
            "title": query,
            "content": util.get_entry(query)
        })
    else:
        for entry in entries:
            if query.lower() in entry.lower():
                matches.append(entry)
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "matches": matches
        })