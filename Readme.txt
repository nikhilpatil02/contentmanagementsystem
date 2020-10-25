Steps to run the project
1. Create the python3 virtual environment with command
=> python3.8 -m venv env 

2. Activate it
=> source env/bin/activate

3. Install the packages using below command
=> pip install -r requirements.txt

4. Run makemigration
=> python manage.py makemigrations

5. Run migrate
=> python manage.py migrate 

6. Create token
=> python manage.py createsuperuser --username user --email user@example.com
   python manage.py drf_create_token user

7. Run server
=> python manage.py runserver