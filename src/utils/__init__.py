# haxe doesn't have the @expose function for python so we have to use __init__.py to name the export what we want.
from .resin_device import resin_Supervisor as Supervisor

__version__ = "xxx"
