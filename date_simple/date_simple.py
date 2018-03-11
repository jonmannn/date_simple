import datetime


def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    if date is None:
        return datetime.date.today()

    elif not isinstance(date, str):  # make sure the arg is the right type
        raise TypeError('must be string')

    elif isinstance(date, str):
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return date_obj


def get_date_string(date_object=None):
    """ takes an optional date object and returns a formatted string """
    if date_object is None:
        date_obj = datetime.date.today()
        return date_obj.strftime('%Y-%m-%d')

    elif not isinstance(date_object, datetime.date):
        raise TypeError('must be date object type')

    elif isinstance(date_object, datetime.date):
        date_object = date_object.strftime('%Y-%m-%d')
        date_obj = datetime.datetime.strptime(date_object, '%Y-%m-%d').date()
        return date_obj.strftime('%Y-%m-%d')
