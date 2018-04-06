from program_note import database
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

def create_user(u_name, f_name, l_name, email, p_word):
    user = database.User(uname = u_name, fname = f_name, lname = l_name, email = email, pword = generate_password_hash(p_word))
    if database.db.session.query(database.db.exists().where(database.User.uname == user.uname)).scalar():
        return False
    else:
        database.db.session.add(user)
        database.db.session.commit()
        return True
