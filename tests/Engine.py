

from CodingTools2.Definitions import System
from AppEngine.Engine import FlameEngine


class Test(FlameEngine):

    def __update__(self) -> None | int:
        print(self.frame.pressed)
        if 32 in self.frame.pressed and 101 in self.frame.pressed:
            return System.EXIT
        if 32 in self.frame.pressed and 114 in self.frame.pressed:
            return System.REBOOT
        return
    def __render__(self) -> None: ...

    ...


if __name__ == '__main__':
    Test().exe()
    ...
