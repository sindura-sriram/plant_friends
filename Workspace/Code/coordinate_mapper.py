import xarray as xr
import pandas as pd
import os
import csv
import re
import reverse_geocoder as rg

def coordinate_to_location(coords):
    results = rg.search(coords)[0]
    country_code = results['cc']
    state = results['admin1']
    return country_code, state


if __name__ == '__main__':
    print(coordinate_to_location((37.7749, -122.4194)))