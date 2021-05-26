# PizZaDelirium  

This project is based on Django channels. This is a real-time ***pizza order updating app*** using Django channels which updates the progress bar in real-time when an order status updates. Also implement real-time updates using WebSockets and Django channels.

### Starting  
1) Create a virtualenv and install the project requirements, which are listed in `requirements.txt`. The easiest way to do this is with `pip install -r requirements.txt` while your virtualenv is activated.  
2) In order to initialize the database for the project, go into the *PizZaDelirium* directory. Then run the following command `python manage.py migrate`. This will run all of the migrations for the project and initialize the database. 
3) To run the project type in python `manage.py runserver`  
4) If you want to create a superuser so you can play around with the admin, use the command `python manage.py createsuperuser` then go to `localhost:8000/admin`.

### Technologies:  
1) ***Front-End*** : HTML, CSS and JavaScript  
2) ***Back-End*** : Python Django  
3) ***Database*** : SQLite
4) ***Channels*** : Web Sockets

### Screenshots 
This is the Home page of the website.
![Home Page](https://github.com/shubhamjain31/PizZaDelirium/blob/main/Screenshots/image_one.png)

Here is the List of All Menus
![One_Page](https://github.com/shubhamjain31/PizZaDelirium/blob/main/Screenshots/image_two.png)

And this is the main thing which is updated by *Web Sockets*
![One_Page](https://github.com/shubhamjain31/PizZaDelirium/blob/main/Screenshots/image_four.png)
