import sys
import logging
import configparser
import pathlib
import string

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if(len(sys.argv) < 4):
    logger.critical("Not engouh arguments provided. You should set the <genfile> <genlocation> <projectname>")
    sys.exit(1)

config = configparser.ConfigParser()
config.optionxform = str
config.read(sys.argv[1])

include_root = pathlib.Path(sys.argv[2]) / "include"
src_root = pathlib.Path(sys.argv[2]) / "src"
gen_root = include_root / "gen"
project_root = pathlib.Path("./project") / sys.argv[3].lower()

gen_root.mkdir(parents=True, exist_ok=True)
project_root.mkdir(parents=True, exist_ok=True)

gen_template_string = ""
with open("./scripts/templates/header_gen.template") as template:
    gen_template_string = string.Template(template.read())

header_template_string = ""
with open("./scripts/templates/header.template") as template:
    header_template_string = string.Template(template.read())

source_template_string = ""
with open("./scripts/templates/source.template") as template:
    source_template_string = string.Template(template.read())

library_gen_template_string = ""
with open("./scripts/templates/library_gen.template") as template:
    library_gen_template_string = string.Template(template.read())

library_template_string = ""
with open("./scripts/templates/library.template") as template:
    library_template_string = string.Template(template.read())

gdnlib_template_string = ""
with open("./scripts/templates/gdnlib.template") as template:
    gdnlib_template_string = string.Template(template.read())

gdns_template_string = ""
with open("./scripts/templates/gdns.template") as template:
    gdns_template_string = string.Template(template.read())

includes = []
normal_registration_commands = []
tool_registration_commands = []

if "normal" in config:
    for line in config["normal"]:
        logger.info(f"Generating: {line}")
        gen_file_path = gen_root / f"{line.lower()}.gen.h"
        gdns_file_path = project_root / f"{line.lower()}.gdns"

        model = {
            "class_name" : line,
            "parent_name" : config["normal"][line],
            "upper_class_name" : line.upper(),
            "lower_class_name" : line.lower(),
            "upper_project_name" : sys.argv[3].upper(),
            "lower_project_name": sys.argv[3].lower(),
        }

        normal_registration_commands.append(f"register_class<{line}>();")

        gen_file_path.touch()
        gen_file_path.write_text(gen_template_string.safe_substitute(model))

        gdns_file_path.touch()
        gdns_file_path.write_text(gdns_template_string.safe_substitute(model))

        include_file_path = include_root / f"{line.lower()}.h"
        includes.append(f"#include <{line.lower()}.h>\n")
        if not include_file_path.exists():
            include_file_path.touch()
            include_file_path.write_text(header_template_string.safe_substitute(model))

        src_file_path = src_root / f"{line.lower()}.cpp"
        if not src_file_path.exists():
            src_file_path.touch()
            src_file_path.write_text(source_template_string.safe_substitute(model))
        

if "tool" in config:
    for line in config["tool"]:
        logger.info(f"Generating: {line}")
        gen_file_path = gen_root / f"{line.lower()}.gen.h"
        gdns_file_path = project_root / f"{line.lower()}.gdns"
        
        model = {
            "class_name" : line,
            "parent_name" : config["tool"][line],
            "upper_class_name" : line.upper(),
            "lower_class_name" : line.lower(),
            "upper_project_name" : sys.argv[3].upper(),
            "lower_project_name": sys.argv[3].lower(),
        }

        tool_registration_commands.append(f"register_tool_class<{line}>();")

        gen_file_path.touch()
        gen_file_path.write_text(gen_template_string.safe_substitute(model))

        gdns_file_path.touch()
        gdns_file_path.write_text(gdns_template_string.safe_substitute(model))
        
        include_file_path = include_root / f"{line.lower()}.h"
        includes.append(f"#include <{line.lower()}.h>\n")
        if not include_file_path.exists():
            include_file_path.touch()
            include_file_path.write_text(header_template_string.safe_substitute(model))

        src_file_path = src_root / f"{line.lower()}.cpp"
        if not src_file_path.exists():
            src_file_path.touch()
            src_file_path.write_text(source_template_string.safe_substitute(model))


commands = "".join(normal_registration_commands) + "".join(tool_registration_commands)
includes = "".join(includes)

model = {
    "upper_project_name": sys.argv[3].upper(),
    "lower_project_name": sys.argv[3].lower(),
    "commands": commands,
    "includes": includes,
}

gen_library_file_path = gen_root / "library.gen.h"
gen_library_file_path.touch()
gen_library_file_path.write_text(library_gen_template_string.safe_substitute(model))

library_file_path = src_root / "library.cpp"
if not library_file_path.exists():
    library_file_path.touch()
    library_file_path.write_text(library_template_string.safe_substitute(model))

gdnlib_file_path = project_root / f"{sys.argv[3].lower()}_native.gdnlib"
gdnlib_file_path.touch()
gdnlib_file_path.write_text(gdnlib_template_string.safe_substitute(model))