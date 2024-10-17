
from CodingTools2.Definitions import Msvcrt, System
from AppEngine.Engine import FlameEngine
Key = Msvcrt.Key

class Test(FlameEngine):

    def __update__(self) -> None | int:
        if self.check_pressed(Key.Space):
            if self.check_pressed(Key.e):
                return System.EXIT
            if self.check_pressed(Key.r):
                return System.REBOOT
        return

    def __render__(self, render: FlameEngine.Render) -> any:
        print(self.frame.pressed)
        return

    ...


if __name__ == '__main__':
    Test().exe()
    ...
