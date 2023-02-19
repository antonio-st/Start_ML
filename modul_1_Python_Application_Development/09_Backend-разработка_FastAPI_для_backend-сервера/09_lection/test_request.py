import  requests
from loguru import logger

r = requests.get('http://127.0.0.1:8000/multiply/5/6')
logger.info(r.status_code)
logger.info(r.text)

r2 = requests.post(
    'http://localhost:8000/user/validate',
    json={'first_name': 'Anton', 'last_name': 'Bogdanov', 'age': 36}
)
logger.info(f'********** response 2')
logger.info(f'Status code: {r2.status_code}')
logger.info(f'Response: {r2.json()}')