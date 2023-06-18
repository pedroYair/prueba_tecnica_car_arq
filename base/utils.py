from config.settings import settings
from django.core import mail
from django.http import HttpResponse
import openpyxl
from typing import Any, List
import pandas as pd
from teachers.models import Teacher
from base import constants


class UnableToProcessRecordFile(Exception):
    pass


def send_email(subject, body):
    success = True
    try:
        mail.send_mail(subject=subject,
                       message=subject,
                       html_message=body,
                       from_email=settings.EMAIL_HOST_USER,
                       recipient_list=[settings.DEFAULT_TO_EMAIL],
                       fail_silently=False
                       )
    except Exception as e:
        print(f"Error: El email no pudo ser enviado!!")
        success = False

    return success


def generate_excel(file_name: str, wb) -> HttpResponse:
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = f'attachment; filename="{file_name}.xlsx"'
    wb.save(response)
    return response


def get_copy_template(object_type: str):
    if object_type == constants.TEACHERS:
        wb = openpyxl.load_workbook(f"{settings.APPS_DIR}/fixtures/XLSX/plantilla_profesores.xlsx")
        return generate_excel(file_name="Formato registro masivo profesores", wb=wb)


def generate_dataframe_records(file: Any, object_type: str) -> List[dict]:
    try:
        io_record = pd.ExcelFile(path_or_buffer=file)
        dataframe = pd.read_excel(io=io_record, engine="openpyxl")
    except Exception:
        raise UnableToProcessRecordFile()
    else:
        if object_type == constants.TEACHERS:
            dataframe = dataframe.rename(
                columns={
                    "DOCUMENTO": "document_number",
                    "TIPO DOCUMENTO": "document_type",
                    "NOMBRES": "first_name",
                    "APELLIDOS": "last_name",
                    "FECHA NACIMIENTO": "date_of_birth",
                    "GENERO": "gender",
                    "TELEFONO": "phone",
                    "EMAIL": "email",
                    "DIRECCION": "address"
                }
            )
            dataframe["date_of_birth"] = pd.to_datetime(
                dataframe["date_of_birth"], errors="coerce"
            )
            dataframe["document_type"] = dataframe["document_type"].str.upper()
            dataframe["gender"] = dataframe["gender"].str.upper()

        return dataframe.to_dict(orient="records")


def save_records(records: List[dict], object_type: str) -> dict:
    success_amount = 0
    errors_amount = 0
    if object_type == constants.TEACHERS:
        for item in records:
            if str(item["phone"])[0:3] != '+57':
                phone = '+57' + str(item["phone"])
            else:
                phone = item["phone"]

            try:
                Teacher.objects.create(
                    document_number=item["document_number"],
                    document_type=item["document_type"],
                    first_name=item["first_name"],
                    last_name=item["last_name"],
                    date_of_birth=item["date_of_birth"],
                    gender=item["gender"],
                    phone=phone,
                    email=item["email"],
                    address=item["address"]
                )
                success_amount += 1
            except Exception as e:
                print(str(e), "++++++++++++++")
                errors_amount += 1
                continue

    return {"success_amount": success_amount,
            "errors_amount": errors_amount}
