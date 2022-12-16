"""
This file will handle the business logic required to perform the scraping needed to form the new txt file.
"""


def grab_file(file_name):
    if file_name and file_name.strip():
        print("Provided file name is empty")
        return

    with open(file_name) as reader:
        print(file_name)
