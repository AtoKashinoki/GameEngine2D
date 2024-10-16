"""
    AppEngine.InputSystem

This file contain InputSystem classes for developing apps.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from abc import abstractmethod
import msvcrt
from threading import Thread
from CodingTools2.Inheritance import InheritanceSkeleton


""" Input system skeleton """


class InputSystemSkeleton(InheritanceSkeleton):
    """ Input system base """

    @abstractmethod
    def __call__(self) -> None:
        """ input process """
        return

    @abstractmethod
    def __flame_end__ (self) -> None:
        """ flame end process """
        return

    ...


""" Console input system """


class Msvcrt(InputSystemSkeleton):
    """ Console input system """

    """ values """
    # constants

    # instances
    __pressed: set

    """ properties """
    @property
    def pressed(self) -> tuple: return tuple(self.__pressed)

    """ processes """
    def __init__(self):
        """ Initialize values """
        self.__pressed = set()
        return

    def check_press(self) -> None:
        if msvcrt.kbhit():
            self.__pressed.add(ord(msvcrt.getch()))
            ...
        return

    def __call__(self) -> None:
        Thread(target=self.check_press).start()
        return

    def __flame_end__(self) -> None:
        self.__pressed = set()
        return

    ...
