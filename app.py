from crypt import methods
from flask import Flask, render_template

from controllers.owners_controller import owners_blueprint


app = Flask(__name__)

app.register_blueprint(owners_blueprint)


@app.route("/")
def log_in():
    return render_template('login.html')

@app.route("/home")
def home_view():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()