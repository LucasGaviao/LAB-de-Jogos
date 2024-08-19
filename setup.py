import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["PPlay", "pygame", "random", "time"]}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

setup(
    name = "NikitRun",
    version = "0.1",
    description = "Game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)]
)