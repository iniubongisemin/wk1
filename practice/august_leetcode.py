"""
34. Conditional Sum to 20
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""
def conditional_sum(x, y):
    num_sum = x + y
    if num_sum > 15 and num_sum < 20:
        print(20)
    else:
        print(f"{num_sum} is not between 15 and 20")
# conditional_sum(-4, 20)


"""
40. Distance Between Points
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""
def slope(x1, y1, x2, y2):
    import math
    x = (x2-x1)**2
    y = (y1-y2)**2
    z =  x + y 
    d = math.sqrt(z)
    print(d)
# slope(3, 4, 2, 2)

"""
41. File Existence Checker
Write a Python program to check whether a file exists.
"""
def file_existence():
    import os
    file = os.path.isfile("names.txt")
    if file is True:
        print("The file exists")
    else:
        print("The file does not exist")
# file_existence()

"""
43. OS and Platform Info
Write a Python program to get OS name, platform and release information.
"""
def os_info():
    import os
    import platform
    os_name = os.name
    platform_info = platform.platform()
    os_release = platform.release()
    print(f"OS: {os_name} Platform: {platform_info} \n Release: {os_release}")
# os_info()

"""
44. Python Site Packages Locator
Write a Python program to locate Python site packages.
"""
def site_packages():
    import site
    pckge = site.getsitepackages()
    print(f"SITE_PACKAGES_LIST>>>>>{pckge}")
# site_packages()

"""
42. Shell Mode Detector
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""
def shell_mode_detector():
    import platform
    info = platform.architecture()[0]
    print(f"{info}")
# shell_mode_detector()

"""
48. String to Numeric Parser
Write a Python program to parse a string to float or integer.
"""
def string_num(var: str):
    if "." in var:
        variable = float(var)
    else:
        variable = int(var) 
    print(f"{variable}")
# string_num("2.05")

"""
45. External Command Runner
Write a Python program that calls an external command.
"""
def ext_command(command: str):
    import subprocess
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        print(f"Exit Code: {result.returncode}")
    except subprocess.CalledProcessError as e:
        return str(f"An error occurred {e}")
# ext_command("deactivate")

"""
46. File Path and Name Finder
Write a Python program to retrieve the path and name of the file currently being executed.
"""
def path_name_finder():
    import os
    file_path = os.path.realpath(__file__)
    print(f"File Path: {file_path}")
# path_name_finder()

"""
47. CPU Count Finder
Write a Python program to find out the number of CPUs used.
"""
def cpu_counter():
    import os
    cpu_count = os.cpu_count()
    print(f"Number of CPU's used = {cpu_count}")
# cpu_counter()

"""
49. Directory Files Lister
Write a Python program to list all files in a directory.
"""
def directory_files_lister(directory):
    import os
    directories = os.listdir(directory)
    print(directories)
# directory_files_lister(r"C:\Users\eugen\OneDrive\Documents\backend\wk1")

"""
50. Print Without Newline
Write a Python program to print without a newline or space.
"""
def print_without_newline():
    print("hello", end="")
    print("world", end="")
# print_without_newline()

def print_to_stderr():
    import sys
    import logging

    print("This is an error message!", sys.stderr)
# print_to_stderr()

"""
51. Find Local IPs
Write a Python program to find local IP addresses using Python's stdlib.
"""
def local_ips():
    import socket
    local_ip_addr = set()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    local_ip_addr.add(ip_address)
    print(local_ip_addr)
# local_ips()

"""
52. Print to STDERR
Write a Python program to print to STDERR.
"""
def print_to_stderr():
    import sys

    print("This message goes to STDOUT (standard output)")
    sys.stderr.write("Method 1: Using sys.stderr.write() - Error message")
print_to_stderr()


