import argparse
import logging

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('linkedout.html')

def setup_logging(loglevel):
    logformat = "%(asctime)s: %(message)s"
    if loglevel:
        logging.basicConfig(level=logging.DEBUG,format=logformat)
    else:
        logging.basicConfig(level=logging.INFO,format=logformat)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Start a the flask server of the linked out project.')
    parser.add_argument('-d','--debug', action='store_true', help='Enable debugging')
    parser.add_argument("-v", "--verbose", action='store_true', help="Increase output verbosity")

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    setup_logging(args.verbose)

    app.run(debug=args.debug)

