**How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).**
1. Create a new django project.
First, I created a new directory named “assignment2_pbp” on my computer files.
Then, I opened the terminal and navigated to the “assignment2_pbp” directory.
Inside that directory, I created a virtual environment by running “python -m venv env” and activated it by running “source env/bin/activate”.
When the virtual environment is already started, the terminal will display “(env)”. 
I made a “requirements.txt” file in the directory and used “pip install -r requirements.txt”to install the necessary dependencies. 
Following that, I created a django project named “assignment2_pbp” by running “django-admin startproject assignment2_pbp .”. 
I opened the directory on my vscode, opened the “settings.py” file, and changed the ALLOWED_HOSTS variable to “ALLOWED HOSTS = [“*”]”. 
To make sure the “manage.py” file is activated, I ran “.manage.py runserver” and then browsed https://localhost:8000 to see if my Django application had already been successfully constructed. 
After that, I made a new public GitHub repository named “assignment2-pbp” and added, committed, and pushed my “assignment2_pbp” directory to it. 
In my directory, I created a “.gitignore” file. Then, I added, committed, and pushed my “.gitignore” file.
2. Create an app with the name “main” on that project.
I ran “python manage.py startapp main” to create a new application.
I opened the “settings.py” file in my directory and added “main” to the list of existing applications.
3. Create a URL routing configuration to access the “main” app.
I added this following code in my “urls.py” inside my “assignment2_pbp” directory
```
from django.urls import path, include
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/', include('main.urls')),
]
```
4. Create a model on the “main” app
On the “models.py” inside the “main” app, I added this following code:
```
from django.db import models
class Product(models.Model):
name = models.CharField(max_length=255)
amount = models.IntegerField()
description = models.TextField()
```
5. Create a function in “views.py” that returns an HTML template
I added this following code into the “views.py” file:
```
from django.shortcuts import render
def show_main(request):
context = {
'name': 'Raisa Fadilla',
'class': 'PBP KI'
}
return render(request, 'main.html', context)
```
Then, I changed the “main.html” code into this:
```
<h1>Product List Page</h1>
<h5>Name:</h5>
<p>{{ name }}</p>
<h5>Class:</h5>
<p>{{ class }}</p>
```
6. Create a routing in ”urls.py” to map the function in “views.py”
I added this following code in "urls.py" inside the "main" app:
```
from django.urls import path
from main.views import show_main

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    ]
```
7. Deploy your app to Adaptable so it can be accessed through the internet.
8. Create a README.md that contains a URL to access your deployed app and answers to the questions
I created the README.md and answered all the questions in this GitHub Repository.


**Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).**


**What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?**
A virtual environment isolates and manages project-specific dependencies, ensuring they don't clash with other projects. Building a Django web app without a virtual environment is possible but discouraged because it can lead to dependency conflicts.

**What is MVC, MVT, and MVVM? Explain the differences between the three.**
1. MVC
   Model: represents the application's business logic and data.
   View: processes user interface elements and displays the data to the user.
   Controller: updates the application's state by accepting user input, processing it, and communicating with the Model and View.
   
3. MVT
   Model: represents the application's business logic and data.
   View: processes user interface elements and displays the data to the user.
   Template: handles presentation logic, such as HTML structure.
   
5. MVVM
   Model: represents the application's business logic and data.
   View: processes user interface elements and displays the data to the user.
   ViewModel: acts as a bridge between the Model and View, converting data from the Model into a format that the View can easily display.
   



