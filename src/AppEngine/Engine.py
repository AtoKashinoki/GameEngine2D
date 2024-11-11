"""
    AppEngine.Engine

This file contain inheritance classes for developing apps.
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
from CodingTools2.Errors import Exit
from . import InputSystem
from . import RenderSystem


""" AppEngine Skeleton """


class AppEngineSkeleton(InheritanceSkeleton):
    """ AppEngine base """
    ...


""" FlameEngine """


class FlameEngine(AppEngineSkeleton):
    """ FlameEngine inheritance class """

    """ values """
    # constants
    Render: type = RenderSystem.RenderSystemSkeleton

    # instants
    class __System(DataClass):
        fps: int
        input_: InputSystem.InputSystemSkeleton = \
            InputSystem.Msvcrt
        render: RenderSystem.RenderSystemSkeleton = \
            RenderSystem.ConsoleRender
        ...

    class __FlameValues(DataClass):
        frame_count: int
        input: tuple
        render: bool
        ...

    __system: __System = None
    __frame: __FlameValues = None

    """ properties """
    @property
    def system(self) -> __System | None: return self.__system

    @property
    def input(self) -> tuple: return self.__frame.input
    @property
    def frame_count(self) -> int: return self.__frame.frame_count
    @property
    def render(self) -> bool: return self.__frame.render
    @render.setter
    def render(self, value: bool): self.__frame.render = value

    """ processes """
    def __init__(self, textures, _fps: int=10):
        """ Initialize engine settings """
        from .Texture import bind_textures
        bind_textures(textures(self))
        self.__system = self.__System()
        self.__system.fps = _fps
        return

    @abstractmethod
    def __update__(self) -> None | int:
        """ flame update function """
        return

    @abstractmethod
    def __render__(self, render_system) -> any:
        """ flame render function """
        return

    def check_pressed(self, _key_id: int) -> bool:
        """ Check and return to pressed keys """
        return _key_id in self.__frame.input

    def __loop_process(self) -> int:
        """ flame loop process function """

        """ initialize """
        self.__frame = self.__FlameValues()
        self.__frame.frame_count = 0
        self.__frame.render = False

        _fps = self.__system.fps
        _ofs = 1/_fps
        _input = self.__system.input_()
        _render = self.__system.render(self.__render__)

        _pre_flame: float = time()

        _system_key = None

        """ run """
        self.__frame.input = _input.input
        _render()

        done = False
        while not done:

            # input system
            _input()

            # create flame
            _now: float = time()
            if _now - _pre_flame < _ofs: continue
            _pre_flame = _now

            """ flame processes """
            self.__frame.input = _input.input

            # update
            try:
                _system_key = self.__update__()
                ...
            except Exit:
                done = True
                ...

            # rendering
            if self.__frame.render:
                _render()
                self.__frame.render = False
                ...

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
