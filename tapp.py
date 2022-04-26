import requests
results = []
pagination = 1
url = 'http://127.0.0.1:8000/stu/total/?q=2022-04-23'
params = {'per_page': 2, 'page': pagination}
r = requests.get(url, params=params)
data = r.json()
for i in data:
    results.append(i)
while r.status_code == 200:
    pagination += 1
    params['page'] = pagination
    r = requests.get(url, params=params)
    data = r.json()
    for i in data:
        results.append(i)
    else:
        break
print(results)