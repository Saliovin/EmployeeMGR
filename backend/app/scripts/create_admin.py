import os
import bcrypt
from app.database import get_db
from app.models.user import User


db_session = next(get_db())

admin_username = os.getenv("ADMIN_USERNAME", "admin")
admin_password = os.getenv("ADMIN_PASSWORD", "password")
hashed_password = bcrypt.hashpw(admin_password.encode(), bcrypt.gensalt())

if __name__ == "__main__":
    db_user = db_session.query(User).filter(User.username == admin_username).first()
    if not db_user:
        admin = User(username=admin_username, hashed_password=hashed_password)
        db_session.add(admin)
        db_session.commit()
