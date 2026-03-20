project(
  'khoca',
  'cpp', 'cython',

  version: run_command(
    ['src/khoca/_version.py'], check: true
  ).stdout().strip(),

  default_options: [
    'buildtype=debugoptimized',
    'cpp_std=c++11',
    'warning_level=2',
  ],
)

cpp = meson.get_compiler('cpp')

py = import('python').find_installation(
  pure: false,
)

gmp_deps = [
  dependency('gmp'),
  dependency('gmpxx'),
]

pari_dep = cpp.find_library('pari')

# Pass -fopenmp
openmp_dep = dependency('openmp')

# Pass -fpthread
thread_dep = dependency('threads')

subdir('src/khoca')
subdir('src/pui')
