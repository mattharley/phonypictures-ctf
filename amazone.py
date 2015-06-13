import argparse
import logging

from flask import Flask, g, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amazone.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

user_list = [
    User('bigboss', 'bigboss@phonypictures.com', 'monkey'),
    User('nerdy', 'nerdy@phonypictures.com', 'l33t'),
    User('hero', 'hero@phonypictures.com', '8arH0SrVhZV7pApyRl'),
    User('shy', 'shy@phonypictures.com', 'david2012!'),

    User('complete_stranger', 'complete_stranger@yahoo.com', 'letmein'),
    User('slighty_better', 'slighty_better@gmail.com', 'qwerty!@#$%'),
    User('yet_another', 'yet_another@hotmail.com', 'newyearsday2015'),
    User('best_practice', 'best_practice@best_practice.com', '2zIcA48NyTLKBct0dp'),
]

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    price = db.Column(db.String(12))

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return '<Product %r>' % self.name

product_list = [
    Product('Widget', 'This is the best widget', "$5"),
    Product('Thingy', 'Thingies are cool. Is it thingies or thingy\'s?', "$12"),
    Product('Whizz Bang', 'Peeeowww. Off into the sky.', "$5"),
    Product('Adult Diapers', 'Peeeowww. Off into the sky.', "$5"),
]

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
    parser.add_argument("-s", "--syncdb", action='store_true', help="Creates the database tables and adds fixtures")

    return parser.parse_args()

def sync_db(db):
    db.drop_all()
    db.create_all()

    logger.info("Creating Users")
    for user in user_list:
        db.session.add(user)

    logger.info("Creating Products") 
    for product in product_list:
        db.session.add(product)

    db.session.commit()

if __name__ == '__main__':
    args = parse_arguments()
    setup_logging(args.verbose)

    if args.syncdb:
        sync_db(db)
    else:
        app.run(debug=args.debug)
