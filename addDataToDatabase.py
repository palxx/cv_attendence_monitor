import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("attendence_private_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://attendancerealtime-de900-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    '678900': {
        "name": "Rutuja Rajgude R",
        "major": "Bsc Chemistry",
        "starting_year": 2017,
        "total_attendance": 24,
        "year": 6,
        "standing":"D",
        "last_attendance_time":"2023-09-29 00:54:34"
    },
    '678901': {
        "name": "Rutuja Rajgude 2",
        "major": "Inner Engineering",
        "starting_year": 2023,
        "total_attendance": 1,
        "year": 6,
        "standing":"A",
        "last_attendance_time":"2023-09-29 00:54:34"
    },
    '761666': {
        "name": "Palavi Rajgude",
        "major": "Senior AI Dev",
        "starting_year": 2021,
        "total_attendance": 8,
        "year": 6,
        "standing":"A",
        "last_attendance_time":"2023-09-29 00:54:34"
    },
    '909000': {
        "name": "Mahendra Rajgude",
        "major": "Assistant GM",
        "starting_year": 2021,
        "total_attendance": 10,
        "year": 6,
        "standing":"A",
        "last_attendance_time":"2023-09-29 00:54:34"
    }
}

for key, value in data.items():
    print(key)
    print(value)
    ref.child(key).set(value)

