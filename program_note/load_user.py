from program_note import database, login_manager, login_user
from werkzeug.security import check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return database.User.query.get(int(user_id))

# checks if user is in database
# if yes, then verifies password and returns a list with the first item being a boolean. If the boolean is true then the User object is returned as the second item.
def login(uName, passW):
    user = database.User.query.filter_by(uname = uName).first()
    if user:
        if check_password_hash(user.pword, passW):
            login_user(user)
            return [True, user]
        else:
            return [False]
    else:
        return [False]