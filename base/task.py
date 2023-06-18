from config.celery import app as celery_app
from .utils import *
from typing import Any


@celery_app.task
def send_email_task(subject: str, body: str):
    return send_email(subject=subject, body=body)


@celery_app.task
def import_massive_data(file: Any, object_type: str):
    records = generate_dataframe_records(file=file, object_type=object_type)
    return save_records(records=records, object_type=object_type)
