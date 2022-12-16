# DIM Wishlist PvE Scraper

This project is for messing around with the "wishlists" feature of the tool
[DIM](https://github.com/DestinyItemManager/DIM), which is a community app that supports the gameplay in 
[Destiny 2](https://www.bungie.net/).

Specifically we are trying to tweak a pre-compiled txt file to filter out sections of it that mention PvP 
(Player vs Player) weapon rolls to try and optimize the tool for player like me who only care about PvE 
(Player vs Environment) content.

### Approach
I plan to start out with a python script that will read a local txt file and scrape the results into an output file,
with the long term plan being I can point at the url where a regularly updated file will live and can just run the 
script whenever that file is updated.
