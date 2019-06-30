from ui import UI
from dotenv import load_dotenv
import os


if __name__ == '__main__':
    load_dotenv()
    tg = UI(
        api_id=os.getenv('API_ID'),
        api_hash=os.getenv('API_HASH'),
        database_encryption_key='changeme1234',
    )
    tg.execute()
