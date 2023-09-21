from project import db, create_app, models

app = create_app()
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()
