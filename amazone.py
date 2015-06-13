import argparse
import logging

from flask import Flask, flash, g, jsonify, redirect, render_template, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amazone.db'
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.debug = True
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
    Product('Adult Diapers', 'ON SPECIAL - for those that can\'t leave their computer', "$25"),
]

@app.route('/')
def show_products():
    products_list = Product.query.all()
    return render_template('products.html', products=products_list)

@app.route('/account')
def account():
    error = None
    username = request.args.get('username')
    if username:
        users = db.engine.execute("select username, password, email from user where username='{}'".format(username)).fetchall()
        if users and session['username'] in [user.username for user in users]:
            pass
        else:
            error = 'You can only view details for your own username!'
    else:
        users = None
    return render_template('account.html', users=users, error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']:
            users = User.query.filter_by(
                    username=request.form['username']
                )
            if users:
                if request.form['password'] and request.form['password'] == users.first().password:
                    session['logged_in'] = True
                    session['username'] = request.form['username']
                    flash('You were logged in')
                    return redirect(url_for('show_products'))
                error = 'Invalid password'
            else:
                error = 'Invalid username'
        else: 
            error = 'Invalid username'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('show_products'))

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

sync_db(db)

if __name__ == '__main__':
    app.run(debug=True)

