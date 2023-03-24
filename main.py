import http.client
import json
import urllib.parse

def operate(data: str, result: int):
    dict = json.loads(data)
    if dict['operation'] == 'sum':
        return result + dict['number']
    if dict['operation'] == 'sub':
        return result - dict['number']
    if dict['operation'] == 'mul':
        return result * dict['number']
    if dict['operation'] == 'div':
        return result / dict['number']


conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/8', )
r2 = conn.getresponse().read().decode()
r2_json = json.loads(r2)
result = r2_json['number']
print(result)


conn.request('GET', '/number/?option=8', )
r1 = conn.getresponse().read().decode()

result = operate(r1, result)

print(result)

headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/number/', 'option=8', headers)
response = conn.getresponse().read().decode()
response_json = json.loads(response)
print(response_json['number'])
result = operate(response, result)
print(result)



headers = {'Content-type': 'application/json'}
body = json.dumps({'option': 8})
conn.request('PUT', '/number/', body, headers)
response = conn.getresponse().read().decode()
response_json = json.loads(response)
print(response_json['number'])
print(response)
result = operate(response, result)
print(result)



body = json.dumps({'option': 8})
conn.request('DELETE', '/number/', body)
response = conn.getresponse().read().decode()
response_json = json.loads(response)
print(response_json['number'])
print(response)
result = operate(response, result)
print(result)