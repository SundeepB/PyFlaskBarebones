import json
import time

from flask import request
from flask import current_app

from . import barebones

@barebones.route('/hello/<name>', methods=['GET'])
def hello(name):
    """
    GET request with parameter capture from the URL
    """
    logger = current_app.logger
    logger.info('Received hello from ' + name)
    return 'hello ' + name, 200

@barebones.route('/echo', methods=['POST'])
def echo():
    """
    POST request with form parameters
    """
    result = {}
    for key in request.form:
        result[key] = request.form[key]
    result['size'] = len(request.form)

    logger = current_app.logger
    logger.info('Received echo request with ' + str(len(request.form)) + ' parameters')

    return json.dumps(result, indent = 4, ensure_ascii = False), 200

@barebones.route('/accept_json', methods=['POST'])
def accept_json():
    """
    POST request that throws 400 bad input if the payload is not JSON
    When JSON data is posted, it returns the original with some more attributes added
    """
    if not request.is_json:
        return 'Expected json body', 400
    json_data = request.get_json()

    logger = current_app.logger
    logger.info('Received json data: ' + str(json_data))

    result = {}
    result['count'] = len(json_data)
    result['timestamp'] = time.time()
    result['original'] = json_data

    return json.dumps(result, indent = 4, ensure_ascii = False), 200
