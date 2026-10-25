{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  strictDeps = true;

  buildInputs = [
    pkgs.gmp
    pkgs.pari
    pkgs.python3
  ];

  nativeBuildInputs = [
    pkgs.python3
    pkgs.python3Packages.build
    pkgs.python3Packages.cython
    pkgs.python3Packages.meson-python
    pkgs.meson
    pkgs.ninja
    pkgs.pkg-config
  ];
}
