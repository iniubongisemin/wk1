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
shell_mode_detector()