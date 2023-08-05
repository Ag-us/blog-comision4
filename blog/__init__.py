# Blog_comision4/blog/settings/__init__.py

from .settings.base import *

# Configuración local para desarrollo en tu máquina
try:
    from .settings.local import *
except ImportError:
    pass

# Configuración para producción en PythonAnywhere u otro servidor
try:
    from .settings.production import *
except ImportError:
    pass