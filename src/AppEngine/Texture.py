"""
    AppEngine.Texture

This file contain texture processes for developing apps.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from abc import abstractmethod
from typing import Callable
from CodingTools2.Inheritance import InheritanceSkeleton
from .Engine import AppEngineSkeleton
from .Object import ObjectSkeleton


""" Skeleton """


class TextureSkeleton(InheritanceSkeleton):
    """ Texture class base """

    """ values """
    # class
    textures: dict[type[ObjectSkeleton], Callable]

    # instance
    __app: ObjectSkeleton | AppEngineSkeleton
    __textures: dict[type[ObjectSkeleton], str | tuple | list | dict | set]

    """ properties """
    @property
    def app(self) -> ObjectSkeleton | AppEngineSkeleton:
        return self.__app

    """ processes """
    def __init__(self, app: ObjectSkeleton | AppEngineSkeleton):
        """ Initialize texture """
        self.__app = app
        self.__textures = {
            key: \
                value if isinstance(value, str) else
                value(self)
            for key, value in self.textures.items()
        }
        return

    def __get_textures__(self)\
            -> dict[type[ObjectSkeleton], str | tuple | list | dict | set]:
        """ Return texture instance """
        return self.__textures
    ...


""" Bind textures """


def bind_textures(textures: TextureSkeleton) -> None:
    """ Bind textures to objects """
    [
        key.set_texture(value)
        for key, value in textures.__get_textures__().items()
    ]
    return
