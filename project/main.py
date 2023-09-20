from flask import Flask, Blueprint, render_template, send_file, request
from flask_login import login_required, current_user
from datetime import datetime
from .models import User
from . import db
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return send_file('templates/index.html')
    # return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/medication_form', methods=['GET', 'POST'])
@login_required
def medication_form():
    if request.method == 'POST':
        medication1_name = request.form.get('medication1_name')
        medication2_name = request.form.get('medication2_name')
        medication1_time = request.form.get('medication1_time').split(',')
        medication2_time = request.form.get('medication2_time').split(',')
        gap_days1 = request.form.get('gap_days1')
        gap_days2 = request.form.get('gap_days2')
        todays_date = datetime.utcnow().isoformat()
        my_json = {
            "medication1": {
                "name": medication1_name,
                "times": medication1_time,
                "gap_days": gap_days1
            },
            "medication2": {
                "name": medication2_name,
                "times": medication2_time,
                "gap_days": gap_days2
            },
            "todays_date": todays_date
            }
        # my_json = {
        #     "medication1_name": medication1_name,
        #     "medication2_name": medication2_name,
        #     "medication1_time": medication1_time,
        #     "medication2_time": medication2_time,
        #     "gap_days1": gap_days1,
        #     "gap_days2": gap_days2,
        #     "todays_date": todays_date
        # }
        user = User.query.filter_by(id=current_user.id).first()
        user.device_data = json.dumps(my_json)
        db.session.commit()
        # Process the form data as needed
        # You can save it to the database, perform calculations, etc.
        return "Form submitted successfully!"  # You can replace this with a redirect or render_template
    return render_template('medication_form.html')

app = Flask(__name__)
app.register_blueprint(main)
app.static_folder = 'static'