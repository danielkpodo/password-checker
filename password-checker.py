import requests

url = "https://api.pwnedpasswords.com/range/" + 'CBFDA'

r = requests.get(url)
print(r)
