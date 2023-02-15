import requests
import json

res = requests.get("http://127.0.0.1:8000/user/likes?user_id=999")

print(res.status_code, '\n')
json_req = json.dumps(res.json(), ensure_ascii=False, indent=4)
print(json_req)