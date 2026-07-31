import requests

from src.config import API_ENDPOINTS


def get_launch_library_data():
    """
    Download launch data from Launch Library 2.
    """
    url = API_ENDPOINTS["launch_library"]

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.json()