import xarray as xr
import pandas as pd
import numpy as np
import os
import csv
import re
from coordinate_mapper import coordinate_to_location

DATASET_DIRECTORY = 'dataset_nc4/'
CSV_DATASET_DIRECTORY = 'dataset_csv/'


def netcdf_to_csv(dataset=DATASET_DIRECTORY):
    if not os.path.exists(CSV_DATASET_DIRECTORY):
        os.mkdir(CSV_DATASET_DIRECTORY)

    subsets = list(map(lambda x: DATASET_DIRECTORY + x + '/', os.listdir(DATASET_DIRECTORY)))
    # print(subsets)

    for subset in subsets:
        crop = subset.split('/')[-2]
        subset_path = CSV_DATASET_DIRECTORY + crop + '/'

        # print(subset_path)
        if not os.path.exists(subset_path):
            os.mkdir(subset_path)

        data_files = list(map(lambda x: subset + x, os.listdir(subset)))

        for path in data_files:
            file_name = path.split('/')[-1].split('.')[-2]
            # print(file_name)
            csv_path = subset_path + file_name + '.csv'
            print(csv_path)

            netcdf_file = xr.open_dataset(path).to_dataframe()
            # Replace null values with zero
            netcdf_file = netcdf_file.fillna(0)
            # netcdf_file['index'] = netcdf_file.index
            # print(netcdf_file.columns)
            # netcdf_file = netcdf_file.rename(index={'lat':'Latitude', 'lon':'longitude'})
            # netcdf_file.columns = [['latitude', 'longitude', 'yield']]
            # netcdf_file = netcdf_file[['longitude', 'latitude', 'yield']]

            netcdf_file.to_csv(csv_path)


# df = nc.to_dataframe()

def text_to_csv(dataset):
    csv_directory = 'temperature_dataset_csv/'
    if not os.path.exists(csv_directory):
        os.mkdir(csv_directory)

    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))
    print(temp_data)

    for path in temp_data:
        # new_path = path.replace('.', '_') + '.txt'
        #
        # os.rename(path, new_path)

        # add_line(path, 'longitude latitude jan feb mar apr may jun jul aug sep oct nov dec')

        # file_in = open(path, 'r+')
        # file_out = open(path + '.bak', 'w')
        #
        # for line in file_in:
        #     file_out.write(re.sub(' +', ' ', line.lstrip()))
        #
        # os.remove(path)
        # os.rename(path + '.bak', path)
        #
        # print(path)

        csv_path = csv_directory + path.split('/')[-1].split('.')[-2] + '.csv'

        input_text = csv.reader(open(path), delimiter=' ')

        out_file = csv.writer(open(csv_path, 'w'))

        out_file.writerows(input_text)


def add_line(file, string):
    temp = file + '.bak'

    with open(file, 'r') as main_file, open(temp, 'w') as write_file:
        write_file.write(string + '\n')

        for line in main_file:
            write_file.write(line)

    os.remove(file)
    os.rename(temp, file)


def add_average_col(dataset):
    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))

    for path in temp_data:
        print(path)

        csv_input = pd.read_csv(path)
        csv_input['average_temp'] = csv_input[
            ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']].mean(axis=1)

        csv_input.to_csv(path)


def fix_longitude(dataset):
    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))

    for path in temp_data:
        print(path)

        csv_input = pd.read_csv(path)
        csv_input['longitude'] = csv_input['longitude'] - 180

        csv_input.to_csv(path)


def filter_country_loc_temp(dataset):
    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))

    for path in temp_data:
        print(path)

        csv_input = pd.read_csv(path)

        # bounding box method
        # (-171.791110603, 18.91619, -66.96466, 71.3577635769)
        # so if lat is between -171.791110603 and -66.96466, &&& lon is between 18.91619 and 71.3577635769... mark as US

        longitude = csv_input['longitude']
        latitude = csv_input['latitude']

        csv_input = csv_input[csv_input['longitude'] > -124.6797351903]
        csv_input = csv_input[csv_input['longitude'] < -66.725281587]
        csv_input = csv_input[csv_input['latitude'] > 25.527664384]
        csv_input = csv_input[csv_input['latitude'] < 49.3619707027]

        csv_input.to_csv(path)


