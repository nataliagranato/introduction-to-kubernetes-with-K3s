from flask import Flask, request
from waitress import serve

import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    logger.info("/ invoked")
    return "Hello world"

if __name__ == '__main__':
    port = 5000
    serve(app, host='0.0.0.0', port=port)