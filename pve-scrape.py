import re
import requests

def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a valid response
    return response.text

def filter_pvp_blocks(url, output_file):
    # Download the file content
    data = download_file(url)

    # Split the data into blocks using double newlines (indicating empty lines between blocks)
    blocks = data.split('\n\n')

    filtered_blocks = []

    for block in blocks:
        # Skip blocks that contain "PvP", unless they mention "PvE" (case-insensitive)
        if re.search(r'pvp', block, re.IGNORECASE) and not re.search(r'pve', block, re.IGNORECASE):
            continue

        # Add the cleaned block to the filtered list
        filtered_blocks.append(block.strip())

    # Join the filtered blocks and write to the output file
    cleaned_data = '\n\n'.join(filtered_blocks).strip()

    with open(output_file, 'w') as outfile:
        outfile.write(cleaned_data)

# Specify the URL and output file
url = 'https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt'
output_file = 'voltron-pve-filter.txt'

# Run the filtering function
filter_pvp_blocks(url, output_file)

print(f"Filtered data has been saved to {output_file}")
