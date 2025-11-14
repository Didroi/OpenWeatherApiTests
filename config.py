import logging
import os

from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("tests.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

'''
Использование логгов в тестах:
def test_read_geo_by_location_name(follow_the_testing_without_object, get_geo):
    logger.info("Starting test for Prague")
    
    get_geo.get_geo_by_location_name("Prague")
    logger.info(f"Response status: {get_geo.response_code}")
    logger.info(f"Response JSON: {get_geo.response_json}")
    
    assert get_geo.check_status_is_(200)
    logger.info("Test passed!")'''

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
