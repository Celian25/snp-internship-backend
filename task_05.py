import datetime


def date_in_future(integer: int) -> datetime.date:
    date = (
        datetime.datetime.now().replace(microsecond=0)
        + datetime.timedelta(days=integer)
        if type(integer) is int
        else datetime.datetime.now().replace(microsecond=0)
    )
    return date


print(date_in_future(5.1))
