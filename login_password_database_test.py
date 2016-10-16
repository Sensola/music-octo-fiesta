from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import sqlite3 as lite
import bcrypt


app = Flask(__name__)

current_user = None


from functools import wraps
from flask import request, Response


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated



class DatabaseHandler:
    # Todo: make to only handle db, and separate encryption maybe and stuffa
    def __init__(self):
        self.con = lite.connect('test.db')

    def create_db(self):
        with self.con:
            self.con.cursor().execute("DROP TABLE IF EXISTS Users")
            self.con.cursor().execute(" CREATE TABLE Users(Username TEXT PRIMARY KEY, Password TEXT)")

    def add_user(self, username, encrypted):
        with self.con:
            cur = self.con.cursor()
            cur.execute("INSERT INTO Users(Username, Password) VALUES('{}','{}')".format(username, encrypted))

    def get_hash(self, username):
        with self.con:
            cur = self.con.cursor()

            # get row including username and password hash from database
            cur.execute("SELECT * FROM Users where username IS '{}'".format(username))
            matchbox = cur.fetchall()

            # Check that there is such user.
            if matchbox:
                return matchbox[0][1]
            else:
                return False

    def save(self):
        self.con.commit()
        self.con.close()

    def update_user(self):
        pass


def encrypt(password):
    encrypted = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    return encrypted


def mathces(password, hashcode):
    return bcrypt.checkpw(password.encode("utf-8"), hashcode.encode("utf-8"))


@app.route('/u/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = DatabaseHandler()
        username = request.form["user"]
        password = request.form["password"]
        password_hash = db.get_hash(username)
        if not password_hash:
            error = "Username doesnt exist"

        elif mathces(password, password_hash):
            return redirect("/u/{}".format(username), code=302)

        else:
            error = "Wrong passord"
    else:
        username = False
        error = False
    return render_template("login.html", username=username, error=error)


if __name__ == '__main__':
    app.debug = True
    app.run()  # host='0.0.0.0') # Make open to network
