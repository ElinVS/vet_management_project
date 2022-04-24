from crypt import methods
from flask import Flask, render_template

from controllers.owners_controller import owners_blueprint
from controllers.pets_controller import pets_blueprint


app = Flask(__name__)

app.register_blueprint(owners_blueprint)
app.register_blueprint(pets_blueprint)


@app.route("/")
def log_in():
    return render_template('login.html')

@app.route("/home")
def home_view():
    return render_template('base.html')

@app.route('/register')
def register_options():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()