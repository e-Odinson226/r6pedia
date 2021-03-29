from . import jalali
from django.utils import timezone


def jalaliazer(time):

    time = timezone.localtime(time)

    gregorian_date =  "{},{},{}".format(time.year, time.month, time.day)
    jalali_date = list(jalali.Gregorian(gregorian_date).persian_tuple())

    months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

    for index, month in enumerate(months):
        if jalali_date[1] == index + 1:
            jalali_date[1] = month

    output = "{},{},{} | {}:{}".format(jalali_date[0], jalali_date[1], jalali_date[2], time.hour, time.minute)
    
    return output
