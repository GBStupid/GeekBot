{
  description = "discord bot using discord.py with dotenv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python311;
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            (python.withPackages (ps: with ps; [
              aiohttp
              aiosignal
              astroid
              attrs
              black
              click
              dill
              discordpy
              frozenlist
              idna
              isort
              mccabe
              multidict
              mypy
              mypy-extensions
              packaging
              pathspec
              platformdirs
              propcache
              pylint
              python-dotenv
              tomlkit
              typing-extensions
              urllib3
              yarl
              types-requests
              aiohappyeyeballs
            ]))
          ];
        };
      });
}
