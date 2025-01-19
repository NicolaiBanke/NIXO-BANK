import os
import dotenv

dotenv.load_dotenv()

USER_ID = os.getenv('USER_ID')
print(USER_ID)