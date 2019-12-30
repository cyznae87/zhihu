import zhihuapi as api
import csv
import time
import random


def follow_and_record(follower_list):
    with open('zhihuers.csv', mode='a', newline='') as zhihuers_file:
        follower_writer = csv.writer(zhihuers_file)
        for follower in follower_list:
            time.sleep(round(random.uniform(0, 2), 2))
            uid = follower['url_token']
            name = follower['name']
            print(uid)
            try:
                api.action.follow(uid)
                follower_writer.writerow([uid, name, 'followed'])
            except:
                follower_writer.writerow([uid, name, 'error'])
                continue



with open('cookie') as f:
    api.cookie(f.read())

data = api.user('zhihuadmin').profile()
#print(data)


followers = api.question(22078840).followers()
offset = len(followers)

follow_and_record(followers)

while (len(followers)>0):
    time.sleep(round(random.uniform(10, 30), 3))
    followers = api.question(22078840).followers(offset)
    offset += len(followers)
    
    print(followers)

    follow_and_record(followers)



# for follower in followers:
#     try:
#         uid = follower['url_token']
#         name = follower['name']
#         print(uid)
#         with open('zhihuers.csv', mode='w') as zhihuers_file:
#             employee_writer = csv.writer(zhihuers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             employee_writer.writerow([uid, name])
#         api.action.follow(uid)
#     except:
#         continue
