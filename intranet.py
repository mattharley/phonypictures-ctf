import argparse
import logging

from flask import Flask, flash, g, jsonify, redirect, render_template, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intrante.db'
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.debug = True
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    content = db.Column(db.String(1024))

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.title

post_list = [
    Post('New Game of Clones', 'bigboss', 
        'Anyone caught stealing the latest Game of Clones movie will be fired <strong>immediately</strong>! This is your first and only warning.'),
]

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    try:
        if request.method == 'POST':
            post = Post(
                request.form['title'],
                'hero',
                request.form['content']
            )
            db.session.add(post)
            db.session.commit()    
    except Exception as e:
        error = e.message
    posts = Post.query.all()
    return render_template('intranet.html', posts=posts, error=error)

def setup_logging(loglevel):
    logformat = "%(asctime)s: %(message)s"
    if loglevel:
        logging.basicConfig(level=logging.DEBUG,format=logformat)
    else:
        logging.basicConfig(level=logging.INFO,format=logformat)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Start a the flask server of the amazone project.')
    parser.add_argument('-d','--debug', action='store_true', help='Enable debugging')
    parser.add_argument("-v", "--verbose", action='store_true', help="Increase output verbosity")

    return parser.parse_args()

def sync_db(db):
    db.drop_all()
    db.create_all()

    logger.info("Creating Posts")
    for post in post_list:
        db.session.add(post)

    db.session.commit()

sync_db(db)

if __name__ == '__main__':
    args = parse_arguments()
    setup_logging(args.verbose)

    app.run(debug=args.debug)

