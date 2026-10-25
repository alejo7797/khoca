py.extension_module(
  'pui',
  [
    shared_src,
    planar_algebra_src,
    krasner_src,
    'pui.pyx',
    'pythonInterface.cpp',
  ],
  dependencies: [
    openmp,
    threads,
    gmp,
    pari,
  ],
  override_options: ['cython_language=cpp'],
  install: true,
  subdir: 'khoca',
)
