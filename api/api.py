import flask
from . import logbookController
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '<h1>Logbook API is up</p>'

@app.route('/logbook', methods=['GET'])
def logbook():
    return logbookController.getLogbookGroupedByDate()

app.run()