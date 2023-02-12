import cx_Freeze
import sys
import conekta

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("formulario.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "Referencias_Oxxo",
    options = {"build_exe": {"packages":["tkinter","conekta"], "include_files":["icon.ico"]}},
    version = "0.01",
    description = "By - Ivan Najera",
    executables = executables
    )