import os
import platform


_machine = platform.machine()
mapniklibpath = f"/usr/lib/{_machine}-linux-gnu"
inputpluginspath = os.path.join(mapniklibpath, 'mapnik', 'input')
fontscollectionpath = os.path.join(mapniklibpath, 'mapnik', 'fonts')

__all__ = [mapniklibpath,inputpluginspath,fontscollectionpath]
