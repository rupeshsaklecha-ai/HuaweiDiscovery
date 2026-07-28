from datetime import datetime


def line(length=70):

    print("=" * length)


def title(text):

    line()

    print(text)

    line()


def timestamp():

    return datetime.now().strftime("%d-%b-%Y %H:%M:%S")


def scale_power(value):

    try:

        return float(value) / 100

    except:

        return None


def safe_int(value):

    try:

        return int(value)

    except:

        return None


def safe_float(value):

    try:

        return float(value)

    except:

        return None
