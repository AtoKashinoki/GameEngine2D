
from CodingTools2.Definitions import Msvcrt, System
from AppEngine.Engine import FlameEngine
from AppEngine.Object import ObjectSkeleton
from AppEngine.Texture import TextureSkeleton
Key = Msvcrt.Key


class TObject(ObjectSkeleton):
    ...


class MainTexture(TextureSkeleton):
    """ texture generator """

    """ textures """
    textures = {
        TObject: "test!ok"
    }
    ...


class Test(FlameEngine):

    def __init__(self, texture):
        super(Test, self).__init__(texture)
        self.test_object = TObject()
        return

    def __update__(self) -> None | int:
        if self.check_pressed(Key.Space):
            if self.check_pressed(Key.e):
                return System.EXIT
            if self.check_pressed(Key.r):
                return System.REBOOT
        return

    def __render__(self, render: FlameEngine.Render) -> any:
        print(self.frame.pressed)
        print(self.test_object)
        return

    ...


if __name__ == '__main__':
    Test(MainTexture).exe()
    ...
