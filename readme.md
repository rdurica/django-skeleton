### Example ###
Example skeleton for new projects

#### Installation ####
1. Clone <code>git clone git@github.com:rdurica/django-skeleton.git</code> repository
2. Create virtualenv using **pipenv**
3. Install python dependencies <code>pipenv install --dev</code>
4. Install front end dependencies <code>npm install --only=dev</code>
5. Compile js/css<code>npx webpack</code>
6. Copy settings file from **_env/dev.py** to **_env/local.py**
7. Configure your database & settings in <code>_env/local.py</code>
8. Run migrations <code>manage.py migrate</code>
9. Create administrator account <code>manage.py createsuperuser</code>
10. Run local server <code>manage.py runserver</code>

#### Technology ####
- [python 3.8.2 64bit](https://www.python.org/downloads/release/python-382/)
- [npm](https://nodejs.org/en/)
- django
- [django-rest-framework](https://www.django-rest-framework.org/)
- webpack
- jquery
- bootstrap4

#### API ####
URL
<code>http://127.0.0.1:8000/api/ </code>

Example
<code>curl -X GET http://127.0.0.1:8000/api/ -H 'Authorization: Token your-token-from-application' </code>