def filter_country_loc_yield(dataset):
    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))
    new_col_list = []
    subsets = list(map(lambda x: dataset + x + '/', os.listdir(dataset)))
    # print(subsets)

    for subset in subsets:
        crop = subset.split('/')[-2]
        subset_path = dataset + crop + '/'

        # print(subset_path)

        data_files = list(map(lambda x: subset + x, os.listdir(subset)))

        for path in data_files:
            file_name = path.split('/')[-1].split('.')[-2]
            # print(file_name)
            csv_path = subset_path + file_name + '.csv'

            csv_input = pd.read_csv(csv_path)

            csv_input = csv_input[csv_input['longitude'] > -124.6797351903]
            csv_input = csv_input[csv_input['longitude'] < -66.725281587]
            csv_input = csv_input[csv_input['latitude'] > 25.527664384]
            csv_input = csv_input[csv_input['latitude'] < 49.3619707027]

            csv_input.to_csv(csv_path)

            print(csv_path)


def assign_country_to_loc_temp(dataset):
    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))

    for path in temp_data:
        print(path)

        csv_input = pd.read_csv(path)

        # coordinate search method
        csv_input['state'] = csv_input.apply(lambda row: coordinate_to_location((row['longitude'], row['latitude'])), axis=1)[0]

        csv_input.to_csv(path)


def assign_country_to_loc_yield(dataset):

        data_files = list(map(lambda x: dataset + x, os.listdir(dataset)))

        for path in data_files:
            file_name = path.split('/')[-1].split('.')[-2]
            # print(file_name)
            csv_path = path
            print(csv_path)

            csv_input = pd.read_csv(csv_path)
            csv_input['state'] = csv_input.apply(lambda row: convert_to_location(row['latitude'], row['longitude']), axis=1)
            # csv_input = csv_input.apply(lambda row: convert_to_location(row['latitude'], row['longitude']), axis=1)
            # print(csv_input)
            csv_input.to_csv(csv_path)




def reformat_yield_data(dataset):
    temp_data = list(map(lambda x: dataset + x, os.listdir(dataset)))
    new_col_list = []
    subsets = list(map(lambda x: dataset + x + '/', os.listdir(dataset)))
    # print(subsets)

    for subset in subsets:
        crop = subset.split('/')[-2]
        subset_path = dataset + crop + '/'

        # print(subset_path)

        data_files = list(map(lambda x: subset + x, os.listdir(subset)))

        for path in data_files:
            file_name = path.split('/')[-1].split('.')[-2]
            # print(file_name)
            csv_path = subset_path + file_name + '.csv'

            csv_input = pd.read_csv(csv_path)
            # if val >= 180, subtract 360. for some reason.
            csv_input['longitude'] = csv_input['longitude'].where(csv_input['longitude'] < 180, csv_input['longitude'] - 360)

            csv_input.to_csv(csv_path)

            print(csv_path)


def rename_reorder(dataset):
    subsets = list(map(lambda x: dataset + x + '/', os.listdir(dataset)))
    # print(subsets)

    for subset in subsets:
        crop = subset.split('/')[-2]
        subset_path = 'yield_' + CSV_DATASET_DIRECTORY + crop + '/'

        # print(subset_path)
        if not os.path.exists(subset_path):
            os.mkdir(subset_path)

        data_files = list(map(lambda x: subset + x, os.listdir(subset)))

        for path in data_files:
            file_name = path.split('/')[-1].split('.')[-2]
            # print(file_name)
            csv_path = subset_path + file_name + '.csv'
            # print("read path: " + path)
            #
            print("write path: " + csv_path)

            csv_input = pd.read_csv(path)
            # csv_input = csv_input.drop(columns=['Unnamed: 0'])
            # print(csv_input)
            csv_input.columns = ['latitude', 'longitude', 'yield']
            csv_input = csv_input[['longitude', 'latitude', 'yield']]

            # print(csv_input.columns)

            csv_input.to_csv(csv_path)


