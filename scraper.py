"""
This file will handle the business logic required to perform the scraping needed to form the new txt file.
"""
import requests

# Constants
PATH = ""
VOLTRON_URL = "https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt"
SMALL_URL = "https://raw.githubusercontent.com/GrahamJA-97/DIM-wishlist-pve-scraper/python/local-samples/small.txtxt"

def do_thing(shouldFilter):
    response = requests.get(VOLTRON_URL, stream=True)

    if shouldFilter:
        filtered_result(response)
    else:
        full_list(response)

def full_list(response):
    output_file = open(PATH + "output.txt", "w")
    for line in response.iter_lines():
        output_file.write(line.decode("utf-8") + "\n")

    output_file.close()

def filtered_result(response):
    output_file = open(PATH + "filtered_result.txt", "w")
    found_pvp = False

    for line in response.iter_lines():
        decoded = line.decode("utf-8")
        lower = decoded.lower()
        if (not found_pvp) and ("pvp" in lower) and (not "pve" in lower):
            found_pvp = True
        elif not line:
            found_pvp = False

        if not found_pvp:
            output_file.write(decoded + "\n")

    output_file.close()

if __name__ == '__main__':
    print("~~~~~Start of file reading~~~~~")

    do_thing(True)

    print("~~~~~End of file reading~~~~~")
