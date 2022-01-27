from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import allcourses, details


def courses(request):
    ac = allcourses.objects.all()
    template = loader.get_template("appName1/courses.html")
    context = {"ac": ac, }
    return HttpResponse(template.render(context, request))


def details(request, course_id):
    course = get_object_or_404(allcourses, pk=course_id)
    return render(request, "appName1/details.html", {'course': course})


def your_choice(request, course_id):
    course = get_object_or_404(allcourses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except(KeyError, allcourses.DoesNotExist):
        return render(request, 'appName1/details.html',
                      {'course': course,
                       'error_message': 'invalid option, try again?'})
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'appName1/details.html', {'course': course})
