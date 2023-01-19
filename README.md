# Setting Up Locally For Development
---

Table Of Contents


- [Setting Up Locally For Development](#setting-up-locally-for-development)
  - [Requirements](#requirements)
  - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  - [Step 4](#step-4)
  - [Step 5](#step-5)
  - [Step 6](#step-6)


## Requirements
    
**Python**

[Link To Download Python](https://www.python.org/downloads/)

---
## Step 1

Clone the project and navigate into the main project  folder 

---

## Step 2

Create A Virtual Environment

Run  `py -m venv venv` in the command prompt in the main project folder *for windows users*

Activate the virtual environment by runing `venv\Scripts\activate` in the commant prompt *for windows users*

---
## Step 3

Run `pip install -r requirements.txt` in the commant prompt *for windows users*

---
## Step 4

    Environment Variables
Create a .env file and put in it the following:

| Name                    | Value                                              |
|:------------------------|:---------------------------------------------------|
| SECRET_KEY              | [Click to here generate one](https://djecrety.ir/) |
| DEBUG                   | **True**                                           |





---
## Step 5

Run these commands in the terminal

```

py manage.py makemigrations

py manage.py migrate

py manage.py runserver

```
---
## Step 6

Navigate to [Api Documentation](http://localhost:8000/) for api documentation

---
## Note:
If you have no previous knowledge on Python or django here are links to their documentations:

[Python Documentation](https://docs.python.org/3/tutorial/index.html)

[Django Documentation](https://docs.djangoproject.com/en/4.1/intro/)

[Django Rest Framework Documentation](https://www.django-rest-framework.org/tutorial/quickstart/)

---