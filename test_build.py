import os
import subprocess

def test_build():
 # Run the build script
 subprocess.run(['python', 'build_executable.py'])

 # Check if the expected executable files are generated
 expected_executables = ['flickering_windows.exe']
 for executable in expected_executables:
 assert os.path.exists(executable)

if __name__ == "__main__":
 test_build()
