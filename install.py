import subprocess
import os
import shutil

if(os.name == "nt"):
    os_build_script = "build_win64.py"
else:
    os_build_script = "build_linux.py"

subprocess.call(os_build_script, shell=True, cwd="build")
if not os.path.exists(os.path.join("..", "Source", "ThirdParty")):
    os.mkdir(os.path.join("..", "Source", "ThirdParty"))
if os.path.exists(os.path.join("..", "Source", "ThirdParty", "libprotobuf")):
    shutil.rmtree(os.path.join("..", "Source", "ThirdParty", "libprotobuf"), True)

shutil.copytree("libprotobuf", os.path.join("..", "Source", "ThirdParty", "libprotobuf"))
