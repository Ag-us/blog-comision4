# Blog_comision4/blog/settings/__init__.py

from .base import *

# Configuración local para desarrollo en tu máquina
try:
    from .local import *
except ImportError:
    pass

# Configuración para producción en PythonAnywhere u otro servidor
try:
    from .production import *
except ImportError:
    pass