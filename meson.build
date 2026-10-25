project(
  'khoca',
  'cpp', 'cython',
  version: '1.5',
  default_options: ['cpp_std=c++11'],
  meson_version: '>=1.10.2',
)

# Python module
py = import('python').find_installation(
  pure: false,
)

# Compilers
cxx = meson.get_compiler('cpp')
cython = meson.get_compiler('cython')

# Dependencies
openmp = dependency(
  'openmp',
  required: false,
)

threads = dependency(
  'threads',
  required: false,
)

gmp = [
  dependency('gmp'),
  dependency('gmpxx'),
]

# Find PARI
pari = cxx.find_library(
  'pari',
  has_headers: ['pari/pari.h']
)

subdir('data')
subdir('src')
subdir('khoca')
