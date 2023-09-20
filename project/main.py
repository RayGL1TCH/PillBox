from flask import Flask, Blueprint, render_template, send_file
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_file('templates/index.html')
    # return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


app = Flask(__name__)
app.register_blueprint(main)
app.static_folder = 'static'