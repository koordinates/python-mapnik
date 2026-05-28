#! /usr/bin/env python3

from pybind11.setup_helpers import Pybind11Extension, build_ext, ParallelCompile, naive_recompile
from setuptools import setup, find_namespace_packages
import shlex
import subprocess
import os
import sys


def check_output(args):
     output = subprocess.check_output(args).decode()
     return output.rstrip('\n')


def pkg_config(*args):
     return check_output(['pkg-config', *args])


lib_path = os.path.join(pkg_config('--variable=prefix', 'libmapnik'), 'lib')
input_plugin_path = pkg_config('--variable=plugins_dir', 'libmapnik')
font_path = os.environ.get('SYSTEM_FONTS') or pkg_config('--variable=fonts_dir', 'libmapnik')

linkflags = shlex.split(pkg_config('--libs', 'libmapnik'))

f_paths = open('packaging/mapnik/paths.py', 'w')
f_paths.write('import os\n')
f_paths.write('\n')
f_paths.write("mapniklibpath = '{path}'\n".format(path=lib_path))
f_paths.write("mapniklibpath = os.path.normpath(mapniklibpath)\n")
f_paths.write("inputpluginspath = '{path}'\n".format(path=input_plugin_path))
f_paths.write("fontscollectionpath = '{path}'\n".format(path=font_path))
f_paths.write("__all__ = [mapniklibpath,inputpluginspath,fontscollectionpath]\n")
f_paths.close()

extra_comp_args = shlex.split(pkg_config('--cflags', 'libmapnik'))
extra_comp_args = [a for a in extra_comp_args if a != "-fvisibility=hidden"]

if os.environ.get("PYCAIRO", "false") == "true":
     import cairo
     extra_comp_args.append('-DHAVE_PYCAIRO')
     extra_comp_args.append('-I' + cairo.get_include())

if sys.platform != 'darwin':
     linkflags.append('-lrt')

ext_modules = [
     Pybind11Extension(
          "mapnik._mapnik",
          [
               "src/mapnik_python.cpp",
               "src/mapnik_layer.cpp",
               "src/mapnik_query.cpp",
               "src/mapnik_map.cpp",
               "src/mapnik_color.cpp",
               "src/mapnik_composite_modes.cpp",
               "src/mapnik_coord.cpp",
               "src/mapnik_envelope.cpp",
               "src/mapnik_expression.cpp",
               "src/mapnik_datasource.cpp",
               "src/mapnik_datasource_cache.cpp",
               "src/mapnik_gamma_method.cpp",
               "src/mapnik_geometry.cpp",
               "src/mapnik_feature.cpp",
               "src/mapnik_featureset.cpp",
               "src/mapnik_font_engine.cpp",
               "src/mapnik_fontset.cpp",
               "src/mapnik_grid.cpp",
               "src/mapnik_grid_view.cpp",
               "src/mapnik_image.cpp",
               "src/mapnik_image_view.cpp",
               "src/mapnik_projection.cpp",
               "src/mapnik_proj_transform.cpp",
               "src/mapnik_rule.cpp",
               "src/mapnik_symbolizer.cpp",
               "src/mapnik_debug_symbolizer.cpp",
               "src/mapnik_markers_symbolizer.cpp",
               "src/mapnik_polygon_symbolizer.cpp",
               "src/mapnik_polygon_pattern_symbolizer.cpp",
               "src/mapnik_line_symbolizer.cpp",
               "src/mapnik_line_pattern_symbolizer.cpp",
               "src/mapnik_point_symbolizer.cpp",
               "src/mapnik_raster_symbolizer.cpp",
               "src/mapnik_scaling_method.cpp",
               "src/mapnik_style.cpp",
               "src/mapnik_logger.cpp",
               "src/mapnik_placement_finder.cpp",
               "src/mapnik_text_symbolizer.cpp",
               "src/mapnik_palette.cpp",
               "src/mapnik_parameters.cpp",
               "src/python_grid_utils.cpp",
               "src/mapnik_raster_colorizer.cpp",
               "src/mapnik_label_collision_detector.cpp",
               "src/mapnik_dot_symbolizer.cpp",
               "src/mapnik_building_symbolizer.cpp",
               "src/mapnik_shield_symbolizer.cpp",
               "src/mapnik_group_symbolizer.cpp",
               "src/mapnik_view_transform.cpp"
          ],
          extra_compile_args=extra_comp_args,
          extra_link_args=linkflags,
     )
]

if os.environ.get("CC", False) == False:
    os.environ["CC"] = 'c++'
if os.environ.get("CXX", False) == False:
    os.environ["CXX"] = 'c++'

ParallelCompile("NUM_JOBS", needs_recompile=naive_recompile).install()
setup(
     name="mapnik",
     include_package_data=True,
     packages=find_namespace_packages(where="packaging"),
     package_dir={"": "packaging"},
     ext_modules=ext_modules,
     cmdclass={"build_ext": build_ext},
)
