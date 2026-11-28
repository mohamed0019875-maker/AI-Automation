import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Mohamed Ali",
    "email": "mohamed@example.com",
    "source": "webhook_test",
}

try:
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()

    data = response.json()
    print("Status code:", response.status_code)
    print("Echoed JSON:", data.get("json"))

except requests.RequestException as e:
    print("Request error:", e)
except ValueError as e:
    print("JSON parsing error:", e)