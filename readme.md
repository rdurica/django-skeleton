### Django skeleton ###
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/rdurica/django-skeleton/django?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/rdurica/django-skeleton?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/rdurica/django-skeleton?style=flat-square)
![GitHub](https://img.shields.io/github/license/rdurica/django-skeleton?style=flat-square)

Example full-stack skeleton for new projects.


### Key features ###
- Prepared Project/Application structure
- Necessary frond-end & back-end tools
- Configured REST API with Token Authentication
- Dependencies managed by pipenv & npm
- Configured webpack

#### Installation ####
1. Clone repository <code>git clone git@github.com:rdurica/django-skeleton.git</code>
2. Install python dependencies <code>pipenv install --dev</code>
3. Install front end dependencies <code>npm install --only=dev</code>
4. Compile js/css<code>npx webpack</code>
5. Copy settings file from **_env/dev.py** to **_env/local.py**
6. Configure your database & settings in <code>_env/local.py</code>
7. Run migrations <code>manage.py migrate</code>
8. Create administrator account <code>manage.py createsuperuser</code>
9. Run local server <code>manage.py runsslserver 127.0.0.1:8888</code>

#### Frontend ####
- [bootstrap 4](https://getbootstrap.com/docs/4.4/components/alerts/)
- [fortawesome](https://fontawesome.com/icons?d=gallery)
- [jquery](https://jquery.com/)
- [jquery-ui](https://jqueryui.com/)
- [sweetalert2](https://sweetalert2.github.io/)

#### Backend ####
- [django](https://www.djangoproject.com/)
- [django-rest-framework](https://www.django-rest-framework.org/)
- [django-simple-history](https://django-simple-history.readthedocs.io/en/latest/)
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [django-mail-panel](https://github.com/scuml/django-mail-panel)

#### API ####
URL
<code>https://127.0.0.1:8888/api/ </code>

Example
<code>curl -X GET https://127.0.0.1:8888/api/ -H 'Authorization: Token your-token-from-application' </code>
