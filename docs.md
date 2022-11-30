# [Flask Material Kit MongoDB]()
This is Flask+Material Kit+ MongoDB starter template

## Requirements
Project depends on these exact versions of dependencies to work.
- Flask==2.0.2
- Flask-Login==0.5.0
- Flask-Minify==0.37
- flask-mongoengine==1.0.0
  
You need MongoDB setup also locally or using online Atlas Mongodb 

## MongoDB Setup <br>
### **Local Server Setup**<br>
**Step 1👉Local MongoDB database Setup**
follow Mongodb Installation requirements to install it in your system. 

**TIP 👉**  You can install MongoDB Compass to aid in querying the database using a GUI.

On successful installation create a database.


**Step 2 👉** Add environmental variables to your `.env` file

```
MONGO_DB=<mongo_database_name>
```
### **Atlas MongoDB Setup**


**Step 1 👉Atlas MongoDB database Setup**
Login to your atlas account and create your database cluster

**Step 2 👉** Add environmental variables to your `.env` file

```
MONGO_DB=<mongo_database_name>
MONGO_HOST=<MongoDB_Cluster_URL>
```

## Getting Started
 **Step 1** - Download the code from the GH repository (using `GIT`) 

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
To run the project all you need to do is run the command

 ```bash
 $ python run.py
 ````

Now open the browser and navigate to [localhost:5000](http://localhost:8000) and the application should be up and running.





