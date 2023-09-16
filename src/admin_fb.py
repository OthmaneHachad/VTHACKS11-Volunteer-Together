import firebase_admin
from firebase_admin import credentials, firestore, auth


# connecting to the firebase sdk
cred = credentials.Certificate("vt-hacks-11-volunteer-together-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

# Create a new user
user = auth.create_user(
    email='vthackstest@gmail.com',
    password='test123'
)
print('User created:', user.uid)


