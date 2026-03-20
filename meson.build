project(
  'khoca',
  'cpp',
  'cython',

  version: run_command(
    ['src/khoca/_version.py'], check: true
  ).stdout().strip(),

  default_options: [
    'buildtype=release',
    'cpp_std=c++11'
  ]
)

gmp = dependency('gmp')
gmpxx = dependency('gmpxx')

cxx = meson.get_compiler('cpp')
pari = cxx.find_library('pari')

py = import('python').find_installation(pure: false)

subdir('src/khoca')
subdir('src/pui')
