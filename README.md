Province Generator is a tool which requires two arguments:
1. The base game's files to read from (these are not written to)
2. A mod folder, which MUST have map/provinces.bmp
Given this provinces.bmp map, it will iterate through every pixel, initializing the data for any new provinces not already defined in the definitions.csv file. The following things are created:
1. definitions.csv (Will be overwritten/re-created)
1. positions.txt (adds the center of each province as the position of all assets. This WILL OVERWRITE EXISTING DEFINITIONS. Will be changed in a later patch)
1. PossibleErrors.txt (NOT a game file: this is written in the same folder as the ProvinceGenerator.py. This file outputs any province definitions that has no pixels, and provinces who's average pixel do not lie in their own border. The latter helps detect possible "duplicate" provinces, who use the same colour)
1. prov_names_l_english.yml and prov_names_adj_l_english.yml (Does not overwrite existing province names)
1. province/history files (Does not overwrite for existing provinces)

IMPORTANT NOTE!!!
This initialization process uses different names for the province names in history/provinces. In order for the game to accept this, inside of your mod descriptor file, add the following line:
```
replace_path = "history/provinces"
```
This will tell your mod to ignore the base game's province history files. This may prove problematic however, if you are not interesting in doing a full-conversion mod. 