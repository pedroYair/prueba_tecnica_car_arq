from django.shortcuts import render, redirect
from subjects import task
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from subjects import models


@login_required
def import_subjects(request):
    scrapper = task.execute_subjects_scrapper()
    messages.success(request, f"{scrapper.subjects_amount_success} Cursos importados exitosamente")
    messages.error(request, f"{scrapper.subjects_amount_error} Cursos no pudieron ser importados")
    # return JsonResponse({"response": "ok", "amount": scrapper.subjects_amount})
    return redirect('subject:list_subjects')


@login_required
def list_subjects(request):

    subjects = models.Subject.objects.all().order_by('name')
    context = {'page_title': 'Cursos', 'subjects': subjects}

    return render(request, 'subject/list.html', context)
