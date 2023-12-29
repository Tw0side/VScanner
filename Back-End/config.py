import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.environ.get('DATABASE_NAME')
db_user = os.environ.get('DATABASE_USER')
db_password = os.environ.get('DATABASE_PASSWORD')
db_host = os.environ.get('DATABASE_HOST')



admin_user = os.environ.get('ADMIN_USER')
admin_password = os.environ.get('ADMIN_PASSWORD')