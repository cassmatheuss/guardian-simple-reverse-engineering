import os
import random
from datetime import datetime

def generate_user_key():
    user = os.environ.get('USER') or os.environ.get('USERNAME')
    return user

def generate_int_key():
    start = 4
    end = 12000
    base_number = random.randrange(start, (end + 1), 4)
    return base_number

def generate_hour_key():
    hour = int(datetime.now().strftime("%H")) # 24h format
    return hour * 7

def validate_user_key(user_key):
    user_env = os.environ.get('USER') or os.environ.get('USERNAME')
    if user_key != user_env:
        return False
    return True

def validate_int_key(int_key):
    if int_key%4 != 0 or int_key > 12000:
        return False
    return True

def validate_hour_key(hour_key):
    try:
        hour_key = int(hour_key)
    except:
        return False
    hour = int(datetime.now().strftime("%H"))
    if hour_key != hour * 7:
        return False
    return True

def validate_key(key):
    try:
        user, int_key, hour_key = key.split('-')
        int_key = int(int_key)
    except:
        return False
 
    if not validate_user_key(user) or not validate_int_key(int_key) or not validate_hour_key(hour_key):
        return False
    return True

def main():
    user_key = input('Key: ')
    if validate_key(user_key):
        print('Valid Key ✅! Congratulations! 🎉')
    else:
        print('Invalid Key ❌! Try again! 🤔')

main()