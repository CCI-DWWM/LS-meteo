import requests

URL="http://127.0.0.1:8000/items2/555"

res = requests.get(URL)

print('status:' , res.status_code)