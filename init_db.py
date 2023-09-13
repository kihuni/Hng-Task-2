import os
from app import app, db
from app.models import Person

# Print the absolute path
print("Expected path for site.db:", os.path.abspath("site.db"))

with app.app_context():
    db.create_all()
    table = Person.__table__
    print(table)
    print("Database tables created!")
