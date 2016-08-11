def format_accounts(filename='accounts.txt'):
    with open(filename, 'r') as input, open('formatted_{}.txt'.format(filename), 'w') as output:
        for line in input:
            username = line.split(':')[0].strip()
            output.write('-u {} '.format(username))
