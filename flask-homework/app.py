import json
from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

#                                    # """HOMEWORK FOR LESSON # 32 """
# @app.route('/hello')
# def hello_world():
#     app.logger.info("Blank function call")
#     return 'Hello World!'
#
#
# @app.route("/hello/json")
# def hello_world_json():
#     app.logger.info("Json function call")
#     return json.dumps({"hello": "world!"})
#
#
# @app.route('/hello/html')
# def hello_world_html():
#     app.logger.info("HTML function call")
#     return "<strong>Hello world!</strong>"
#
#                                    # """HOMEWORK FOR LESSON # 32  ENDS HERE"""

from views import *

if __name__ == '__main__':
    app.run()
