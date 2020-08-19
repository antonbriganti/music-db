import sys
from tinydb import TinyDB, Query
from csv_helper import CSVHandler

def format_release_data(filename):
    data = CSVHandler().convert_csv_to_dict(filename)
    for entry in data:
        entry['Genre'] = [genre.strip() for genre in entry['Genre'].split("/")]
    return data

def update_db(data, table):
    for release in data:
        if not release_already_in_db(release, table):
            table.insert(release)

def release_already_in_db(release, table):
    Release = Query()
    return len(table.search(Release.Release == release["Release"])) > 0


if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        source_file = sys.argv[1]
        print("loading", source_file)
        release_data = format_release_data(source_file)

        # intialise db
        print("intialising db") 
        db = TinyDB('music.json')
        release_db_table = db.table('releases')

        # update db
        print("updating db")
        update_db(release_data, release_db_table)
    
    