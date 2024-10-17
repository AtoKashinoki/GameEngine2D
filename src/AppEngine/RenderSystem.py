"""
    AppEngine.RenderSystem

This file contain RenderSystem classes for developing apps.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from os import system
from abc import abstractmethod
from CodingTools2.Inheritance import InheritanceSkeleton


""" Render system skeleton """


class RenderSystemSkeleton(InheritanceSkeleton):
    """ Render system skeleton """

    """ values """
    # constants

    # instances
    __render_func = None

    """ properties """
    @property
    def render_func(self): return self.__render_func

    """ processes """
    def __init__(self, __render__):
        """ Initialize render system """
        self.__render_func = __render__
        return

    @abstractmethod
    def __call__(self) -> None:
        """ render processes """
        return

    ...


""" Console render """


class ConsoleRender(RenderSystemSkeleton):
    """ Render system in console """

    """ values """
    # constants

    # instances
    __texts: str
    __new_texts: str

    """ properties """

    """ processes """
    def __init__(self, __render__):
        """ Initialize render system """
        super(ConsoleRender, self).__init__(__render__)
        self.__texts = ""
        self.__new_texts = ""
        return

    def __call__(self) -> None:
        system("cls")
        self.render_func(self)
        return

    ...
