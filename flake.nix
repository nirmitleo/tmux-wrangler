{
  description = "tmux wrangler";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          pip
        ]);
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [ 
            pythonEnv
          ];
          shellHook = ''
            export LANG=C.UTF-8
            export POETRY_VIRTUALENVS_IN_PROJECT=true
            export PYTHONDONTWRITEBYTECODE=1

            # Create venv if it doesn't exist
            if [ ! -d "venv" ]; then
              python3 -m venv venv
              venv/bin/pip install -U pip setuptools
              venv/bin/pip install poetry==1.8.3
            fi
            
            export PATH=bin:$PATH
            echo $PATH
            
            # Activate venv
            source ./venv/bin/activate
            echo "✅ Activated venv"


             # Verify Poetry installation
            poetry --version
          '';
        };
      }
    );
}
