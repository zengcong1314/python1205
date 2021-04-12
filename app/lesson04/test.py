

str = "Test Engneer"
a = str[::-1]
print(a)

for i in range (1,10000):
    sum = 0
    sum = sum + i**10
print(sum)

import requests
res = requests.get("http://httpbin.org/json")
res_json = res.json()
res_title = res_json['slideshow']['slides'][0]['title']
slides = res_json['slideshow']['slides']
print("title:{},slides count:{}".format(res_title,len(slides)))

import random
import hashlib
value=random.choice(dict[key])
hashlib.md5(value)

[6,30,32,7,9]