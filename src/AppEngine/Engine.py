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
from time import time
from CodingTools2.Inheritance import (
    InheritanceSkeleton,
    DataClass,
)


""" AppEngine Skeleton """


class AppEngineSkeleton(InheritanceSkeleton):
    """ AppEngine base """
    ...


""" FlameEngine """


class FlameEngine(AppEngineSkeleton):
    """ FlameEngine inheritance class """

    """ values """
    # constants

    # instants
    class __System(DataClass):
        fps: int
        input_
        render
        ...


    """ properties """
    @property
    def system(self) -> type[__System]: return self.__System

    """ processes """
    def __init__(self, _fps: int=10):
        """ Initialize engine settings """
        self.__System.fps = _fps
        return

    @abstractmethod
    def __update__(self) -> None:
        """ flame update function """
        return

    @abstractmethod
    def __render__(self) -> None:
        """ flame render function """
        return

    def __loop_process(self) -> None:
        """ flame loop process function """

        """ initialize """
        _fps: int = self.__System.fps
        _ofs: float = 1/_fps
        _input = self.__System.input_()
        _render = self.__System.reder(self.__render__)
        _frame_count: int = 0

        _pre_flame: float = time()

        """ run """
        done = False
        while not done:

            # input system
            _input()

            # create flame
            _now: float = time()
            if _now - _pre_flame < _ofs: continue
            """ flame processes """

            # update
            self.__update__()

            # rendering
            _render()

            # count
            _frame_count += 1
            ...

        """ shutdown """

        return

    def exe(self) -> int:
        """ Run application """
        return 0
    ...
