import os
import sys
from flask import jsonify, make_response
from modules.logger import logger
from modules.app import app

ROOT_PATH = os.path.dirname(os.path.relpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

# create a logger object to log the info and debug
LOG = logger.get_root_logger(os.environ.get('ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'output.log'))

# Port variable to run application
PORT = os.environ.get('PORT')


@app.errorhandler(404)
def not_found(err):
    LOG.error(err)
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/')
def index():
    return f"Welcome to our car park service"


if __name__ == '__main__':
    LOG.info('running application with environment: %s', os.environ.get('ENV'))
    app.config['debug'] = os.environ.get('ENV') == 'development'
    app.run(host='0.0.0.0', port=int(PORT))
