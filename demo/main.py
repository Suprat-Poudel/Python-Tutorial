from firebase import firebase

firebase = firebase.FirebaseApplication("https://myparkingsolutions-default-rtdb.firebaseio.com/", None)
result = firebase.get('/myparkingsolutions-default-rtdb/number/vehicle/vno', '')
print(result)