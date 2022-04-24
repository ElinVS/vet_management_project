from flask import Flask, render_template

from controllers.owners_controller import owners_blueprint


app = Flask(__name__)

app.register_blueprint(owners_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()