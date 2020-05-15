import json
a='''{
    "result" : [
        {
            "request_id" : "1234_6789"
        }
    ],
    "log_id":149689853984104 
}'''

b=json.loads(a)
print(b['result'])

print('result' in b)
