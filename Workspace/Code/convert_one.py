import xarray as xr
import pandas as pd
import os
import netCDF4


def netcdf_to_csv(file_path, file_name):
    print('converting:')
    netcdf_file = xr.open_dataset(file_path).to_dataframe()
    netcdf_file = netcdf_file[['longitude', 'latitude', 'temperature', 'climatology']]
    print(netcdf_file)

    # print(netcdf_file)
    # Replace null values with zero
    # netcdf_file = netcdf_file.where(netcdf_file == None, 0)

    netcdf_file.to_csv(file_name + '.csv')


# df = nc.to_dataframe()

if __name__ == '__main__':
    netcdf_to_csv('Complete_TAVG_EqualArea.nc', 'temperatures')
