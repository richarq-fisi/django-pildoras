```sh
virtualenv -p python  venv
pip install Django
django-admin.exe startproject ProyectoWeb

cd ProyectoWeb
django-admin.exe startapp ProyectoWebApp
django-admin.exe startapp Servicios


pip install Pillow
python .\manage.py makemigrations
python .\manage.py migrate

python manage.py createsuperuser
python manage.py run server

django-admin.exe startapp Blog
python manage.py makemigrations Blog
python manage.py migrate Blog
```
