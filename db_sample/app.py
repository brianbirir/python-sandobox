from flask import Flask
from models import db
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://python_test:toor@localhost:5432/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize db
db.init_app(app)

# migrate initialization
migrate = Migrate(app, db)

@app.route('/')
def main():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
