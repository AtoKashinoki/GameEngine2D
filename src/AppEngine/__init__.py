"""
    AppEngine

This file contain import system.
"""


""" Prevent execution this file """


if __name__ == '__main__':
    from CodingTools2.Errors import PreventExecution
    raise PreventExecution(__file__)


""" imports """


try:
    from . import Engine
    ...
except ImportError as error:
    Engine = ImportError(error)
    ...


try:
    from . import InputSystem
    ...
except ImportError as error:
    InputSystem = ImportError(error)
    ...


try:
    from . import RenderSystem
    ...
except ImportError as error:
    RenderSystem = ImportError(error)
    ...


try:
    from . import Object
    ...
except ImportError as error:
    Object = ImportError(error)
    ...


try:
    from . import Texture
    ...
except ImportError as error:
    Texture = ImportError(error)
    ...

