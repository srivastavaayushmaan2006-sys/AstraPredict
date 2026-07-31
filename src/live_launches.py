import requests

from src.config import API_ENDPOINTS


def get_next_launch():
    """
    Fetch the next upcoming launch.
    """

    url = (
        API_ENDPOINTS["upcoming_launches"]
        + "?mode=detailed&limit=1"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    if not data["results"]:
        return None

    return data["results"][0]