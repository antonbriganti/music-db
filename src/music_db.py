from tinydb import TinyDB, Query

def load_releases(database_name):
    db = TinyDB(database_name)
    release_db_table = db.table('releases')
    return release_db_table

def update_releases(release_data, releases_table):
    for release in release_data:
        if not __release_already_in_db(release, releases_table):
            releases_table.insert(release)

def __release_already_in_db(release, table):
    Release = Query()
    return len(table.search(Release.Release == release["Release"])) > 0
