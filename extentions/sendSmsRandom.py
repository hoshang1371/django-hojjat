from random import randint
import time

# from post_information.views import code


# import post_information
# co = post_information.views
# from ..post_information.views import code
import sys
import os
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# print('current=',current)
# print('parent=',(parent+'\post_information'))
# sys.path.append(parent+'\post_information')

# from extentions.globalValue import code
from extentions import globalValue


from ippanel import Client
from ippanel import HTTPError, Error, ResponseCode


from django.http import HttpResponse
import datetime
import logging

from decouple import config


logger = logging.getLogger(__name__)

# you api key that generated from panel
api_key = "tVnkn0VqCuVvolYqStkCNljo3AZef8gVmZgKq8FeRK0=	"
# api_key = config('API_KEY')
# pattern_code = config('PATTERN_CODE')

# create client instance
sms = Client(api_key)

credit = sms.get_credit()
# stop_threads_sendSmsVarify = False

def random_with_N_digits(n):
    # range_start = 10**(n-1)
    # range_end = (10**n)-1
    # return randint(range_start, range_end)
    return ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])

def sendSms(code,mobilenumber):
    try:
        # message_id = sms.send("9810001", ["98912xxxxx"], "ippanel is awesome")
        pattern_values = {
            "verificationCode": code,
        }

        message_id = sms.send_pattern(
            "r1eppoe3ilfudqx",    # pattern code
            # pattern_code,    # pattern code
            "3000505",      # originator
            mobilenumber,  # recipient
            pattern_values,  # pattern values
        )
    except Error as e: # ippanel sms error
        print(f"Error handled => code: {e.code}, message: {e.message}")
        if e.code == ResponseCode.ErrUnprocessableEntity.value:
            for field in e.message:
                print(f"Field: {field} , Errors: {e.message[field]}")
    except HTTPError as e: # http error like network error, not found, ...
        print(f"Error handled => code: {e}")

def sendSmsForVarifyAddress(user,stop):
    # a=0
    # a += 1
    # print(stop_threads_sendSmsVarify)
    # sendSms('12345','09367262334')
    # global code
    print('sendSmsForVarifyAddressCode=',globalValue.code)
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')

    # todo : مقدار 120 صحیح است
    for a in range(0,120):
    # for a in range(0,10):
        time.sleep(1)
        # print(stop()) 
        if stop():
            # globalValue.code = ''
            # print('sendSmsForVarifyAddressCodeEnd=',globalValue.code)
            break
        print(a)


    # global code
    # print('sendSmsForVarifyAddress',code)
    # print(stop_threads_sendSmsVarify)
    # print('a=',a)
    # if a==120:
    #     print(user)


