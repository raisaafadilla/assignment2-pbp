## Assignment 2

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


## Assignment 3

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


## Assignment 4

**What is UserCreationForm in Django? Explain its advantages and disadvantages.**

Django UserCreationForm is used to create a new user who can access a website application. The advantage of using UserCreationForm is that it provides a practical method for creating user registration forms without having to individually describe each field and rule validation. However, UserCreationForm does not cover all the use cases for user registration. If people want to collect additional user data or complicated requirements during the registration, they must design a custom registration form.

**What is the difference between authentication and authorization in Django application? Why are both important?**

Authentication is the process of verifying user identities, while authorization is the process of verifying what specific data a user has access to. Authentication and authorization is important because they are two fundamental information security procedures that are used to protect systems and data. 

**What are cookies in website? How does Django use cookies to manage user session data?**

What’s referred to as a ‘cookie’ in a website is a piece of data collected as you browse to identify specific users and improve your browsing experience later on. To identify each browser and its associated session with the site, a cookie containing a special session id is used by Django. Those actual session datas are stored in the site database by default, which is more secure than cookie-stored data because they are more vulnerable to malicious users. 

**Are cookies secure to use? Is there potential risk to be aware of?**

The safety of cookies relies on how the developer handles them. Developers need to be careful about what information they put in cookies, use security features, and consider user privacy to make sure cookies are safe in their apps. Cookies can also track what users do on different websites, which can cause privacy concerns. Moreover, if cookies store too much data, it could make websites slower and increase the risk of exposing sensitive information.

**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**

1. Implement registration, login, and logout functions to allow users to access the previous application.
    - Registration :
      I first imported the necessary modules, including redirect, UserCreationForm, and messages, in the views.py file located within the main directory. Next, I implemented a register function       in the views.py file to automatically generate a registration form. To complement this, I created a corresponding register.html file within the main/templates folder to render the               registration form. To ensure that users can access this registration page, I went into the urls.py file in the main directory, imported the register function, and established a new URL          path for the registration page.
    - Login :
      I included the authenticate and login functions in the views.py file to facilitate user authentication and login upon successful authentication. Additionally, I crafted a login_user             function within the same views.py file to handle the login process. For the presentation layer, I created a dedicated HTML file, login.html, inside the main/templates folder to render the       login form and user interface. To ensure user accessibility to the login page, I made corresponding updates in the urls.py file located in the main directory by importing the login_user         function and establishing a new URL path specifically for user login.
    - Logout
      I imported the logout module in the views.py file located in the main folder. To handle user logout requests, I implemented the logout_user function within the same views.py file. To            provide users with a convenient means of logging out, I modified the main.html file situated within the main/templates folder to include a visible logout button or link. To ensure that          the logout feature is accessible, I updated the urls.py file inside the main directory by importing the logout_user function and establishing a new URL path dedicated to user logout.
      
3. Connect Item model with User.
   - In model.py file inside the main folder, I imported user and added user variable (user = models.ForeignKey(User, on_delete=models.CASCADE)). Then, in show_main function, I added ('name':        request.user.username) inside the context variable.
   
5. Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.
   - In the views.py file located within the main subdirectory of my Django project, I made several important updates. First, I included imports for HttpResponseRedirect, reverse, and datetime       to handle redirection, URL reversing, and date-related functionalities. Within the login_user function, I introduced modifications within the "if user is not None" block to enhance the          login process. Additionally, in the show_main function, I incorporated the statement 'last_login': request.COOKIES['last_login'] to include the 'last_login' cookie data in the response,         thereby enabling it to be displayed on the web page. To improve user logout functionality in the logout_user function, I introduced the line response.delete_cookie('last_login') to              effectively delete the 'last_login' cookie when a user logs out. Finally, to display the 'last login' data to users, I inserted the "Last login session:" code into the main.html file.


## Assignment 5

**Explain the purpose of some CSS element selector and when to use it.**

CSS selectors are used to select the specific HTML elements that we want to style on a web page. In class, we learned three types of CSS selectors, which are element selector, ID selector, and class selector. Element selector is for choosing things on the page that have the same HTML tag. ID selector is for picking out something special on a webpage using its unique ID. Class selector is for choosing things that have a particular class attribute.

