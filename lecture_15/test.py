#from render.logger import logger
#logger.info("Test logger initialized")
from render.custom_exception import InvalidURLException
def test_invalid_url_exception():
    invalid_url = "https://www.invalidurl.com/watch?v=dQw4w9WgXcQ"
    try:
        raise InvalidURLException(invalid_url)
    except InvalidURLException as e:
        assert str(e) == f"The provided URL '{invalid_url}' is not a valid YouTube URL."