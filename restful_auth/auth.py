from flask_httpauth import HTTPBasicAuth
from flask import make_response, jsonify

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'test_user':
        return 'test_password'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)