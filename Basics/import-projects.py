from unpacking import albums
while True:
    # print("please select a movie ")
    # for index,value in enumerate (albums):
    #     movie,country,year,song_list = value
    #     print("{}: {} {} {} {}".format(index + 1,movie,country,year,song_list))
    # print()
    # for index,(movie, country, year, song_list) in enumerate (albums):
    #     print("{}: {} {} {} {}".format(index, movie, country, year, song_list))
    # break
    print("Movie list")
    for index,value in enumerate (albums):
        movie,country,year,song_list = value
        print("{}: {}".format(index + 1,movie))
    choice = int(input("select a movie: "))
    if 1<= choice <= len(albums):
        songs_list = albums[choice-1][3]
        print(songs_list)
    for index, (song) in enumerate (songs_list):
        print(index+1,song)
    song_to_play = int(input("select a song: "))
    print("="*80)
    print("{} is playing".format(songs_list[song_to_play-1]))

    break
