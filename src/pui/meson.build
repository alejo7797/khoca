includes = include_directories(
  '.',
  'krasner',
  'planar_algebra',
  'python_interface',
)

sources = files(
  'shared.cpp',
  'krasner/krasner.cpp',
  'planar_algebra/coefficient_rings.cpp',
  'planar_algebra/planar_algebra.cpp',
  'planar_algebra/smith.cpp',
  'planar_algebra/sparsemat.cpp',
  'python_interface/pythonInterface.cpp',
  'python_interface/pui.pyx',
)

py.extension_module(
  'pui',
  sources,
  include_directories: includes,
  dependencies: [
    gmp,
    gmpxx,
    pari
  ],
  override_options: [
    'cython_language=cpp'
  ],
  install: true,
  subdir: 'khoca' / 'bin'
)
