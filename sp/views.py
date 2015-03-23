from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView

from sp.models import Squad, Student


# Create your views here.
class SquadsListView(ListView):
    model = Squad


class StudentsListView(ListView):
    model = Student


class SquadDetailView(DetailView):
    model = Squad


def squad_list(request, template_name):
    squads = {'squad_list': Squad.objects.all()}
    return render_to_response(template_name, squads, context_instance=RequestContext(request))


def squad_detail(request, template_name, squad_name):
    squad = Squad.objects.filter(name=squad_name)
    context = {'squad': squad[0]}
    return render_to_response(template_name, context, context_instance=RequestContext(request))


def student_detail(request, template_name, squad_name, student_id):
    student = Student.objects.filter(pk=student_id)
    context = {'squad_name': squad_name, 'student': student[0]}
    return render_to_response(template_name, context, context_instance=RequestContext(request))