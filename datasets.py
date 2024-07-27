import pandas as pd


care_area_column_names = ['id', 'x1', 'x2', 'y1', 'y2']

meta_data_types = {
    'Main Field Size': float,
    'Sub Field size': float
}

care_area_data_types = {
    'id': int,
    'x1': float,
    'x2': float,
    'y1': float,
    'y2': float
}

sample_meta_data_file_path = './Dataset-0/Sample/Input/metadata.csv'
sample_care_area_file_path = './Dataset-0/Sample/Input/CareAreas.csv'

dataset_0_meta_data_file_path = './Dataset-0/1st/metadata.csv'
dataset_0_care_area_file_path = './Dataset-0/1st/CareAreas.csv'

# dataset_1_meta_data_file_path = './Dataset-1/2nd/metadata.csv'
# dataset_1_care_area_file_path = './Dataset-1/2nd/CareAreas.csv'

# dataset_2_meta_data_file_path = './Dataset-1/3rd/metadata.csv'
# dataset_2_care_area_file_path = './Dataset-1/3rd/CareAreas.csv'

# dataset_3_meta_data_file_path = './Dataset-1/4th/metadata.csv'
# dataset_3_care_area_file_path = './Dataset-1/4th/CareAreas.csv'

# dataset_4_meta_data_file_path = './Dataset-1/5th/metadata.csv'
# dataset_4_care_area_file_path = './Dataset-1/5th/CareAreas.csv'

# dataset_5_meta_data_file_path = './Dataset-1/6th/metadata.csv'
# dataset_5_care_area_file_path = './Dataset-1/6th/CareAreas.csv'


def convert_to_types(df, types):
    for column, dtype in types.items():
        df[column] = pd.to_numeric(df[column], errors='coerce')
        if dtype == int:
                df[column] = df[column].fillna(0).astype(dtype)
        else:
            df[column] = df[column].astype(dtype)
    return df


sample_meta_data_df = pd.read_csv(sample_meta_data_file_path, dtype=float)
sample_care_area_df = pd.read_csv(sample_care_area_file_path, header=None, names=care_area_column_names, dtype=str)

dataset_0_meta_data_df = pd.read_csv(dataset_0_meta_data_file_path, dtype=float)
dataset_0_care_area_df = pd.read_csv(dataset_0_care_area_file_path, header=None, names=care_area_column_names, dtype=str)

# dataset_1_meta_data_df = pd.read_csv(dataset_1_meta_data_file_path, dtype=str)
# dataset_1_care_area_df = pd.read_csv(dataset_1_care_area_file_path, header=None, names=care_area_column_names, dtype=str)

# dataset_2_meta_data_df = pd.read_csv(dataset_2_meta_data_file_path, dtype=str)
# dataset_2_care_area_df = pd.read_csv(dataset_2_care_area_file_path, header=None, names=care_area_column_names, dtype=str)

# dataset_3_meta_data_df = pd.read_csv(dataset_3_meta_data_file_path, dtype=str)
# dataset_3_care_area_df = pd.read_csv(dataset_3_care_area_file_path, header=None, names=care_area_column_names, dtype=str)

# dataset_4_meta_data_df = pd.read_csv(dataset_4_meta_data_file_path, dtype=str)
# dataset_4_care_area_df = pd.read_csv(dataset_4_care_area_file_path, header=None, names=care_area_column_names, dtype=str)

# dataset_5_meta_data_df = pd.read_csv(dataset_5_meta_data_file_path, dtype=str)
# dataset_5_care_area_df = pd.read_csv(dataset_5_care_area_file_path, header=None, names=care_area_column_names, dtype=str)


sample_meta_data_df = convert_to_types(sample_meta_data_df, meta_data_types)
sample_care_area_df = convert_to_types(sample_care_area_df, care_area_data_types)

dataset_0_meta_data_df = convert_to_types(dataset_0_meta_data_df, meta_data_types)
dataset_0_care_area_df = convert_to_types(dataset_0_care_area_df, care_area_data_types)

# dataset_1_meta_data_df = convert_to_types(dataset_1_meta_data_df, meta_data_types)
# dataset_1_care_area_df = convert_to_types(dataset_1_care_area_df, care_area_data_types)

# dataset_2_meta_data_df = convert_to_types(dataset_2_meta_data_df, meta_data_types)
# dataset_2_care_area_df = convert_to_types(dataset_2_care_area_df, care_area_data_types)

# dataset_3_meta_data_df = convert_to_types(dataset_3_meta_data_df, meta_data_types)
# dataset_3_care_area_df = convert_to_types(dataset_3_care_area_df, care_area_data_types)

# dataset_4_meta_data_df = convert_to_types(dataset_4_meta_data_df, meta_data_types)
# dataset_4_care_area_df = convert_to_types(dataset_4_care_area_df, care_area_data_types)

# dataset_5_meta_data_df = convert_to_types(dataset_5_meta_data_df, meta_data_types)
# dataset_5_care_area_df = convert_to_types(dataset_5_care_area_df, care_area_data_types)


__all__ = [
    'sample_meta_data_df', 'sample_care_area_df',
    'dataset_0_meta_data_df', 'dataset_0_care_area_df',
    # 'dataset_1_meta_data_df', 'dataset_1_care_area_df',
    # 'dataset_2_meta_data_df', 'dataset_2_care_area_df',
    # 'dataset_3_meta_data_df', 'dataset_3_care_area_df',
    # 'dataset_4_meta_data_df', 'dataset_4_care_area_df',
    # 'dataset_5_meta_data_df', 'dataset_5_care_area_df'
]
