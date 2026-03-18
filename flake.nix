{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };
  };

  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {

      systems = [
        "x86_64-linux"
      ];

      perSystem =
        {
          pkgs,
          ...
        }:
        {
          devShells.default =

            let
              python = pkgs.python3;
              venv = python.withPackages (ps: [
                ps.build
                ps.cython
                ps.meson-python
              ]);
            in

            pkgs.mkShell {

              nativeBuildInputs = [
                pkgs.bear
                pkgs.ninja
                pkgs.pkg-config
                venv
              ];

              buildInputs = [
                pkgs.gmp
                pkgs.pari
                python
              ];

            };

        };

    };
}
