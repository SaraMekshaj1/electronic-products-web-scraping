import time
import requests

def get_with_retry(session, url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
            return response

        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return None
