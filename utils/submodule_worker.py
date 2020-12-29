import importlib
import importlib.util
import os.path


def import_submodules(module):
    print(f"🚀 Enabling endpoints...")
    print(f"├ 📖 Loading \"{module}\" as a module.")
    module = importlib.util.find_spec(module)

    if module is None:
        raise ValueError(f"Specified path {module} is not a module.")

    print(f"├ 🔎 Searching modules in \"{module.name}\".")
    locations = set(module.submodule_search_locations)
    for location in locations:
        print(f"│     ├ 📂 {location}/")
        __enable_endpoint_from_dir(location, 2, module.name)
    print("│     └ ✨ Done!")
    print("└ ✨ Done!")


def __enable_endpoint_from_dir(location, level, module):
    arrow = "{}├".format("│     " * level)
    terminate = "{}└".format("│     " * level)

    for child in os.listdir(location):
        path = os.path.join(location, child)
        if os.path.isdir(path):
            if child == "__pycache__":
                print(f"{arrow} 📁 {child}/ (cache folder; skipping)")
                continue
            print(f"{arrow} 📂 {child}/")
            __enable_endpoint_from_dir(path, level + 1, module + "." + child)
        if os.path.isfile(path):
            __read_module(location, child, arrow, module)
    print(f"{terminate} ✨ Done!")


def __read_module(directory, child, indent, module):
    path = os.path.join(directory, child)
    if not child.endswith(".py"):
        print(f"{indent} 📝 {child}")
        return

    print(f"{indent} 🐍 {child}")
    module_spec = importlib.util.spec_from_file_location(module + "." + child.replace(".py", ""), path)
    if module_spec is None:
        raise ValueError(f"Couldn't import {path}!")
    importlib.import_module(module_spec.name)

    importlib.import_module(".hello_world", "controller.endpoint")