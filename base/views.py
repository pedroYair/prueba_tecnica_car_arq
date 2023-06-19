import os

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from base.forms import LoadDataForm
from django.contrib import messages
from base import constants, task, utils


@login_required
def import_massive_data(request):
    if request.method == "POST":
        form = LoadDataForm(request.POST, request.FILES)
        if form.is_valid():
            type_action = form.cleaned_data["type_action"]
            object_type = form.cleaned_data["object_type"]

            if type_action == constants.LOAD:
                file = form.cleaned_data["file"]
                file_type = os.path.splitext(file.name)[1]
                file_type = file_type.upper()[1:]
                result = task.import_massive_data(file=file, object_type=object_type, file_type=file_type)

                success_amount = result["success_amount"]
                errors_amount = result["errors_amount"]
                success_message = ""
                error_message = ""
                subject = ""
                body = ""

                if object_type == constants.TEACHERS:
                    success_message = f"{ success_amount} profesor(es) importados exitosamente"
                    error_message = f"{errors_amount} profesor(es) no pudieron ser importados"
                    subject = "Importaciòn masiva de profesores"
                    body = f"<strong>Profesor(es) importados: {success_amount}<br>Profesor(es) no importados: {errors_amount}</strong>"

                if success_amount > 0:
                    messages.success(request, success_message)

                if errors_amount > 0:
                    messages.error(request, error_message)
                else:
                    messages.info(request, error_message)

                send_email_response = task.send_email(subject=subject, body=body)

                if send_email_response:
                    messages.success(request, "Email enviado!!")
                else:
                    messages.error(request, "El email no pudo ser enviado!!")

                return redirect("base:import_massive_data")
            else:
                return utils.get_copy_template(object_type=object_type)
    else:
        form = LoadDataForm()
    return render(request, "base/add.html", {'page_title': 'Importación masiva', "form": form})

