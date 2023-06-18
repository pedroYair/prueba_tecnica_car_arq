from datetime import datetime

from django.shortcuts import render, redirect
from subjects import task
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from subjects import models
from base import task as base_task


@login_required
def import_subjects(request):
    scrapper = task.execute_subjects_scrapper()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"<strong>Fecha: {now}<br>Cursos importados: {scrapper.subjects_amount_success}<br>Cursos no importados: {scrapper.subjects_amount_error}</strong>"
    send_email_response = base_task.send_email(subject="Scrapper cursos", body=body)

    if scrapper.subjects_amount_success > 0:
        messages.success(request, f"{scrapper.subjects_amount_success} cursos importados exitosamente")

    message = f"{scrapper.subjects_amount_error} cursos no pudieron ser importados"
    if scrapper.subjects_amount_error > 0:
        messages.error(request, message)
    else:
        messages.info(request, message)

    if send_email_response:
        messages.success(request, "Email enviado!!")
    else:
        messages.error(request, "El email no pudo ser enviado!!")
    return redirect('subject:list_subjects')


@login_required
def list_subjects(request):

    subjects = models.Subject.objects.all().order_by('name')
    context = {'page_title': 'Cursos', 'subjects': subjects}

    return render(request, 'subject/list.html', context)
