import csv
from pandas import read_csv
from typing import Tuple
from datasets import sample_meta_data_df, sample_care_area_df

def get_area(x1, x2, y1, y2):
    return abs(x1 - x2) * abs(y1 - y2)

def main() -> None:
    MFS = sample_meta_data_df['Main Field Size'].values[0]
    SFS = sample_meta_data_df['Sub Field size'].values

    MFS_coords = []
    SFS_coords = []
    
    print(MFS, SFS)

    for row in sample_care_area_df.itertuples(index=True):
        id, x1, x2, y1, y2 = getattr(row, "id"), getattr(row, "x1"), getattr(row, "x2"), getattr(row, "y1"), getattr(row, 'y2')

        if (MFS * MFS >= get_area(x1, x2, y1, y2)):
            print(f'MFS covers {id}')

            ix1, ix2, jy1, jy2 = x1, x1 + SFS[0], y1, y1 + SFS[0]

            MFS_coords.append([id, x1, x1 + MFS, y1, y1 + MFS])
            # print(MFS_coords)

            sfs_index = 0

            while ((ix2 <= x2  and jy1 <= y2 ) and (ix1 >= x1 and y1 >= y1)):

                while (ix1 <= x2):

                    SFS_coords.append(
                        [sfs_index, ix1, ix1 + SFS[0], jy1, jy2, id]
                    )
                    # print([sfs_index, ix1, ix1 + SFS[0], jy1, jy2, id])
                    
                    ix1 += SFS[0]
                    sfs_index += 1
                    
                # jy1 += SFS[0]
                # jy2 += SFS[0]

                while (ix1 > x1):

                    SFS_coords.append(
                        [sfs_index, ix1, ix1 - SFS[0], jy1, jy1 + SFS[0], id]
                    )
                    # print([sfs_index, ix1, ix1 - SFS[0], jy1, jy1 + SFS[0], id])
                   
                    ix1 -= SFS[0]
                    sfs_index += 1

                jy1 += SFS[0]
                jy2 += SFS[0]


    with open('subfields.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Index', 'X1', 'X2', 'Y1', 'Y2', 'ID'])
        writer.writerows(SFS_coords)

    print("Subfields CSV has been written to subfields.csv")


    with open('mainfields.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(MFS_coords)

    print("Mainfields CSV has been written to mainfields.csv")

if __name__ == '__main__':
    main()


#  .\Validator.exe "D:\KLA-Unhack-2024\Validator\Validator\Students" "D:\KLA-Unhack-2024\Validator\Validator\Results"