"""Send a GET request to httpbin.org and print key fields from the response.

Requires the `requests` library:  pip install requests
"""

import sys

try:
    import requests
except ImportError:
    print("Error: the 'requests' library is not installed.")
    print("Install it with: pip install requests")
    sys.exit(1)

URL = "https://httpbin.org/get"
TIMEOUT = 10  # seconds


def fetch(url):
    """Send a GET request and return the response object."""
    try:
        return requests.get(url, timeout=TIMEOUT)
    except requests.exceptions.Timeout:
        print(f"Error: the request timed out after {TIMEOUT} seconds. Try again later.")
    except requests.exceptions.ConnectionError:
        print("Error: could not connect. Check your internet connection.")
    except requests.exceptions.RequestException as error:
        print(f"Error: the request failed: {error}")
    return None


def parse_json(response):
    """Parse the response body as JSON. Returns None if it is not valid JSON."""
    try:
        return response.json()
    except ValueError as error:
        print(f"Error: the response was not valid JSON ({error}).")
        return None


def print_key_fields(data):
    """Print the url, origin, and User-Agent from the parsed JSON."""
    if not isinstance(data, dict):
        print("Error: the JSON response was not in the expected format.")
        return

    print(f"URL:        {data.get('url', 'N/A')}")
    print(f"Origin:     {data.get('origin', 'N/A')}")
    print(f"User-Agent: {data.get('headers', {}).get('User-Agent', 'N/A')}")


def main():
    print(f"Sending GET request to {URL} ...")

    response = fetch(URL)
    if response is None:
        return

    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        print(f"Error: expected status 200 but got {response.status_code}. Stopping here.")
        return

    data = parse_json(response)
    if data is None:
        return

    print_key_fields(data)


if __name__ == "__main__":
    main()