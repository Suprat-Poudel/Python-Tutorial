import pyrebase

firebaseConfig={"apiKey": "AIzaSyD8QDTrddis-y7KdoWZawqFlGr5Iz_M3q4",
  "authDomain": "myparkingsolutions.firebaseapp.com",
  "databaseURL": "https://myparkingsolutions-default-rtdb.firebaseio.com",
  "projectId": "myparkingsolutions",
  "storageBucket": "myparkingsolutions.appspot.com",
  "messagingSenderId": "410418407078",
  "appId": "1:410418407078:web:24094de0decc459606f667",
  "measurementId": "G-F74WN8L7B7"}

firebase= pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
#push
data={"user":"John", "age":"21"}
db.push(data)