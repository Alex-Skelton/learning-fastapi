from project import create_app
from project.users.tasks import divide

app = create_app()
celery = app.celery_app
x = divide(2,1)