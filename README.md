**Assignment 2**

**How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).**
1. Create a new django project.
    - First, I created a new directory named “assignment2_pbp” on my computer files.
    - Then, I opened the terminal and navigated to the “assignment2_pbp” directory.
    - Inside that directory, I created a virtual environment by running “python -m venv env” and activated it by running “source env/bin/activate”. When the virtual environment is already started, the terminal will display “(env)”. 
    - I made a “requirements.txt” file in the directory and used “pip install -r requirements.txt”to install the necessary dependencies. 
    - Following that, I created a django project named “assignment2_pbp” by running “django-admin startproject assignment2_pbp .”. 
    - I opened the directory on my vscode, opened the “settings.py” file, and changed the ALLOWED_HOSTS variable to “ALLOWED HOSTS = [“*”]”. 
    - To make sure the “manage.py” file is activated, I ran “.manage.py runserver” and then browsed https://localhost:8000 to see if my Django application had already been successfully constructed. After that, I made a new public GitHub repository named “assignment2-pbp” and added, committed, and pushed my “assignment2_pbp” directory to it. 
    - In my directory, I created a “.gitignore” file. Then, I added, committed, and pushed my “.gitignore” file.

2. Create an app with the name “main” on that project.
    - I ran “python manage.py startapp main” to create a new application.
    - Then, I opened the “settings.py” file in my directory and added “main” to the list of existing applications.
    
3. Create a URL routing configuration to access the “main” app.
    - I added this following code in my “urls.py” inside my “assignment2_pbp” directory
    ```
    from django.urls import path, include
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('main/', include('main.urls')),
    ]
    ```

4. Create a model on the “main” app.
    - On the “models.py” inside the “main” app, I added this following code:
```
from django.db import models
class Product(models.Model):
name = models.CharField(max_length=255)
amount = models.IntegerField()
description = models.TextField()
```

5. Create a function in “views.py” that returns an HTML template.
    - I added this following code into the “views.py” file:
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

6. Create a routing in ”urls.py” to map the function in “views.py”.
    - I added this following code in "urls.py" inside the "main" app:
```
from django.urls import path
from main.views import show_main

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    ]
```

7. Deploy the app to Adaptable so it can be accessed through the internet.
    - I opened adaptable.io and signed in by using my GitHub account.
    - I clicked "New App" and choosed "Connect an Existing Repository"
    - Then, I choosed "assignment2_pbp" repository for the application to be deployed and selected "master" branch to use as the deployment branch.
    - Following that, I choosed "Python App Template" as the deployment template and "PostgreSQL as the database type to be used.
    - I changed the pyton version to 3.10 and typed "python manage.py migrate && gunicorn assignment2_pbp.wsgi" for the start command.
    - To start the process of deploying the application,  I selected "Deploy App" and then checked the "HTTP Listener on PORT option".
   
9. Create a README.md that contains a URL to access your deployed app and answers to the questions
    - I created the README.md and answered all the questions in this GitHub Repository.


**Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).**

