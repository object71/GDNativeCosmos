import sys
import logging
import configparser
import pathlib

if(len(sys.argv) < 3):
    sys.exit(1)

config = configparser.ConfigParser()
config.read(sys.argv[1])

gen_root = pathlib.Path(sys.argv[2]) / "include" / "gen"

if "normal" in config:
    for line in config["normal"]:
        gen_file_path = gen_root / f"{line.lower()}.gen.h"
        print(str(gen_file_path.as_posix()), end=";")

if "tool" in config:
    for line in config["tool"]:
        gen_file_path = gen_root / f"{line.lower()}.gen.h"
        print(str(gen_file_path.as_posix()), end=";")