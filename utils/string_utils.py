import jdatetime


def to_persian(string):
    week_days = [
        ('Sa', 'شنبه'),
        ('Su', 'یک‌شنبه'),
        ('Mo', 'دو‌شنبه'),
        ('Tu', 'سه‌شنبه'),
        ('We', 'چهار‌شنبه'),
        ('Th', 'پنج‌شنبه'),
        ('Fr', 'جمعه'),
        ('saturday', 'شنبه'),
        ('sunday', 'یک‌شنبه'),
        ('monday', 'دو‌شنبه'),
        ('tuesday', 'سه‌شنبه'),
        ('wednesday', 'چهار‌شنبه'),
        ('thursday', 'پنج‌شنبه'),
        ('friday', 'جمعه')
    ]
    numbers = [
        ('0', '۰'),
        ('1', '۱'),
        ('2', '۲'),
        ('3', '۳'),
        ('4', '۴'),
        ('5', '۵'),
        ('6', '۶'),
        ('7', '۷'),
        ('8', '۸'),
        ('9', '۹'),
    ]
    ampm = [
        ('AM', 'قبل از ظهر'),
        ('PM', 'بعد از ظهر')
    ]
    for en, fa in week_days:
        string = string.replace(en, fa)
    for en, fa in numbers:
        string = string.replace(en, fa)
    for en, fa in ampm:
        string = string.replace(en, fa)
    return string


def convert_datetime_to_persian_date(datetime_value, with_time=False):
    persian_months = {
        1: 'فروردین',
        2: 'اردیبهشت',
        3: 'خرداد',
        4: 'تیر',
        5: 'مرداد',
        6: 'شهریور',
        7: 'مهر',
        8: 'آبان',
        9: 'آذر',
        10: 'دی',
        11: 'بهمن',
        12: 'اسفند'
    }
    jdt = jdatetime.GregorianToJalali(datetime_value.year, datetime_value.month, datetime_value.day)
    year = to_persian(str(jdt.jyear))
    month = persian_months.get(jdt.jmonth)
    day = to_persian(str(jdt.jday))
    if with_time:
        hour = to_persian(f'{datetime_value.hour:02d}')
        minute = to_persian(f'{datetime_value.minute:02d}')
        return f'{day} {month} {year} ساعت {hour}:{minute}'
    return f'{day} {month} {year}'
