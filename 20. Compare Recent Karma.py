'''
This script allows the user to enter:
 1) Number of reddit users
 2) Their usernames
 and then prints the karma of their latest reddit posts

'''
import json
import urllib3

urlrequester = urllib3.PoolManager()
header = {'User-agent':'bot 0.1'}


def check_karma(n):
    '''

    :param n: List of usernames
    :return:
    '''
    score = []
    for i in n:
        url = 'https://www.reddit.com/user/' +i+'.json'
        req = urlrequester.request('GET', url, headers=header)
        user_data = json.loads(req.data.decode('utf-8'))
        user_data = user_data['data']['children']
        if len(user_data) == 0:
            print('User "',i,'" doesn\'t havent  any posts.')
        else:
            score.append([user_data[0]['data']['score'], i])
            #print(user_data[0]['data']['score'],user_data[0]['data']['num_comments'])
    score = sorted(score, reverse = True)
    for i, x in score:
        print(f'The user "{x}" has {i} posts')
    print(f'Therefore the user with the highest Karma is: {score[0][1]}')





def enter_usernames():
    '''

    :return:
    '''
    users = []
    while True:
        users_count = input('Please enter the number of users you want to be compared: ')
        try:
            users_count = abs(int(users_count))
            break
        except:
            print('Please enter an integer')
    if users_count>10:
        users_count = 10
        print('Number of users set to 10, previous number was too large.')
    for i in range(users_count):
        while True:
            usernames = input('Please enter the username: ')
            url = 'https://www.reddit.com/user/' + usernames + '.json'
            req = urlrequester.request('GET', url, headers=header)
            if req.status != 404 and usernames not in users:
                break
            print('Username not valid or already used.')
        users.append(usernames)
    check_karma(users)


def main():
    repeat_program = True
    while repeat_program == True:
        enter_usernames()
        x = input('Repeat? Type "y" to repeat: ')
        if x.lower() != 'y':
            repeat_program = False
    print('Program ended, thank you!')

if __name__ == '__main__': main()