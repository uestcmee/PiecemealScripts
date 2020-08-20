import requests

res=requests.get('https://api.github.com/users/uestcmee/repos')

print(res)