import requests


def request_api_data(char):
    res = requests.get("https://api.pwnedpasswords.com/range/" + f"{char}")
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching data: {res.status_code}")
    return res


print(request_api_data("water"))