**Explain some of the HTML5 tags that you know.**

    - <a> is used for making a hyperlink.
    - <br> is used for making a single line break.
    - <button> is used for creating a clickable button.
    - <div> is used for specifying a section in a document.
    - <hr1> to <hr6> is used to define HTML headings.

**What are the differences between margin and padding?**

Margin and padding are two elements in CSS that create space around elements on a web page. Margin controls the space outside the border of an element, while padding controls the space inside the border of an element. 

**What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?**

Tailwind is a newer tool that's still improving, while Bootstrap has been around for a while and is great for saving time when making websites.
When we use Tailwind to build a website, we have more freedom to make it special and unique because we start from the beginning. But with Bootstrap, our website might look similar to others because it starts with a ready-made design.
If we want our website to be very different and customized, Tailwind is the way to go because we can make it our own. However, if we need to focus more on the technical backend stuff and want a common website layout, Bootstrap is a better choice because it comes with its own pre-made template.

**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**

I picked Bootstrap as the CSS framework for my assignment. I made changes to the login page, registration, and product creation using Bootstrap's cards. I also improved things like colors, fonts, padding, and more. On the main page, I customized the list table, added a navigation bar, and made adjustments to colors, fonts, padding, buttons, and other details.

## Assignment 6

**Explain the difference between asynchronous programming and synchronous programming.**

Asynchronous programming enables many processes to run simultaneously, allowing the program to move on to other tasks while awaiting the outcome of each task. In contrast, synchronous programming handles tasks sequentially, requiring each task to complete before moving on to the next one.

**In the implementation of JavaScript and AJAX, there is an implemented paradigm called the event-driven programming paradigm. Explain what this paradigm means and give one example of its implementation in this assignment.**

In event-driven programming, the program's actions depend on events that occur during its execution, rather than a fixed sequence of steps. Programmers define event handlers to control these events, and the code actively anticipates these particular events to occur. When an event takes place, the linked event handler is invoked, and the code promptly reacts, leading to a modification in the page's visual presentation. An example in this assignment is the implementation of the delete button. 

```
function deleteProduct(id) {
        fetch("delete-product-ajax/" + id, {
            method: "POST"
        }).then(refreshProducts);

        document.getElementById("form").reset();
        return false;
    }
```

**Explain the implementation of asynchronous programming in AJAX.**

Asynchronous programming allows a computer program to handle several jobs concurrently rather than sequentially. For the implementation, when something happens on a webpage, like someone clicking a button or submitting a form, JavaScript can take action. It can either make an XMLHttpRequest object or use the fetch API. This object is like a messenger that asks a web server for something. The web server gets this request, figures out what's needed, and then sends an answer back to the web browser. JavaScript reads this answer and deals with it according to the event that started everything. The actions it takes depend on the code that's been set up beforehand.

**In this semester, the implementation of AJAX is done using the Fetch API rather than the jQuery library. Compare the two technologies and write down your opinion which technology is better to use.**

The Fetch API is a new and modern tool that's already in a web browser. It's like a better and more standard way to ask the internet for things, even for AJAX stuff. Now, jQuery is an old favorite tool people have used for a long time but it's still user-friendly for beginners. I prefer the Fetch API more because it is up-to-date and great for new projects.

​​**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**

To implement the add product using AJAX, first in views.py, I imported  from django.views.decorators.csrf import csrf_exempt and made a function called get_product_json and add_product_ajax. Then, in urls.py, I imported the get_product_json and add_product_ajax and added both URL paths inside the urlspatterns list. In main.html, I replaced the table code with table id="product_table">/table>. I added a <script> tag block and a new method called getProducts(). In the <script> tag block, I also added a new method called refreshProducts(). The product data will be updated asynchronously using this function. Moreover, I created a new function inside the <script> tag block called addProduct() and set the addProduct() function as the onclick function of the model's  "Add Product" button. Next, I created a form modal by using bootstrap to add the products and also the button to show the modal. Lastly, I adjusted the add product button that uses ajax by replacing it with the previous add products button.


