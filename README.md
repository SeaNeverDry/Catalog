## Project
--------
This is 'The Item Catalog Application' Readme file - Version 1.0 (August-2018)
This application provides a variety list of items in terms of footwea, apparel, accessories and equipment that are used 
in different sports. This application also provides a user registration and authentication system using Google Sign In. 
Registered users have the ability to post, edit and delete their own items and only view other users' items. Non-registered 
users and users not logged in can only view the items, whether theirs or others.





## Getting Started

------------------

* First of all, a database_setup python file (database_setup_catalog.py) contains the database design:
the tables, their respective rows and names and relationships
* AllCategoriesItems.py file contains the data that will fill the tables created in the step above
* Running AllCategoriesItems.py in Git Bash creates the database file 'catalogapp'
* Running the application ('python application.py' in Git Bash) allows the user to access the application via 
'http://localhost:5000/' on any browser
* Users can log in using their google account. Authentification is done using Oauth.
* Users are then enabled to create, read, update and delete informations they have created once they are logged in
* Users not logged in can only view information present in the database.



### Prerequisites


------------------

*Runs on Windows and Mac Operating systems
*Can be run on top of the computer operating system using a virtual machine and vagrant



### Installing




---------------

Requires the installation of Git, Virtual Box, Vagrant and Python.


### Step By Step Instructions

------------------

a) Install Git, Virtual Box and Vagrant
(Please install the version for your operating system)
* Download Git from here: https://git-scm.com/downloads
* Download Virtual Box from here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
* Download Vagrant from here: https://www.vagrantup.com/downloads.html

b) Launch the Virtual Machine
*open Git bash
*change directory and cd into the vagrant folder
*launch the virtual machine using 'vagrant up'. When it is up and running type 'vagrant ssh' 
(or 'winpty vagrant ssh') to log your terminal into the virtual machine.
*Type 'cd /vagrant' to change directory to the /vagrant directory. This moves you to the 
shared folder between your computer and the virtual machine.

c) Setting Up and creating the database
*ensure you are cd into the vagrant directory
* the database set up can be found in the database_setup_catalog.py file.
The tables, rows, names and properties are found in this file.
* AllCategoriesItems.py files contains the initial data used to fill the above created tables.
* Running the command 'python AllCategoriesItems.py' will create the 'catalogapp' database file inside 
the current directory. The application (application.py) source data is the 'catalogapp' file;


d) Running the Python .py program
* In the virtual machine, type 'python application.py' and type enter to run the program
* Open your browser and access the web application via 'http://localhost:5000/'

e) Exploring / Viewing the data
* Users can use their google accounts sign in details to complete CRUD (Create, Read, Update, Delete) 
operations on the data;
* Any user not signed in can still explore the data using the 'view' option;
* Click on a given 'categorie'
* The given 'Categorie' page will open to show the items inside listed under each of the 4 genres: Footwear, 
Apparel, Equipment and Accessories.
* The user is able to 'view' the details for each item bu clicking on 'view';

f) Log in 
* Click on the 'Login' link at the top right corner of the page;
* Once done, user is directed to a Google sign in page. Click on the 'Sign In' button;
* A pop-up page will open asking the user to enter their google email and password
User to enter their google account email and password for authentication;
* If login details are correct, application will return a 'successful login' message and 
redirect the user to the application;

g) CRUD Operations
* Once logged in, the user is able not only to view the items under each 'categorie', but is also able to edit 
and delete the items; 


h) Logout
* Users are able to logout of the application by clicking on the 'logout' link that appears at the upper right side
of the screen after the user has been successfully logged in;




## Built With


--------------

* Python 2.7.14
* SQLAlchemy 
* Flask
* OAuth2



## Versioning


--------------
Version 1.0 




## Authors


----------

* Patricia Nzouonta 

* Contributors: None 




## License

----------

This project is licensed under the MIT License



## Acknowledgments

-------------------


* SQLAlchemy, 
