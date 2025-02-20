
from CodingTools2.Definitions import Msvcrt, System
from AppEngine.Engine import FlameEngine
from AppEngine.Object import ObjectSkeleton
from AppEngine.Texture import TextureSkeleton
Key = Msvcrt.Key


class TObject(ObjectSkeleton):
    def __repr__(self):
        return ""
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
        self.pre_input = ()
        return

    def __update__(self) -> None | int:
        if not self.pre_input == self.input:
            self.render = True
            ...

        if self.check_pressed(Key.Special):
            if self.check_pressed(Key.Del):
                return System.EXIT
            if self.check_pressed(Key.Ins):
                return System.REBOOT
            ...

        self.pre_input = self.input
        return

    def __render__(self, render: FlameEngine.Render) -> any:
        print(self.input)
        print(self.test_object)
        return

    ...


if __name__ == '__main__':
    Test(MainTexture).exe()
    ...
