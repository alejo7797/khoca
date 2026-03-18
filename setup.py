#!/usr/bin/env python

# A packaging of Khoca that allows easy installation using pip.
#
# Sebastian Oehms, 09/24/2021
# seb.oehms@gmail.com
#
# Run `python -m build` and it will automatically download all the
# necessary sources and create a tar ball suitable for pip.
#
# We can upload with `twine upload -r pypi dist/khoca-...tar.gz`.

import os.path
from platform import system

from Cython.Build import cythonize
from setuptools import Extension, setup

v_file = "_version.py"
version = "0.9"
with open(v_file) as f:
    # read the current version from file
    code = f.read()
    exec(code, locals())

khoca_dir = "."
src_dir = "src"
bin_dir = "bin"
data_dir = "data"
converters_dir = "converters"

khoca_pkg = "khoca"
bin_pkg = ".".join([khoca_pkg, bin_dir])
data_pkg = ".".join([khoca_pkg, data_dir])
converters_pkg = ".".join([khoca_pkg, converters_dir])

pui_name = "khoca.bin.pui"

Linux = system() == "Linux"
MacOS = system() == "Darwin"
Windows = system() == "Windows"

include_dirs = []
library_dirs = []
extra_objects = []
extra_compile_args = ["-c", "-D__STDC_LIMIT_MACROS", "-Wall"]
extra_link_args = ["-lpthread", "-lstdc++", "-t"]
libraries = []

if Linux:
    extra_compile_args += ["-fopenmp", "-std=c++11", "-shared", "-fPIC", "-O3"]
    extra_link_args += ["-z defs"]
    libraries = ["gmp", "gmpxx", "pari"]

elif MacOS:
    locdir = "Pari42"
    pari_include_dir = os.path.join(locdir, "include")
    pari_library_dir = os.path.join(locdir, "lib")
    homebrew_lib = "/opt/homebrew/lib/"
    include_dirs += [
        "/opt/homebrew/opt/libomp/include",
        "/opt/homebrew/include/",
        pari_include_dir,
    ]
    library_dirs += [
        "/opt/homebrew/opt/libomp/lib",
        homebrew_lib,
        pari_library_dir,
    ]
    extra_compile_args += [
        "-std=c++11",
        "-shared",
        "-fPIC",
        "-O3",
        "-mmacosx-version-min=10.9",
        "-Wno-unreachable-code",
        "-Wno-unreachable-code-fallthrough",
    ]
    libraries = ["gmp", "gmpxx", "pari"]

elif Windows:
    locdir = "Pari42"
    pari_include_dir = os.path.join(locdir, "include")
    pari_library_dir = os.path.join(locdir, "bin")
    gmp_include_dir = r"C:\msys64\usr\include"
    gmp_library_dir = r"C:\msys64\mingw64\lib"
    gmp_library_dir_bin = r"C:\msys64\mingw64\bin"

    include_dirs += [pari_include_dir, gmp_include_dir]
    library_dirs += [gmp_library_dir, gmp_library_dir_bin, pari_library_dir]
    extra_compile_args += ["/DDISABLE_INLINE", "/openmp", "/std:c11", "/LD"]
    extra_link_args = [
        os.path.join(gmp_library_dir, "libgmp.dll.a"),
        os.path.join(gmp_library_dir, "libgmpxx.dll.a"),
        os.path.join(pari_library_dir, "libpari.dll.a"),
    ]

pui_sources = [
    "src/krasner/krasner.cpp",
    "src/planar_algebra/coefficient_rings.cpp",
    "src/planar_algebra/planar_algebra.cpp",
    "src/planar_algebra/smith.cpp",
    "src/planar_algebra/sparsemat.cpp",
    "src/python_interface/pythonInterface.cpp",
    "src/python_interface/pui.pyx",
    "src/shared.cpp",
]

pui_ext = Extension(
    name=pui_name,
    sources=pui_sources,
    language="c++",
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    extra_objects=extra_objects,
    extra_compile_args=extra_compile_args,
    libraries=libraries,
    extra_link_args=extra_link_args,
)

setup(
    name=khoca_pkg,
    version=version,
    packages=[
        khoca_pkg,
        bin_pkg,
        converters_pkg,
        data_pkg,
    ],
    package_dir={
        khoca_pkg: khoca_dir,
        bin_pkg: bin_dir,
        converters_pkg: converters_dir,
        data_pkg: data_dir,
    },
    ext_modules=cythonize(
        pui_ext,
    ),
    package_data={
        data_pkg: ["*"],
    },
)
