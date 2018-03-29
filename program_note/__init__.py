from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

from program_note import views