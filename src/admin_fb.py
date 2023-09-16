import firebase_admin
from firebase_admin import credentials, firestore, auth


# connecting to the firebase sdk
cred = credentials.Certificate("vt-hacks-11-volunteer-together-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)


firebase_db = firestore.client()



"""
    Creates a new user
"""
def create_user(email, password):
    user = auth.create_user(
        email=email,
        password=password
    )

    return user

def check_user_exists(email):
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except auth.UserNotFoundError:
        return "doesn't exist"

def assign_user_type(uid, user_type):
    # gets the user data
    
    user_ref = firebase_db.collection("users").document(uid)
    # sets the user's "userType" to the user_type parameter inputted
    user_ref.set({
        "userType": user_type
    })

    return {
        "user" : uid,
        "updated_user_type": user_type
    }


def create_user_type():
    pass

def get_user_type():
    pass


#my_user = create_user("othmane3333hachad@gmail.com", "ttqagag")

#set_user_type = assign_user_type(my_user.uid, "volunteer")



#print(set_user_type["updated_user_type"])