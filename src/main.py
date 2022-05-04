import sys
import music_db
import csv_parser

if __name__ == "__main__":

    if (len(sys.argv) >= 2):
        # intialise db
        print("intialising db") 
        release_db_table = music_db.load_releases("music.db.json")

        # read in data from listed file
        source_file = sys.argv[1]
        print("loading", source_file)
        release_data = csv_parser.format_release_data(source_file) 

        # update db
        print("updating db")
        music_db.update_releases(release_data, release_db_table)
    
    else:
        print("missing args. try using something like")
        print("python3 src/main.py input.csv")
