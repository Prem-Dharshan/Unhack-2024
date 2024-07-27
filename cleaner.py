import csv
import os
import shutil
import tempfile

def clean_cell(cell):
    cleaned = cell.strip()
    cleaned = ' '.join(cleaned.split())
    cleaned = cleaned.replace(',', '.')
    
    try:
        return float(cleaned)
    except ValueError:
        return None

def clean_csv(input_file_path):
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        temp_file_path = temp_file.name
        csv_reader = csv.reader(open(input_file_path, mode='r', newline=''))
        csv_writer = csv.writer(temp_file)

        for row in csv_reader:
            cleaned_row = [clean_cell(cell) for cell in row]
            csv_writer.writerow(cleaned_row)
    
    shutil.copy(temp_file_path, input_file_path)
    
    os.remove(temp_file_path)

input_file_path = './Dataset-0/Sample/Input/CareAreas.csv'

clean_csv(input_file_path)

print(f"Cleaned CSV has been written to {input_file_path}")
