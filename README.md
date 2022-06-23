
# CRM-Django

Following [Study Gyaang](https://studygyaan.com/django)'s tutorial create a CRM from scratch I'm learning Django framework.

## Live Demo - http://dprampolini.pythonanywhere.com/

## References

 - [Video Tutorial](https://www.youtube.com/watch?v=H2lWpstb2WE&list=PLSPMgrv4IuJ4WLURdlzKNx4sgsyqW8d5q&index=2)
 - [Django Project Structure](https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files)
 - [Django Configuration](https://studygyaan.com/django/django-best-practice-configuring-settings-file)
 - [Free Bootstrap template website](https://startbootstrap.com/)
 - [Emailer Creation](https://studygyaan.com/django/how-to-send-email-in-django)
 - [Timepicker](https://trentrichardson.com/examples/timepicker)
 - [Free hosting (for development and test purpose)](https://www.pythonanywhere.com/)

 

## Deployment

Clone the git repository.

In the project folder run the following commands to install the virtual environment: 
```bash
  pip install virtualenv

  virtualenv env

  .\env\Scripts\activate
```

Or in alternative run:
```bash
  mkvirtualenv --python=/usr/bin/<python_version> <virtualenv_name>
```
Replace <python_version> with the python version of your environment, for example:
<python_version> = python3.9

Replace <virtualenv_name> with the name of the virtual environment, for example:
<virtualenv_name> = crm-virtualenv

In the virtual environment shell run the following command to install python dependancies:
```bash
  pip install -r requirements.txt
```

Configure the local_settings.py file with your database and email settings.

Run the following commands to make the migrations and populate the database:
```bash
  python manage.py migrate
```

Run the following command to create the superuser of the system:
```bash
  python manage.py createsuperuser
```
