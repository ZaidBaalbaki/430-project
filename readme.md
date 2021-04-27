1. Clone this repository by downloading it or by ``git clone https://github.com/ZaidBaalbaki/430-project.git ``
2. Replace SMTP server details in settings.py file:-
	
	- EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
	- EMAIL_HOST = 'smtp.your-host.com'
	- EMAIL_USE_TLS = True
	- EMAIL_PORT = 587
	- EMAIL_HOST_USER = 'user@your-host.com'
	- EMAIL_HOST_PASSWORD = 'your-password'

* Make sure you are inside the folder ``mentcare/``
5. Run ``py manage.py makemigrations`` to create the migrations.
6. Run ``py manage.py migrate`` to create the app models.
8. Start the development server using ``py manage.py runserver `` 
11. Visit http://127.0.0.1:8000/signup/ to for patient signup.
12. Visit http://127.0.0.1:8000/login/ to login for doctors, clinics, or patients.
10. Clinics can add doctors.


* Clinic credentials:
Email = clinic1@clinic.com
Pass = clinic1234
