# music-db
a project designed to convert my "music listened to" spreadsheets into some kind of usable database format 

# inspiration for the project
I've been tracking what music I listen to in spreadsheets since 2017, and I've always been interested in the statistics that comes from it. I've got some formulas going on to give neat breakdowns on how many albums/EPs/mixtapes I give a "must listen" rating to, how many releases I listened to came out that year, stuff like that. 

but as I've been doing this longer, I've wanted to find out to more about the music I listen to. I know I listen to a lot of rap, but what would the next most popular genre be? what's the gender ratio of artists I listen to? is there a particular year where I just think all music that came out in that year wasn't very good?

some of that is doable with the spreadsheet formulas, but others require more data. I could add that into the spreadsheet but the reason why I began to track what I listen to in a spreadsheet was because it was super simple. adding more data would complicate it and also not look very nice. so what's the next best idea?

# goal 
the goal of the project is to create some kind of database where I can import my music spreadsheets and also begin to track extra data that isn't present in the source spreadsheets. doing this will also allow me to run more specific queries that can target a wider amount of information, and I can also hopefully automate some of the data collection by pointing to existing web APIs. 

## input csv format 
```
Release,Artist,Genre,Rating,Release Type
Yes Lawd!,NxWorries,R&B,good,Album
anemone EP (アネモネEP),the peggies,J-Pop Rock,great,EP/Mixtape
```