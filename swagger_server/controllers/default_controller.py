import connexion
import six

from swagger_server.models.lecture import Lecture  # noqa: E501
from swagger_server import util


def uni_get_day_lectures(offset):  # noqa: E501
    """Get the Lectures of the Current(+offset) Day

    This endpoint will return the luctures of the current day(+offset).  # noqa: E501

    :param offset: Day offset from current day
    :type offset: float

    :rtype: List[Lecture]
    """
    return 'do some magic!'


def uni_get_days_around_lectures(offset, range):  # noqa: E501
    """Get Lecture-Days around today(+offset) in range of range

    This endpoint will return the current day of lectures and the days that are in range around today. This will be in an array of arrays like a  Week.  # noqa: E501

    :param offset: day offset from current day
    :type offset: float
    :param range: The range of days returned
    :type range: float

    :rtype: List[List[Lecture]]
    """
    return 'do some magic!'


def uni_get_week_lectures(offset):  # noqa: E501
    """Get the Lectures of the Current Week(+offset)

    This endpoint will return the luctures of the current week.  # noqa: E501

    :param offset: Week offset from current day
    :type offset: float

    :rtype: List[List[Lecture]]
    """
    return 'do some magic!'
