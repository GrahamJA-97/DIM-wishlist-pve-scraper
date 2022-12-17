"""
This file will handle the business logic required to perform the scraping needed to form the new txt file.
"""
import os
import urllib.request

import requests

# CONSTANTS
URL_TO_SCRAPE = "https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt"
SMALL_FILE_NAME = os.path.join('local-sample', 'small.txt')
FULL_FILE_NAME = os.path.join('local-sample', 'voltron.txt')


# function for testing the process to see if it works on small local files before scaling up to the web version
def lines_from_file(file_name):
    print("File name: " + file_name + "\n")
    with open(file_name, "r") as file:
        print("Exists: " + file)
        for line in file:
            print(line)


def lines_from_urllib(url):
    response = urllib.request.urlopen(url)
    return response.readlines()


def process_with_request(url):
    request = requests.get(url)
    # if request != requests.codes.ok:
    #     print("Something wrong with request, try again later")
    #     return

    for line in request.text:
        print(line)
        # if "pvp" in line.lower():
        #     print(line)


if __name__ == '__main__':
    print("~~~~~Start of file reading~~~~~")
    # with open("output.txt", 'w') as output_file:
    lines = lines_from_urllib(URL_TO_SCRAPE)
    found_pvp = False

    for line in lines:
        string = line.decode()

        if "PvP" in string:
            found_pvp = True
            print("~~~~~~~~~~~~" + string)
        # elif string == '\n':
        #     found_pvp = False
        else:
            print(string)

    print("~~~~~End of file reading~~~~~")
