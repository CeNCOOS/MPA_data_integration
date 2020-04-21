def get_worms_from_scientific_name(sci_name):
    """
    Using the WoRMS REST API, retrieve WoRMS ID and taxon ID given a scientific name.

    Dependencies:
        import urllib.request, urllib.parse, json

    Usage:
        get_worms_from_scientific_name(sci_name)

    Inputs:
        The scientific name of interest as a string, e.g. 'Dosidicus gigas'

    Outputs:
        1. scientificName: WoRMS specified scientific name that matched to sci_name
        2. scientificNameID: WoRMS specified ID
        3. taxonID: WoRMS specified taxon ID

    Patrick Daniels
    Small changes from Diana LaScala-Gruenewald
    2020-04-20
    Python 3.7
    """

    # Imports
    import urllib.parse
    import urllib.request
    import json

    # Create url to query
    sci_name_url = urllib.parse.quote(sci_name)
    _url = 'http://www.marinespecies.org/rest/AphiaRecordsByNames?scientificnames%5B%5D=' + sci_name_url + '&like=false&marine_only=false'

    # Try query
    try:
        with urllib.request.urlopen(_url) as url:
            data = json.loads(url.read().decode())
            return (data[0][0]['scientificname'], data[0][0]['lsid'], data[0][0]['AphiaID'])

    # If it fails, try searching for just the genus
    except Exception as e:
        if len(sci_name_url.split('%20')) > 1:
            # If species is unknown and listed as spp. or sp.
            return get_worms_from_scientific_name(sci_name_url.split('%20')[0])
        else:
            print("Url didn't work, check name, ", sci_name)


def get_worms_from_common_name(common_name):
    """
    Using the WoRMS REST API, retrieve WoRMS ID, scientific name and taxon ID given a common name.

    Dependencies:
        import urllib.request, urllib.parse, json, warnings

    Usage:
        worms_from_common_name(common_name)

    Inputs:
        The common name of interest as a string, e.g. 'Bigmouth sole'

    Outputs:
        1. scientificName: WoRMS specified scientific name
        2. scientificNameID: WoRMS specified ID
        3. taxonID: WoRMS specified taxon ID

    Diana LaScala-Gruenewald
    Based on worms_from_scientific_name by Patrick Daniels
    2020-04-20
    Python 3.7
    """

    # Imports
    import urllib.parse
    import urllib.request
    import json
    import warnings

    # Ensure name is lower case, has no trailing whitespace
    common_name = common_name.lower().strip()

    # Create url to query
    name_url = urllib.parse.quote(common_name)
    _url = 'http://www.marinespecies.org/rest/AphiaRecordsByVernacular/' + name_url + '?like=false&offset=1'

    # Try query
    try:
        with urllib.request.urlopen(_url) as url:
            data = json.loads(url.read().decode())

            # If more than one match is found, warn and return first match with status 'accepted'
            if len(data) > 1:
                warnings.warn(
                    'More than one match found for ' + common_name + '. Returning data from first match with status \'accepted\'.')

                for record in data:
                    if record['status'] == 'accepted':
                        return (record['scientificname'], record['lsid'], record['AphiaID'])
            else:
                return (data[0]['scientificname'], data[0]['lsid'], data[0]['AphiaID'])

    except Exception as e:
        print('Query wasn\'t successful, check name: ', common_name)


if __name__ == '__main__':
    pass

    # # Code for testing:
    # print('Querying scientific name...')
    # sci_name = get_worms_from_scientific_name('Sebastes carnatus')
    #
    # print('Querying common name...')
    # com_name = get_worms_from_common_name('Great white shark')
    #
    # print((sci_name, com_name))