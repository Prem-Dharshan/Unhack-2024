import csv
from pandas import read_csv
from typing import List
from datasets import dataset_0_meta_data_df, dataset_0_care_area_df

def get_area(x1: float, x2: float, y1: float, y2: float) -> float:
    return abs(x1 - x2) * abs(y1 - y2)

def main() -> None:
    MFS = dataset_0_meta_data_df['Main Field Size'].values[0]
    SFS = dataset_0_meta_data_df['Sub Field size'].values[0]

    MFS_coords: List[List[float]] = []
    SFS_coords: List[List[float]] = []
    
    print(MFS, SFS)

    for row in dataset_0_care_area_df.itertuples(index=True):
        id, x1, x2, y1, y2 = row.id, row.x1, row.x2, row.y1, row.y2

        if (MFS * MFS >= get_area(x1, x2, y1, y2)):
            print(f'MFS covers {id}')

            MFS_coords.append([id, x1, x1 + MFS, y1, y1 + MFS])
            ix1, jy1 = x1, y1

            while jy1 + SFS <= y2:
                ix1 = x1
                while ix1 + SFS <= x2:
                    SFS_coords.append([len(SFS_coords), ix1, ix1 + SFS, jy1, jy1 + SFS, id])
                    ix1 += SFS
                jy1 += SFS

    with open('D:/KLA-Unhack-2024/Validator/Validator/Students/22XW54/Milestone1/subfields.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Index', 'X1', 'X2', 'Y1', 'Y2', 'ID'])
        writer.writerows(SFS_coords)

    with open('D:/KLA-Unhack-2024/Validator/Validator/Students/22XW54/Milestone1/mainfields.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'X1', 'X2', 'Y1', 'Y2'])
        writer.writerows(MFS_coords)

if __name__ == '__main__':
    main()
