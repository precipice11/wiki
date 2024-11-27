from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from . import util
import random


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

def makepage(request):
    return render(request, "encyclopedia/makepage.html")

def save(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()
        if not title or not content:
            return render(request, "encyclopedia/error.html", {
            "message": "Both title and content are required when submitting a page."
        }) 
        titles = util.list_entries()
        # if title in titles:
        #     return render(request, "encyclopedia/error.html", {
        #         "message": f"The entry '{title}' already exists."
        #     })
        # else:
        util.save_entry(title, content)
        return redirect("encyclopedia:entry_page", title=title)

    return render(request, "encyclopedia/error.html", {
        "message": "Invalid request method."
    })

def edit(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/editpage.html",  {
            "title": title,
            "content": content
        })
    else:
        return render(request, "encyclopedia/error.html", {
                "message": f"The entry '{title}' already exists."
            })

def randompage(request):
    titles = util.list_entries()
    title = random.choice(titles)
    return redirect("encyclopedia:entry_page", title=title)

