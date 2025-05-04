import datetime


def date_in_future(integer: int) -> str:
    date = (
        datetime.datetime.now().replace(microsecond=0)
        + datetime.timedelta(days=integer)
        if type(integer) is int
        else datetime.datetime.now().replace(microsecond=0)
    )
    return date.strftime("%d-%m-%Y %H:%M:%S")
