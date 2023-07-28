# IDEAS : STUDENT MANAGEMENT SYSTEM WITH BOT INTEGRATION

[See dashboard](https://dashboard-ies-ipsabot.herokuapp.com/)
- --
## NOTE
- First Deploy the API and then the Dashboard/Web-App
- Before deploying make sure the API's base url is correct in `routes.py`
- - -
## RUN
After First/Fresh Deploy in Database, we need to run following query to initialise sqlalchemy

 ```
  from dashboard import models
  from dashboard import db
  db.create_all()
  db.session.commit()
  admin = models.Login('jd@admin', 'jd@admin', 'Jaydeep', 'Sahu', 'admin', 'image_url')
  db.session.add(admin)
  db.session.commit()
  
  admin = models.Login.query.all()
  print(admin)
  ```
Now to run if not deployed just run `wsgi.py`
```commandline
python wsgi.py
```

- --
## FEATURES

### ALERT SYSTEM
- send alerts to all
- send alerts to targeted user
- send alerts after filtering

### DATA DOWNLOAD UPLOAD [MAJOR-2]
- UPLOAD DATA VIA CSV FILE
- DOWNLOAD DB DATA INTO CSV FILE

### ADMIN PRIVILEGES
- CAN VIEW AND DELETE USERS DETAILS IN REALTIME [_done_]
- CAN SEE STUDENTS DETAILS - [_done_]
- CAN CRUD FACULTY DETAILS
- CAN CRUD NOTES
- CAN CRUD NOTICE BOARD [_MAJOR -2_]
- CAN TRIGGER SCHEDULERS MANUALLY 
- CAN WRITE ALERT MESSAGES AND SEND IT TO TARGETED USERS 
  - alert about feature updates
  - students who have not registered their branch or year
  - alert to update year after every session

### FACULTY PRIVILEGES
- CAN SEND ALERTS TO STUDENTS _via alert system_
- CAN PUT **ASSIGNMENT LINKS** or EVEN **UPLOAD ASSIGNMENT** TO THE DATABASE

  can be accessed  via **ASSIGNMENT** option in Chatbot.
  
  Doing this will send alerts to all the targest students via ALERT BOT
- CAN ADD NOTES
- CAN SEND ALERTS TO TARGETED STUDENTS

  - about assignment deadlines
  - lectures etc.

### DATA VISUALIZATION

- USER COUNT [_done_]
- STUDENT DATA [_done_]
  - BRANCH WISE ANALYSIS
  - YEAR WISE ANALYSIS
  - STUDENTS WITH BRANCH OR YEAR UNREGISTERED
- FACULTY DATA 
  - OPTION TO SELECT WHICH DATA TO VIEW
  - JOINING DATE / YEAR / EXPERIENCE
  - RESEARCH PAPERS / PUBLICATIONS
  - SPECIALIZATION [_done_]
  - SUBJECTS 
- NOTICE DATA [_MAJOR-2_]
  - NOTICE UPDATE FREQUENCY 
- NOTES
  - NUMBER OF SUBJECTS COVERED [_done_]

### ADMIN AUTHENTICATION SYSTEM [_done_]
- useful if we added FACULTY section as well in future

---

