1. Install deps:
   pip install -r requirements.txt

2. Create .env from env.example:

3. Run broker:
   docker run -d -p 5672:5672 rabbitmq

4. Run worker:
   celery -A djangoProject worker -l INFO

5. Run Django server:
   python manage.py runserver
