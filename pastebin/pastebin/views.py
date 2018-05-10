from django.shortcuts import render, get_object_or_404
from .models import Paste
from .forms import PasteForm

def index(request):
    parameters = PasteForm()
    ctx = {'parameters':parameters}
    return render(request, 'pastebin/index.jinja2', ctx)


def paste(request, id):
    ctx = {}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):

    if language == 'js':
        pastes = Paste.objects.filter(language = "Javascript")
    elif language == 'python':
        pastes = Paste.objects.filter(language = "Python")
    else:
        pastes = Paste.objects.filter(language = "Outros")
    ctx = {'pastes': pastes}

    return render(request, 'pastebin/paste-language.jinja2', ctx)

def paste_new(request):
    parameters = Paste.objects.create(
        title = request.POST.get('title'),
        language = request.POST.get('language'),
        content = request.POST.get('content')
    )
    ctx = {'paste':parameters}
    return render(request, 'pastebin/paste-detail.jinja2', ctx)