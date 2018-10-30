from run import app
from models import UserModel
from datetime import datetime
new_user = UserModel(email = "admin@gmail.com",
                     password="password",
                     type_user=1,
                     year=datetime.utcnow().strftime('%d/%m/%Y')
                     )
try:
   new_user.save_to_db()
   print("created")
except Exception as e:
   print("error "+e)

