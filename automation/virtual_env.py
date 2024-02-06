
import os
import subprocess
import platform

def virtual_env_setup(directory):

    pc_type = platform.system()

    # installs .venv file into the new directory
    subprocess.run(["python3", "-m", "venv", ".venv"], cwd=directory)

    # activates .venv if the user is on mac.
    if pc_type == "Darwin":
        subprocess.run(["source", ".venv/bin/activate"], cwd=directory, executable='/bin/bash')
    
    # activates .venv if the user is on pc.
    elif pc_type == "Windows":

        
        # This might have to change because it might be different for each user
        bash_path = r"C:\Program Files\Git\usr\bin\bash.exe"

        subprocess.run(["source", ".venv/Scripts/activate"], cwd=directory, executable= bash_path)

    else:
        pass
        #throw an error
