from config.celery import app as celery_app
from subjects import subjects_scrapper


@celery_app.task
def execute_subjects_scrapper():
    scrapper = subjects_scrapper.Scrapper()
    scrapper.run()
    return scrapper
