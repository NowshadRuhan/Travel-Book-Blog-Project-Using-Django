# Trevel-Book Blog Project Using Django
 Trevel-Book blog project one of my django project. Here, i create a full blog project to use all of blog functionality, using language python framework Django.

# About Project:
**In this project i used virtual environment, two apps, media folder, static folder, templates and others pip library/packages.**

## About Virtual-Environment:
virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

- [x] pip install virtualenv **[For install virtual environment for python]**
- [x] virtualenv --version **[for check your virtual environmentversion]**
- [x] py -m venv your_virtualenv_name  **[for create and start your virtual environment]**
- [x] cd Scrripts\activate **[for activate your virtual environment]**
- [x] deactivate **[for deactivate your virtual environment]**

## About Crispy forms in python:
Django-crispy-forms supports several frontend frameworks, such as Twitter Bootstrap (versions 2, 3, and 4), Uni-form and Foundation. You can also easily adapt your custom company's one, creating your own, see the docs for more information. You can easily switch among them using CRISPY_TEMPLATE_PACK setting variable.

### Installing django-crispy-forms:

**Install latest stable version into your python environment using pip:**
- pip install django-crispy-forms

**If you want to install development version (unstable), you can do so doing:**
- pip install git+git://github.com/django-crispy-forms/django-crispy-forms.git@dev#egg=django-crispy-forms

**Once installed add crispy_forms to your INSTALLED_APPS in settings.py:**
```
INSTALLED_APPS = (
    ...
    'crispy_forms',
)
```




