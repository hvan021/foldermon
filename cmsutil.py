import datetime
import settings

def strfunixtime(t):
    return datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")

def debug(obj):
    if settings.DEBUG:
        print obj


