import argparse
import logging

from flask import Flask, flash, g, jsonify, redirect, render_template, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///capture.db'
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.debug = True
db = SQLAlchemy(app)

class Credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Credentials %r>' % self.username

cred_list = [
    Credentials('some_sucker','p4ssw0rd'),
    Credentials('another_sucker','dogsNameCatsName42'),
]

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    try:
        if request.method == 'POST':
            cred = Credentials(
                request.form['username'],
                request.form['password'],
            )
            db.session.add(cred)
            db.session.commit()    
    except Exception as e:
        error = e.message
    creds = Credentials.query.all()
    return render_template('capture.html', creds=creds, error=error)

def setup_logging(loglevel):
    logformat = "%(asctime)s: %(message)s"
    if loglevel:
        logging.basicConfig(level=logging.DEBUG,format=logformat)
    else:
        logging.basicConfig(level=logging.INFO,format=logformat)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Start a the flask server of the capture project.')
    parser.add_argument('-d','--debug', action='store_true', help='Enable debugging')
    parser.add_argument("-v", "--verbose", action='store_true', help="Increase output verbosity")

    return parser.parse_args()

def sync_db(db):
    db.drop_all()
    db.create_all()

    logger.info("Creating Credentials")
    for cred in cred_list:
        db.session.add(cred)

    db.session.commit()

sync_db(db)

if __name__ == '__main__':
    args = parse_arguments()
    setup_logging(args.verbose)

    app.run(debug=args.debug)

