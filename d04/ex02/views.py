from django.shortcuts import render
from django.utils import timezone

from .forms import DjangoForm

from pathlib import Path

# Create your views here.

def django_form(request):
    form = DjangoForm()

    if request.method == "POST":
        form = DjangoForm(request.POST)
        # print(form)
        if form.is_valid:
            print(form)
            # breakpoint()
            data = (form.cleaned_data).get('text_field')
            add_logs(data)
            # print(form_list)
    else:
        form = DjangoForm()

    p = Path('./logs')
    if p.exists():
        with p.open("r", encoding="utf-8") as f:
            text = f.read()
        form_list = text.split('\n')
    else: 
        form_list = []
    context = {'form': form, 'form_list': form_list}
    template_name = 'ex02/django_form.html'

    form = DjangoForm()

    return render(request, template_name, context)


def add_logs(submission):
    p = Path('./logs')
    if p.exists():
        with p.open("a+", encoding="utf-8") as fd:
            fd.write("{} {}\n".format(timezone.localtime().strftime("%Y-%m-%d %H:%M:%S"), submission))

