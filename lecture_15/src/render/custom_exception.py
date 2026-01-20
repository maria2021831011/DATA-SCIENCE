class InvalidURLException(Exception):
    """Custom exception for invalid YouTube URLs."""
    
    def __init__(self, url: str):
        self.url = url
        self.message = f"The provided URL '{self.url}' is not a valid YouTube URL."
        super().__init__(self.message)