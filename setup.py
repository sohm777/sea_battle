from cx_Freeze import setup, Executable
import sys
import os

includes = []
include_files = [r"C:\Users\Igor\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"C:\Users\Igor\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
                 r"C:\Users\Igor\AppData\Local\Programs\Python\Python36-32\Scripts\dist\ship.ico"]
os.environ['TCL_LIBRARY'] = r'C:\Users\Igor\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Igor\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
base = 'Win32GUI' if sys.platform == 'win32' else None


setup(name='SeaBattle', version='0.9', description='Classic Sea Battle',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=[Executable(r'C:\Users\Igor\AppData\Local\Programs\Python\Python36-32\Scripts\dist\START.py', base=base)])
