import pandas as pd


import lyricsgenius


chart_list = ["Pop","R&B","Country","Hot 100"]
years= [ year for year in range(1970,1980)]
artists_list=[]
for chart in chart_list:
    document = pd.read_excel('Artists.xlsx', sheet_name=chart)
    for year in years:
        for i in range(len(document[year])):
            print(document[year][i])
            artists_list.append(document[year][i])
artists_list = list(set(artists_list))
artists_list = artists_list[1:]
print(artists_list)
print(len(artists_list))
# print(document[1970])

genius = lyricsgenius.Genius("Nwxa-R8Sbxi6jx7U3B3Jjq088VQ5CiutlLig9xq7Is8Q_Eg20RTAt1P7IpoKVjRF")
genius.verbose = False # Turn off status messages
lines = []
for artist in artists_list:
    try:
        artist_obj = genius.search_artist(artist, max_songs=5, sort="popularity")
        # print(artist_obj.songs[0].lyrics)
        # artist_obj.save_lyrics()
        print('Artist: ',artist)
        # print('Songs: '','.join(artist_obj.songs))
        line = ['70',artist]
        for song in artist_obj.songs:
            line.append(song.lyrics.replace(',','').replace('\n',' '))
        lines.append(line)
    except Exception as e:
        continue

with open('artistlyrics.csv',"w+") as fileobj:
    for line in lines:
        fileobj.write(','.join(line))

