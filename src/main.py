#import schedule
#jimport time
import tweepy
from random import sample


def get_keys():
    keys = open("../tokens/jedi_tokens.py", "r").read().splitlines()

    return keys


def authenticate(api_key, api_key_secret, access_token, access_token_secret):
    authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    tweepy.API(authenticator, wait_on_rate_limit=True)
    return


'''
def get_line_count(file) -> int:
    """
    Calculates the number of lines in file.
    """

    with open(file) as f:
        line_count = sum(1 for _ in f)
    return line_count

'''

def enum_sayings(file):
    with open(file) as f:
        for (num, saying) in enumerate(f):
            return num, saying

def gen_random_num():
     indexes = [i for i in range(line_count)]
     return sample(indexes)


def gen_order(line_count: int):
    indexes = [i for i in range(line_count)]
    order = sample(indexes, len(indexes))


def get_todays_saying():
   return sample()


def get_saying():
    pass    

'''
def job():
    print("I'm working...")

    schedule.every(2).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)
'''




if __name__ == "__main__":
    file = "../data/CloneWarsSayings.txt"
    keys = get_keys()

    api_key = keys[0]
    api_key_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    try:
        authenticate(api_key, api_key_secret, access_token, access_token_secret)
        print("Authentication compete")
    except:
        print("There is an error in authentication")

    sayings = enum_sayings(file)    
    print(sayings)




    index = get_todays_saying()
    
    # job(get_saying)
