r"""
This SCRIPT creates an empty file
"""

import datetime

# filename = "sample1.txt"
filename = datetime.datetime.now()

#Create an empty file
def create_file():
    """This FUNCTION creates an empty file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f" + ".txt") , "w") as file:
        file.write("")

create_file()