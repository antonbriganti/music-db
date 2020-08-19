from csv_helper import CSVHandler
import sys

def format_release_data(filename):
    data = CSVHandler().convert_csv_to_dict(filename)
    for entry in data:
        entry['Genre'] = [genre.strip() for genre in entry['Genre'].split("/")]
    return data

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        source_file = sys.argv[1]
        print("loading", source_file)
        release_data = format_release_data(source_file)
    
    