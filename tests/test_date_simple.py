import pytest
import date_simple as ds
import datetime

# assert that if date_simple.get_date_object() is called with no arguments,
# it will return a date object for today.
def test_get_date():
    assert ds.get_date_object() == datetime.date.today()


# assert that if date_simple.get_date_object()
# is called with a properly formatted date string, it will return a date object for that date.
def test_date_simple_format():
    assert ds.get_date_object('2017-01-02') == datetime.date(2017, 1, 2)

# assert that if date_simple.get_date_string() is called with no arguments,
# it will return a date string for today.
def test_get_date_string_noarg():
    date_obj = datetime.date.today()
    assert ds.get_date_string(date_object=None) == date_obj.strftime('%Y-%m-%d')

# assert that if date_simple.get_date_string() is called with a date object,
# it will return the date string for that date
def test_get_date_string_dateobj():
    x = datetime.datetime.strptime('2018-02-26', '%Y-%m-%d')
    assert ds.get_date_string(date_object=x) == '2018-02-26'


# assert that if date_simple.get_date_object() is called with an improperly formatted date,
# it will raise a ValueError exception.
def test_get_date_object_format():
    with pytest.raises(ValueError):
        ds.get_date_object('43-13-16')

# assert that if date_simple.get_date_object() is called with an object that is not type str,
#  it will raise a TypeError exception.
def test_get_date_object_passed():
    with pytest.raises(TypeError):
        ds.get_date_object(4)

# assert that if date_simple.get_date_string() is called with an object that is not type datetime.date,
# it will raise a TypeError exception.
def test_get_date_string_type():
    with pytest.raises(TypeError):
        ds.get_date_string('hi')