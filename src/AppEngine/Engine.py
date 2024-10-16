"""
    AppEngine.Engine

This file contain inheritance classes for developing games.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from abc import abstractmethod
from CodingTools2.Inheritance import InheritanceSkeleton


""" AppEngine Skeleton """


class AppEngineSkeleton(InheritanceSkeleton):
    """ AppEngine base """
    ...


""" FlameEngine """
