# [Flask Material Kit MongoDB]()
This is Flask+Material Kit+ MongoDB starter template

## Requirements
Project depends on these exact versions of dependencies to work.
- Python 3.9
- Flask==2.0.2
- Flask-Login==0.5.0
- Flask-Minify==0.37
- flask-mongoengine==1.0.0
- Git
  
You need MongoDB setup also locally or using online Atlas Mongodb 

## MongoDB Setup <br>
### **Local Server Setup**<br>
**Step 1👉Local MongoDB database Setup**
follow Mongodb Installation requirements to install it in your system.

MongoDB Community Server Download Page [Here](https://www.mongodb.com/try/download/community).

Download  and Install the server

On successful MongoDB Community server download, add `MONGO_DB` and `MONGO_HOST` in the `.env` file.

**TIP 👉**  You can install MongoDB Compass to aid in querying the database using a GUI.

On successful installation create a database.


**Step 2 👉** Add environmental variables to your `.env` file

```
MONGO_DB=<mongo_database_name>
MONGO_HOST=localhost
```
### **Atlas MongoDB Setup**


**Step 1 👉Atlas MongoDB database Setup**
Login to your atlas account and create your database cluster according to your project needs but you can start with a free shared database  [Atlas MongoDB Account Here](https://cloud.mongodb.com)

<img width="100%"  src="./images/Screenshot%202022-11-30%20232705.png">

On successful creation of Atlas Cluster it will be visible as Cluster

<img width="100%"   src="./images/Screenshot 2022-11-30 232846.png">


Copy the connection string for connecting using python as the language

<img width="100%"   src="./images/Screenshot%202022-11-30%20233728.png">

**Step 2 👉** Add environmental variables to your `.env` file. Ensure to add database name to the connection string to avoid using the default `test` database 

```bash
DEBUG=True  #Turn to False in Production
MONGO_DB=<mongo_database_name>
MONGO_HOST=mongodb+srv://<username>:<password>@<your_cluster>.mongodb.net/<mongo_database_name>?retryWrites=true&w=majority
```

## Getting Started
 **Step 1** - Download the code from the Github repository (using `git` command). 

 It comes preinstalled in Unix and Mac.<br>
 If you dont have `git` installed on your system download and install it [Git Download Page](https://git-scm.com/downloads)



```bash
$ git clone https://github.com/app-generator/sample-flask-mongo.git
```


 **Step 2 -** - create virtual environment and install project dependencies

** 👉Linux/MacOS Users Setup**

Open Terminal and navigate to the repo
```bash
$ cd sample-flask-mongo
$ pip install virtualenv
$ python-virtualenv env
(env) $ pip install -r requirements.txt

```

**👉 Windows Users Setup**

Open Windows Powershell or CMD and navigate to the repo
```powershell
C:\> cd sample-flask-mongo
C:\> pip install virtualenv
C:\> python-virtualenv env
C:\> env\Scripts\activate
(env) C:\> pip install -r requiremenrs.txt

```

### Runing the Project
Having followed all the previous steps its time to run the application.<br>
To run the project all you need to do is run the command on your terminal or CMD

 ```bash
 $ python run.py
 ````

Now open the browser and navigate to [localhost:5000](http://localhost:8000) and the application should be up and running.

There you go! You have successfully run the application on your machine or server.