def convert_to_location(y_coord, x_coord):
    state_names = np.empty(50, dtype=str)
    states = np.empty((50, 4), dtype=float)
    state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
                   "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
                   "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                   "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
                   "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
                   "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                   "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                   "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    boxes = pd.read_csv('state_boxes.csv')

    for index, row in boxes.iterrows():
        val_list = [row.xmin, row.xmax, row.ymin, row.ymax]
        states[index] = val_list


    for i in range(len(states)):
        xmin = states[i][0]
        xmax = states[i][1]
        ymin = states[i][2]
        ymax = states[i][3]
        if (xmin <= x_coord <= xmax) and (ymin <= y_coord <= ymax):

            state = state_names[i]
            print(state)
            return state

    print('no state found')
    # return 'no state'


def concat_data(dataset):
    subsets = list(map(lambda x: dataset + x + '/', os.listdir(dataset)))

    for subset in subsets:
        crop = subset.split('/')[-2]
        subset_path = dataset + crop + '/'
        print(subset_path)

        if not os.path.exists(subset_path):
            os.mkdir(subset_path)

        data_files = list(map(lambda x: subset + x, os.listdir(subset)))



        dataframes = []
        first = True

        for path in data_files:
            file_name = path.split('/')[-1].split('.')[-2]
            # print(file_name)
            # print("read path: " + path)
            year = file_name.split('_')[2]
            if first:
                dataframe = pd.read_csv(path)
                first_year = year
                first = False
            else:
                dataframe = dataframe.join(pd.read_csv(path), rsuffix="_" + year)

        dataframe.rename(columns={'average_temp': 'average_temp_' + first_year}, inplace=True)

        write_path = 'concatenated_temp/temp.csv'
        print(write_path)
        dataframe.to_csv(write_path)

def get_relevant_data(dataset):
    data_files = list(map(lambda x: dataset + x, os.listdir(dataset)))

    col_list = ['latitude', 'longitude', 'state']

    for i in range(1981, 2015):
        col_list.append("average_temp_" + str(i))

    # print(col_list)
    #
    for path in data_files:

        df = pd.read_csv(path)

        clean_df = df[col_list]

        write_path = 'clean_temp/' + path.split('/')[1]
        print(write_path)
        clean_df.to_csv(write_path)


def join_datasets(table_path, dataset):
    temp = pd.read_csv(table_path)
    temp = temp.set_index(['latitude', 'longitude'])
    data_files = list(map(lambda x: dataset + x, os.listdir(dataset)))

    for path in data_files:
        plant_yield = pd.read_csv(path)
        plant_yield = plant_yield.set_index(['latitude', 'longitude'])

        # print(plant_yield)
        # print(temp)

        joined = plant_yield.join(temp, how='inner' ,rsuffix='0')

        print(path.split('/')[1])

        write_path = 'final_tables/' + path.split('/')[1]

        joined = joined.drop(columns=['Unnamed: 0', 'Unnamed: 00'])

        joined.to_csv(write_path)


def filter_states(dataset):
    data_files = list(map(lambda x: dataset + x, os.listdir(dataset)))

    for path in data_files:

        df = pd.read_csv(path)
        df = df.dropna()

        df = df.drop(columns='Unnamed: 0')

        df.to_csv(path)



if __name__ == '__main__':
    # join_datasets('clean_temp/temp.csv', 'clean_yield/')
    assign_country_to_loc_yield('extra_tables/')
    filter_states('extra_tables/')
