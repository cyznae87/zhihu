import zhihuapi as api
import csv

with open('cookie') as f:
    api.cookie(f.read())

data = api.user('zhihuadmin').profile()
print(data)

offset = 20
for i in range(3):
    followers = api.question(22078840).followers(offset=offset)
    offset += 20

#print(followers)

for follower in followers:
    try:
        uid = follower['url_token']
        name = follower['name']
        print(uid)
        with open('zhihuers.csv', mode='w') as zhihuers_file:
            employee_writer = csv.writer(zhihuers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow([uid, name])
        api.action.follow(uid)
    except:
        continue