![djangodiagram](https://github.com/raisaafadilla/assignment2-pbp/assets/134634814/0c5c586d-b443-421c-a76c-c678b0f4a887)


**What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?**

A virtual environment isolates and manages project-specific dependencies. It is possible to create a Django web app without a virtual environment, however it is not recommended because it may generate dependency problems.

**What is MVC, MVT, and MVVM? Explain the differences between the three.**
1. MVC
   - Model: stores the application data and responsible, responsible for handling the real-world business rules, and communication with the database and network layers.
   - View: user interface layer that holds components that are visible on the screen.
   - Controller: updates the application's state by accepting user input, processing it, and communicating with the Model and View.
   
3. MVT
   - Model: stores the application data and responsible, responsible for handling the real-world business rules, and communication with the database and network layers.
   - View: user interface layer that holds components that are visible on the screen.
   - Template: manages the state of the View and takes actions according to the user's input notification from the View
   
5. MVVM
   - Model: stores the application data and responsible, responsible for handling the real-world business rules, and communication with the database and network layers.
   - View: user interface layer that holds components that are visible on the screen.
   - ViewModel: exposes the essential data streams to the View, acting as a bridge between the Model and the View. 

Link : https://assignment2-pbp.adaptable.app


**Assignment 3**

**What is the difference between POST form and GET form in Django?**
The POST method is used by Django's login form, in which the browser packages the form's data, encrypts it for transmission, sends it to the server, and then waits for the server to respond. In contrast, the GET method constructs a URL by assembling a string composed of the submitted data, encompassing both the data keys, values, and the target destination.

**What are the main differences between XML, JSON, and HTML in the context of data delivery?**
HTML is designed to describe how data is displayed on the web pages. It specifies how text, graphics, and links should be organized and presented on the web for web browser rendering. 
Both XML and JSON are used to store and transport data, however their approaches to data representation and structuring are different. JSON is frequently chosen because it is straightforward, readable, and appropriate for data exchange in modern web applications, while XML is still useful in some areas where extensibility and hierarchical data structures are essential.

**Why is JSON often used in data exchange between modern web applications?**
JSON is simple and readable. It uses a human-readable format by using key-values pairs and arrays. Moreover, JSON supports a wide variety of data structures, including arrays, objects, strings, numeric values, and boolean values. This flexibility makes it suitable for illustrating complex data structures.

**Explain how you implemented the checklist above step-by-step.**
1. Create a form input to add a model object to the previous app.
    - I added a new file called forms.py to the main folder. The form structure for new item data, including name, price, and description, will be made using this file.
    - Then, I inserted some imports at the beginning of the views.py file in the main folder. I also created a new function named create_product.
    - I added create_product as the import and a new url path inside the url patterns list to access the previously imported function in urls.py inside the main folder.
    - I made a new HTML file called create_product.html in the templates subdirectory of the main folder.
    - I added the code below to the main.html file to create a table with the product data and a button that directs users to the form page.
```
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Below is how to show the product data {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

2. Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats and create URL routing for each of the views.
    - I created a new function named show_xml.
    - I added show_xml as the import and a new url path inside the url patterns list to access the previously imported function in urls.py inside the main folder.
    - The same thing with XML, returning data as JSON is also done by creating a new function in the views.py file and adding the function as import and a new url path inside the url patterns list.
    - For retrieving data based on ID in XML and JSON format : In views.py inside the main folder, I added a new function show_xml_by_id and show_json_by_id.
    - I added a return statement that returns a HttpResponse with the serialized data in either XML or JSON format and sets the content_type parameter to "application/xml" or "application/json".
    - In the urls.py file, I imported all the functions that I created before and added all the url paths into the urlpatterns list.

**Screenshots of the results in Postman.**

1. HTML
   <img width="1512" alt="Screenshot 2023-09-20 at 11 32 09 AM" src="https://github.com/raisaafadilla/assignment2-pbp/assets/134634814/fea9c14e-7ace-469a-9ec5-2fe114019392">

3. XML
   <img width="1512" alt="Screenshot 2023-09-20 at 11 32 20 AM" src="https://github.com/raisaafadilla/assignment2-pbp/assets/134634814/7ae95c72-e6f6-4cb0-9909-019cb9bbbb5f">

4. JSON
   <img width="1512" alt="Screenshot 2023-09-20 at 11 32 38 AM" src="https://github.com/raisaafadilla/assignment2-pbp/assets/134634814/3216861f-683a-4000-aa70-fcf08dea72ff">

6. XML by ID
   <img width="1512" alt="Screenshot 2023-09-20 at 11 32 52 AM" src="https://github.com/raisaafadilla/assignment2-pbp/assets/134634814/e4693b35-0b1e-40db-9d88-63c523bf57d8">

8. JSON by ID
   <img width="1512" alt="Screenshot 2023-09-20 at 11 33 02 AM" src="https://github.com/raisaafadilla/assignment2-pbp/assets/134634814/5a76c0b2-19cd-4c49-af5d-f7384daeab1b">



