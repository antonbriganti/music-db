from csv_helper import CSVHandler

def convert_spreadsheet_to_dict(filename):
    data = CSVHandler().convert_csv_to_dict(filename)
    for entry in data:
        entry['Genre'] = [genre.strip() for genre in entry['Genre'].split("/")]
    return data

if __name__ == "__main__":
    source_file = "input.csv"
    release_data = convert_spreadsheet_to_dict(source_file)
    
    