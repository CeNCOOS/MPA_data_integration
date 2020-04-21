# MPA_data_integration

Code for converting MPA-related biological data from the California coast to Darwin Core Standard format. <br>
https://dwc.tdwg.org/terms/#occurrence

**Author:** Diana LaScala-Gruenewald <br>
**Code:** Python 3.7

## Folders and files currently included:
**CCFRP** - code for converting California Collaborative Fisheries Research Program data
- **CCFRP_species_name_conversion.ipynb** - initial code for finding scientific names from common names
- **CCFRP_common_to_scientific.csv** - file containing common and scientific names for all species in CCFRP data set

**WoRMS.py** - functions for querying the World Register of Marine Species (WoRMS) REST API
