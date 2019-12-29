import zhihuapi as api

with open('cookie') as f:
    api.cookie(f.read())

data = api.user('zhihuadmin').profile()
print(data)