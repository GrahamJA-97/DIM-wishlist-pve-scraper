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
    seen_wishlist_items = set()

    for block in blocks:
        # Skip blocks that contain "PvP", unless they mention "PvE" (case-insensitive)
        if re.search(r'pvp', block, re.IGNORECASE) and not re.search(r'pve', block, re.IGNORECASE):
            continue

        # Process block lines to remove duplicate dimwishlist:item= entries
        lines = block.split('\n')
        unique_lines = []
        contains_wishlist_item = False

        for line in lines:
            if line.startswith("dimwishlist:item="):
                if line in seen_wishlist_items:
                    continue
                seen_wishlist_items.add(line)
                contains_wishlist_item = True
            unique_lines.append(line)

        # Skip block if no item roll lines remain
        if not contains_wishlist_item:
            continue

        # Add the cleaned block to the filtered list
        filtered_blocks.append('\n'.join(unique_lines).strip())

    # Join the filtered blocks and write to the output file
    cleaned_data = '\n\n'.join(filtered_blocks).strip()

    # Custom title and description lines to add to the output file
    custom_lines = "title:This is a filtered down version of voltron.txt, a compiled collection of god/recommended rolls from top community minds.\n" + \
                   "description:This has been filtered down to remove duplicate rolls and rip out any PVP specific rolls, updated when I think to and dependent on its source (voltron.txt).\n"

    # Write to the output file with custom lines at the top
    with open(output_file, 'w') as outfile:
        outfile.write(custom_lines + '\n' + cleaned_data)


# Specify the URL and output file
url = 'https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt'
output_file = 'voltron-pve-filter.txt'

# Run the filtering function
filter_pvp_blocks(url, output_file)

print(f"Filtered data has been saved to {output_file}")
