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
from . import InputSystem


""" AppEngine Skeleton """


class AppEngineSkeleton(InheritanceSkeleton):
    """ AppEngine base """
    ...


""" FlameEngine """

class Test:
    def __init__(self, _render): ...
    def __call__(self, *args, **kwargs): ...


class FlameEngine(AppEngineSkeleton):
    """ FlameEngine inheritance class """

    """ values """
    # constants

    # instants
    class __System(DataClass):
        fps: int
        input_ = InputSystem.Msvcrt
        render = Test
        ...

    class __FlameValues(DataClass):
        frame_count: int
        pressed: tuple
        ...

    __system: __System = None
    __frame: __FlameValues = None

    """ properties """
    @property
    def system(self) -> __System | None: return self.__system

    @property
    def frame(self) -> __FlameValues | None: return self.__frame

    """ processes """
    def __init__(self, _fps: int=10):
        """ Initialize engine settings """
        self.__system = self.__System()
        self.__system.fps = _fps
        return

    @abstractmethod
    def __update__(self) -> None | int:
        """ flame update function """
        return

    @abstractmethod
    def __render__(self) -> None:
        """ flame render function """
        return

    def __loop_process(self) -> int:
        """ flame loop process function """

        """ initialize """
        self.__frame = self.__FlameValues()
        self.__frame.frame_count = 0

        _fps = self.__system.fps
        _ofs = 1/_fps
        _input = self.__system.input_()
        _render = self.__system.render(self.__render__)

        _pre_flame: float = time()

        _system_key = None

        """ run """
        done = False
        while not done:

            # input system
            _input()

            # create flame
            _now: float = time()
            if _now - _pre_flame < _ofs: continue
            _pre_flame = _now

            """ flame processes """
            self.__frame.pressed = _input.pressed

            # update
            _system_key = self.__update__()

            # rendering
            _render()

            # flame end processes
            _input.__flame_end__()
            self.__frame.frame_count += 1
            if _system_key is not None: done = True
            ...

        """ shutdown """

        return _system_key

    def exe(self) -> int:
        """ Run application """
        return self.__loop_process()
    ...
