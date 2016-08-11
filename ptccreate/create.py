import argparse
import time

from pgoapi import PGoApi

from ptcaccount import create_account

def main():
    parser = argparse.ArgumentParser(
        description='PTC Account Creator'
    )

    parser.add_argument('username', type=str, default=None, help='Username')
    parser.add_argument('password', type=str, default=None, help='Password')
    parser.add_argument('email', type=str, default=None, help='Email')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of accounts')
    parser.add_argument('-s', '--start', type=int, default=1, help='Account number to start at')

    args = parser.parse_args()

    start = args.start
    end = start + args.number
    print('Creating {} accounts ({} to {})...'.format(args.number, start, end))
    with open('accounts.txt', 'a+') as output:
        for number in range(start, end + 1):
            username = '{}{}'.format(args.username, number)
            password = args.password
            email = args.email.replace('@', '+{}@'.format(number))

            print('Creating {} ({})'.format(username, email))
            create_account(username, password, email)

            print('Accepting TOS')
            accept_tos(username, password)

            output.write('{}\n'.format(username))

    print('Done!')

def accept_tos(username, password, auth='ptc'):
    api = PGoApi()
    api.set_position(40.7127837, -74.005941, 0.0)
    api.login(auth, username, password)
    time.sleep(2)
    req = api.create_request()
    req.mark_tutorial_complete(tutorials_completed = 0, send_marketing_emails = False, send_push_notifications = False)
    response = req.call()
    print('Accepted Terms of Service for {}'.format(username))

if __name__ == '__main__':
    main()
