#!/usr/local/bin/python3
import sys
from pathlib import Path
import glob
import os


def change_working_dir():
    home = str(Path.home())
    home += "/commands/"
    os.chdir(home)
    return home


def get_py_files(path):
    files = [f for f in glob.glob(pathname=(path + "*.py"))]
    for idx, file in enumerate(files):
        filename = file.rsplit("/", 1)[1]
        files[idx] = filename
    return files


def get_func_return_value(file):
    vn = os.popen(f"python3 -c 'from {file[:-3]} import version; import sys; sys.stdout.write(version())'").read()
    return vn


def get_var_value(line, file, var_and_val):
    split_at_eq = line.split("=")
    for idx, i in enumerate(split_at_eq):
        split_at_eq[idx] = split_at_eq[idx].replace(" ", "").replace("\n", "").split(",")
    for idx, i in enumerate(split_at_eq):
        if "version" in i:
            var_and_val.append([file, split_at_eq[1][idx]])


def search_for_var_or_func_in_file(files):
    var_and_val = []
    for file in files:
        with open(file, "r") as f:
            a = f.readlines()
        definition = False
        for line in a:
            if definition and "version(" in line:
                definition = False
                vn = get_func_return_value(file)
                var_and_val.append([file, vn])
            if "version =" in line or "version," in line or " version" in line or "version=" in line and "version():" not in line:
                get_var_value(line, file, var_and_val)
            if "def version" in line:
                definition = True
    return var_and_val



def get_version_func(files):
    ver_func = []
    for file in files:
        try:
            exec(f"import {file}")
        except ImportError:
            print("Could not Import File!")

        try:
            exec(f"a = {file}.version")
            if callable(a):
                exec(f"b = {file}.a()")
                ver_func.append[file, b]
            else:
                exec(f"a = {file}.__dict__['version'])")
                ver_func.append([file, a])
        except:
            print("No version!")
    return ver_func

def get_var_val(files, version_list):
    for file in files:
        if "version" in file.__dict__.keys() and isinstance(file.__dict__["version"], str):
            version_list.append([file, file.__dict__["version"]])


def get_version(files):
    ver_func = []
    for file in py_files:
        try:
            exec(f"import {file[:-3]}")
            exec(f"ver = {file[:-3]}.version")
            if callable(ver):
                exec(f"b = {file[:-3]}.version()")
                ver_func.append([file, b])
            else:
                exec(f"a = {file[:-3]}.__dict__['version']")
                ver_func.append([file, a])
        except ImportError:
            print("Could not Import File!")
        return ver_func


if __name__ == "__main__":
    sys.path.insert(0, "/Users/fq/commands")
    os.chdir("/Users/fq/commands")
    new_work_dir = change_working_dir()
    py_files = get_py_files(new_work_dir)
    #var_and_val = search_for_var_or_func_in_file(py_files)
    ver_func = []
    for file in py_files:
        try:
            exec(f"import {file[:-3]}")
            exec(f"ver = {file[:-3]}.version")
            if callable(ver):
                exec(f"b = {file[:-3]}.version()")
                ver_func.append([file, b])
            else:
                exec(f"a = {file[:-3]}.__dict__['version']")
                ver_func.append([file, a])
        except ImportError:
            print("Could not Import File!")
    print(ver_func)
