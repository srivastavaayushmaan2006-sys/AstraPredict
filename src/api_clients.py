import time
import requests

from src.config import API_ENDPOINTS


def get_all_launch_data():
    """
    Download every launch available from the Launch Library API.
    Handles pagination and rate limits.
    """

    url = API_ENDPOINTS["launch_library"]
    all_launches = []

    while url:
        print(f"Downloading: {url}")

        retries = 5

        while retries > 0:
            try:
                response = requests.get(url, timeout=30)

                if response.status_code == 429:
                    print("Rate limit reached. Waiting 10 seconds...")
                    time.sleep(10)
                    retries -= 1
                    continue

                response.raise_for_status()

                data = response.json()

                all_launches.extend(data["results"])

                print(f"Downloaded {len(all_launches)} launches")

                url = data["next"]

                # Be nice to the API
                time.sleep(1)

                break

            except requests.exceptions.RequestException as e:
                retries -= 1

                if retries == 0:
                    raise Exception(f"Failed after multiple retries: {e}")

                print(f"Request failed: {e}")
                print("Retrying in 5 seconds...")
                time.sleep(5)

    return all_launches