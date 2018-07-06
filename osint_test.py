import subprocess

DATASPLOIT_PATH = '../datasploit/'


def extract_twitter_account_info(username):
    result = subprocess.run(['harpoon', 'twitter', '--user', username], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))


def extract_tweets(username):
    result = subprocess.run(['harpoon', 'twitter', '--tweets', username], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))


def extract_email_info(email):
    result = subprocess.run(['python', DATASPLOIT_PATH + 'emails/email_fullcontact.py', email],
                            stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))


def extract_username_info(username):
    result = subprocess.run(['python', DATASPLOIT_PATH + 'username/username_usernamesearch.py', username],
                            stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))


def run():

    print("Extracting twitter account info. Enter username please:")
    username = input()
    extract_twitter_account_info(username)

    print("Extracting tweets from user. Enter username please:")
    username = input()
    extract_tweets(username)

    print("Extracting email info. Enter email please:")
    email = input()
    extract_email_info(email)

    print("Extracting username info. Enter username please:")
    username = input()
    extract_username_info(username)


run()
