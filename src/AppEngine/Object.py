"""
    AppEngine.Object

This file contain object classes for developing games.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


from abc import abstractmethod
from CodingTools2.Inheritance import InheritanceSkeleton


""" Skeleton """


class ObjectSkeleton(InheritanceSkeleton):
    """ Object class base """

    """ values """
    # texture
    __TEXTURE: any

    @property
    def texture(self) -> any: return self.__TEXTURE

    @classmethod
    def set_texture(cls, texture: any):
        """ set texture """
        cls.__TEXTURE = texture
        return

    ...
