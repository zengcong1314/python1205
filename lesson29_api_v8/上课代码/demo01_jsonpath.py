""""""
from jsonpath import jsonpath
json_dict = {'id': 1472, 'token': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjE0NzIsImV4cCI6MTYxMjA5OTIyM30._C3kKzusl6S5Gx5Ut4sq8dY6qh8YV1XNjZcXcBrC7qXg8rpSVtHEjNdbCL719i-xJXb7TgYs-1n1Fog7Cyp7gA', 'leave_amount': 0.0}
# 匹配的结果放在列表,如果没有匹配,返回False
res = jsonpath(json_dict,'$.id')
print(res)