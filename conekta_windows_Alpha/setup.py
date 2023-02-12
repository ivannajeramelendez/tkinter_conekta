import cx_Freeze
import sys
import matplotlib
import conekta

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("formulario.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "Club-Alpha",
    options = {"build_exe": {"packages":["tkinter","matplotlib","conekta"], "include_files":["icon.ico"]}},
    version = "0.01",
    description = "Pagos con Oxxo",
    executables = executables
    )