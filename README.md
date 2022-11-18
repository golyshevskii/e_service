## User's manual

1. clone the repository to a specific directory

    > git clone https://github.com/golyshevskii/e_service.git

2. activate *virtual environment*

    > source venv/bin/activate

3. install the required python libraries

    > pip install -r requirements.txt

4. start docker app

5. run rebbitmq on docker (docker app running)

    > docker run -d -p 5672:5672 rabbitmq

6. run the application using the command

    > python3 manage.py runserver

7. run celery inside project dir

    > celery -A core worker --loglevel=info

8. go to the web application page using *localhost*

    > http://127.0.0.1:8000/

9. create a new user

10. send email

### administration page: admin/admin