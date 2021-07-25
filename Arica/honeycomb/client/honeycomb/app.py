"""
honeycomb main manager
Written by Kenan- yell at him if this breaks
"""
from flask import Flask
import logging
import time
from flask import Flask
import sys
from flask_restful import Resource, Api

sys.path.append("./routes/")

from upgrade_peripheral import upgrade

# All output for this service will be piped to journalctl under the honeycomb service
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
api = Api(app)
app.register_blueprint(upgrade)


@app.route("/")
def hello_world(): 
    return { "message" : "hello" }


if __name__ == "__main__":
    app.run(debug=True)

