#!/usr/bin/env python3
# Author ID: rakkerman1

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return f"Error: {error.decode('utf-8').strip()}"
    else:
        return output.decode('utf-8').strip()

if __name__ == "__main__":
    print(free_space())

