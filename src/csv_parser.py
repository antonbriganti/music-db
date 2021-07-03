import csv

def format_release_data(filename):
    data = __convert_csv_to_dict(filename)
    for entry in data:
        entry['Genre'] = [genre.strip() for genre in entry['Genre'].split("/")]
    return data

def __convert_csv_to_dict(self, filename):
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        csv_rows = [dict(row) for row in csv_reader]
    return csv_rows
