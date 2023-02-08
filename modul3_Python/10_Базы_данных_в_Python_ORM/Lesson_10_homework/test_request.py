import json

import requests

#num_in = int(input("Введите id: "))

# r = requests.get(f"http://127.0.0.1:8000/user/{num_in}")
# print(r.status_code)
# print(r.text)
#
# r = requests.get(f"http://127.0.0.1:8000/post/{num_in}")
# print(r.status_code)
# print(r.json())

r = requests.get(f"http://127.0.0.1:8000/post/recommendations/")
print(r.status_code, '\n')
# json_req = json.dumps(r.json(), ensure_ascii=False, indent=4)
# print(json_req)
print(r.text)
