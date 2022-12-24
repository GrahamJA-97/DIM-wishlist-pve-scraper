# DIM Wishlist PvE Scraper

This project is for messing around with the "wishlists" feature of the tool
[DIM](https://github.com/DestinyItemManager/DIM), which is a community app that supports the gameplay in 
[Destiny 2](https://www.bungie.net/).

Specifically we are trying to tweak a pre-compiled txt file to filter out sections of it that mention PvP 
(Player vs Player) weapon rolls to try and optimize the tool for player like me who only care about PvE 
(Player vs Environment) content.

The Wishlist that we are trying to manipulate is the main "voltron" wishlist that DIM uses by default located [here](https://github.com/48klocs/dim-wish-list-sources/blob/master/voltron.txt).

### How to use
Add of the output files as a source in your DIM account to view the filtered down version of the "voltron" list. If an update to that list has been posted and I missed it, feel free to open a pull request with your own version to update it.

### Scripts/code for extrating the filtered list
Each language will exist on thier own branches, with main only containing the filtered txt files to choose from.
