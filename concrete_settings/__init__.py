import sys

from . import core  # noqa: F401 # imported but unused
from .core import (  # noqa: F401 # imported but unused
    prefix,
    Settings,
    Setting,
    PropertySetting,
    INVALID_SETTINGS,
    Behaviors,
    Behavior,
    override,
)

from .validators import Validator  # noqa: F401 # imported but unused
from .types import Undefined  # noqa: F401 # imported but unused
from .sources import register_source  # noqa: F401 # imported but unused
from .contrib.behaviors import required  # noqa: F401 # imported but unused

setting = PropertySetting

name = "concrete_settings"
PY_VERSION = (sys.version_info.major, sys.version_info.minor)
PY_36 = (3, 6)

if PY_VERSION < PY_36:
    raise ImportError("Python 3.6 or higher is required by concrete_settings library")


def _load_contrib():
    from .contrib.sources import YamlSource, JsonSource, EnvVarSource  # noqa: F401


_load_contrib()


__version__ = "0.0.0"
