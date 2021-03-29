from . import jalali
from django.utils import timezone

def to_persian_numbers(numb_str):
    index ={
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
        "0":"۰",
    }
    for eng, per in index.items():
        numb_str = numb_str.replace(eng,per)
    return numb_str

def jalaliazer(time):

    time = timezone.localtime(time)

    gregorian_date =  "{},{},{}".format(time.year, time.month, time.day)
    jalali_date = list(jalali.Gregorian(gregorian_date).persian_tuple())

    months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

    for index, month in enumerate(months):
        if jalali_date[1] == index + 1:
            jalali_date[1] = month

    output = "{},{},{} | {}:{}".format(jalali_date[0], jalali_date[1], jalali_date[2], time.hour, time.minute)
    
    return to_persian_numbers(output)
