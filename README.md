# MPA_data_integration

Code for converting long-term MPA monitoring data from the California coast to [Darwin Core Standard format](https://dwc.tdwg.org/terms/#occurrence).

Most of these notebooks were used to quality check data and refine DwC conversion scripts. Final versions were uploaded to Axiom's Research Workspace. On that platform, further changes have been made, so that's where the most recent, operational versions of the code can be found.

**Author:** Diana LaScala-Gruenewald <br>
**Language:** Python 3.7 

## Folders and files currently included:
### CCFRP
Code for converting [California Collaborative Fisheries Research Program](https://mlml.sjsu.edu/ccfrp/) data ([archived on DataONE](https://opc.dataone.org/view/doi%3A10.25494%2FP6901R))
- **CCFRP_common_to_scientific.csv** - CSV file containing common and scientific names for all species in CCFRP data set
- **CCFRP_conversion.ipynb** - Jupyter Notebook containing initial code for full DwC conversion
- **CCFRP_grid-level_conversion.ipynb** - Jupyter Notebook containing code for converting grid-cell resolution (non-aggregated) data to DwC
- **CCFRP_grid-level_conversion_withMoF.ipynb** - Jupyter Notebook containing code for converting grid-cell resolution data, with fish counts, fishing effort, and Catch-Per-Unit-Effort included in a [MeasurementOrFact extension](https://tools.gbif.org/dwca-validator/extension.do?id=http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact) file. **This is the final notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.** 
- **CCFRP_species_name_conversion.ipynb** - Jupyter Notebook containing initial code for finding scientific names from common names using the [WoRMS API](http://www.marinespecies.org/rest/).

### Estuaries
Code for converting data from the Estuaries monitoring program led by researchers at Moss Landing Marine Laboratories
- **estuaries_preliminary_data.ipynb** - Jupyter Notebook containing an exploration and description of preliminary vegetation survey and fish seine/cast net surveys conducted in Spring 2021

### MARINe
Code for converting data from the [MARINe](https://marine.ucsc.edu/) monitoring program ([count](https://data.piscoweb.org/metacatui/view/doi%3A10.6085%2FAA%2Fmarine_ltm.4.8) and [photoplot/transect data archived on DataONE](https://data.piscoweb.org/metacatui/view/doi%3A10.6085%2FAA%2Fmarine_ltm.12.5))
- **MARINe_LTM_count_conversion.ipynb** - Jupyter Notebook containing the conversion code for sea star and Katharina count data. **This is the final notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **MARINe_LTM_phototransect_conversion.ipynb** - Jupyter Notebook containing the conversion code for photoplot and phototransect percent cover data. **This is the final notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **MARINe_CBS_pointcontact_conversion.ipynb** - Jupyter Notebook containing the conversion code for coastal biodiversity surveys of percent cover data using point contact. 

### North Coast Kelp
Code for converting the [Bull Kelp Forest Ecosystem Monitoring Database, Northern California, 1971-2019](https://search.dataone.org/view/urn%3Auuid%3A41177927-92dc-421a-b8eb-d28f71537d96) (monitoring team led by Laura Rogers-Bennett) dataset to a DwC archive, and for running QC tests before re-uploading to DataONE. Note that Marine Lebrec worked on this dataset, building from existing code that Diana had started, which live in the old_notebooks/ directory. 
- **north_coast_kelp_DWC_conversion.ipynb** - Jupyter Notebook containing code for QC'ing and pre-processing counts, size, % algae, and % habitat type tables, and converting to a DwC archive with an event core. 
**This is the final notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**

### PISCO
Code for converting [PISCO](http://www.piscoweb.org/) survey data to DwC ([archived on DataONE](https://opc.dataone.org/view/doi%3A10.25494%2FP6%2FMLPA_kelpforest.5))
- **PISCO_add_absence_records.ipynb** - Jupyter Notebook where I developed and tested code to populate absence records in the PISCO fish and swath transect data, which they store as a presence-only data set
- **PISCO_fish_transect_conversion.ipynb** - Jupyter Notebook containing code to convert the fish transect data through 2018 to DwC
- **PISCO_fish_transect_conversion_20210816.ipynb** - Jupyter Notebook containing code to convert the fish transect data through 2020 to DwC. **This is the final fish transect notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **PISCO_fish_transect_notes.ipynb** - Jupyter Notebook where I developed and tested code to extract sex and age information from the notes field in the PISCO fish transect data
- **PISCO_sizefreq_conversion.ipynb** - Jupyter Notebook containing code to convert the size frequency data through 2018 to DwC
- **PISCO_sizefreq_conversion_20210816.ipynb** - Jupyter Notebook containing code to convert the size frequency data through 2020 to DwC. **This is the final sizefreq notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **PISCO_swath_and_upc_conversion.ipynb** - Jupyter Notebook containing initial swath transect conversion code
- **PISCO_swath_and_upc_conversion_20210816.ipynb** - Jupyter Notebook containing code to convert the swath transect data through 2020 to DwC. **This is the final swath notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **PISCO_swath_and_upc_conversion_draft2.ipynb** - Jupyter Notebook containing code to convert the swath transect data through 2018 to DwC

### Reef Check
Code for converting [Reef Check California](https://www.reefcheck.org/california-program/) survey data to DwC ([fish](https://opc.dataone.org/view/doi%3A10.25494%2FP6JS3M), [invertebrate](https://opc.dataone.org/view/doi%3A10.25494%2FP69885), [algae](https://opc.dataone.org/view/doi%3A10.25494%2FP65K5W), and [UPC data archived on DataONE](https://opc.dataone.org/view/doi%3A10.25494%2FP6F30N))
- **ReefCheck_abalone_size_conversion.ipynb** - Jupyter Notebook containing conversion code for abalone size data. **This is the final abalone size notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **ReefCheck_invasives_conversion.ipynb** - Jupyter Notebook containing conversion code for invasive algae presence/absence data. **This is the final invasive algae notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **ReefCheck_inverts_conversion.ipynb** - Jupyter Notebook containing conversion code for invertebrate transect data. **This is the final transect data notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**
- **ReefCheck_kelp_conversion.ipynb** - Jupyter Notebook containing conversion code for algae transect data. 
- **ReefCheck_urchin_size_conversion.ipynb** - Jupyter Notebook containing conversion code for sea urchin size data. **This is the final urchin size notebook that was uploaded to Axiom's Research Workspace. Additional changes to the code have been made on that platform.**

### Sandy Beaches
Code for converting data from the Sandy Beaches monitoring program led by researchers at UCSB (baseline North Coast, North Central Coast, and South Coast data archived on DataONE, but not yet publicly available as of September 2021)
- **LTER_data.ipynb** - Jupyter Notebook containing an exploration and description of survey data from a single LTER site that overlaps with the larger sandy beaches methods and study areas

### Other files
**Sampling_effort_by_MPA.ipynb** - Jupyter Notebook where I started developing code to quantify how many surveys had been conducted at each MPA accross LTM groups

**Standardizing_place_names_GTGN.ipynb** - Jupyter Notebook containing some initial code that I'm hoping to develop into a tutorial on querying [GTGN] for biological data managers

**WoRMS.py** - Python module containing functions for querying the [World Register of Marine Species (WoRMS) REST API](http://www.marinespecies.org/rest/)

## Links to completed Darwin Core Archives on [OBIS](https://obis.org/)
**CCFRP** - CCFRP declined to have data submitted to OBIS

**Reef Check** - [Fish, invertebrate, algae, and UPC transect data](https://obis.org/dataset/cfceb150-bbe2-4efb-8682-14cfc7167e7c)

## Links to entries in [CeNCOOS](https://data.cencoos.org/) and [MBON](https://mbon.ioos.us/) data catalogues
**CCFRP** 
- Fish abundance and CPUE ([CeNCOOS](https://data.cencoos.org/#module-metadata/e2685d37-f661-4e47-b55f-47890ef243d6/0d895d62-3aa1-4b6a-b2ec-e7e12aab74f8), [MBON](https://mbon.ioos.us/#module-metadata/e2685d37-f661-4e47-b55f-47890ef243d6/0d895d62-3aa1-4b6a-b2ec-e7e12aab74f8))

**Reef Check** 
- Fish, invertebrate, and algae transect data, abalone and sea urchin size data, and invasive algae presence/absence data ([CeNCOOS](https://data.cencoos.org/#module-metadata/10b12afd-c2d4-410b-bff1-c94ca0b71a24/43a6cb45-1c97-477c-8977-805d4910c2ea), [MBON](https://mbon.ioos.us/#module-metadata/10b12afd-c2d4-410b-bff1-c94ca0b71a24))

**MARINe** 
- Long-Term Monitoring Surveys: Transects and Photoplots ([CalOOS](https://data.caloos.org/#module-metadata/dbd06ba8-024a-498b-b1c5-45ffb3e76022), [MBON](https://mbon.ioos.us/#module-metadata/dbd06ba8-024a-498b-b1c5-45ffb3e76022))
- Sea Stars and Katharina along the Pacific coast from Alaska to Mexico, 1992 - 2021 ([CalOOS](https://data.caloos.org/#module-metadata/eb29d751-8534-4869-a920-030566f903fa/0736dd24-89c2-4880-a824-4a862d199062), [MBON](https://mbon.ioos.us/#module-metadata/eb29d751-8534-4869-a920-030566f903fa/0736dd24-89c2-4880-a824-4a862d199062))
