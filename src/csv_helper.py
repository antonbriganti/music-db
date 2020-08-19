import csv
class CSVHandler:
    def convert_csv_to_dict(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            csv_rows = [dict(row) for row in csv_reader]
        return csv_rows
