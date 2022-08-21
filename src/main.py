#import schedule
import time
#import tweepy
from random import sample

def get_keys():
    keys = open('../tokens/jedi_tokens.py', 'r').read().splitlines()
    
    api_key = keys[0]
    api_key_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    return api_key, api_key_secret, access_token, access_token_secret


def get_line_count(file) -> int:
    """
    Calculates the number of lines in file.
    """

    with open(file) as f:
        line_count = sum(1 for _ in f)
    return line_count


def enum_sayings(file):
    with open(file) as f:
        for (num, saying) in enumerate(f):
            return num, saying


def gen_order(line_count: int):
    indexes = [i for i in range(line_count)]
    order = sample(indexes, len(indexes))


def get_saying():
    pass


def job():
    print("I'm working...")

    schedule.every(2).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    c = get_keys()
    print (c)

    #file = "../data/CloneWarsSayings.txt"

    #line_count = get_line_count(file)
    #gen_order(line_count)
    #job(get_saying)
