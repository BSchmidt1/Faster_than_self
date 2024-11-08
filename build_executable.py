import os
import PyInstaller.__main__

def build_executable(build_config):
    with open(build_config, 'r') as f:
        build_list = [line.strip() for line in f.readlines()]

    for file in build_list:
        PyInstaller.__main__.run([
            '--onefile',
            '--windowed',
            file
        ])

if __name__ == "__main__":
    build_executable('build_list')
