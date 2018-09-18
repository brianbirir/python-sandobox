from flask import Flask, request, make_response, abort, jsonify, url_for
from flask_migrate import Migrate
from models import User, DB

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://python_test:toor@localhost:5432/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize db
DB.init_app(app)

# migrate initialization
migrate = Migrate(app, DB)


# register user
@app.route('/api/v1.0/user/register', methods=['POST'])
def new_user():

    if not request.json:
        abort(400)

    req_data = request.get_json()

    username = req_data['username']
    password = req_data['password']

    if username is None or password is None:
        abort(400) # missing arguments

    if User.query.filter_by(username=username).first() is not None:
        abort(400) # existing user

    user = User(username=username)
    user.hash_password(password)
    DB.session.add(user)
    DB.session.commit()
    return (jsonify({ 'username': user.username }), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})

    # return '''The username value is: {}
    # The password value is: {}'''.format(username, password)


# get a user
@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


# not found error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Resource not found'}),404)


@app.errorhandler(400)
def not_allowed(error):
    return make_response(jsonify({'error':'Method is not allowed'}),400)


if __name__ == '__main__':
    app.run(debug=True)