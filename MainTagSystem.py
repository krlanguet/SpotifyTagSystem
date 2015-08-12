def databaseConstructor(tag_list = {'tag123': ('song1', 'song2', 'song3'), 'tag245': ('song2', 'song4', 'song5'), 'tag31': ('song3', 'song1')}):
    #Creates a dictionary database of songs and their tags
    song_database = {}
    print(tag_list)
    
    for current_tag in tag_list:
        for current_song in tag_list[current_tag]:
            if song_database == None:
                song_database[current_song] = [current_tag]
                continue
            for song in song_database:
                #append current_tag to current_song in song_database if there
                if song == current_song:
                    song_database[song].append(current_tag)
                    break
            else:
                #if not there, add current_song to song_database with current_tag
                song_database[current_song] = [current_tag]

    #print(song_database)

def TagConverter():
    #Creates a list of tags and their songs from text files, per user specifications
    tag_list = {}
    #tag_list = {'tag347': ('song3', 'song4', 'song7'), 'tag245': ('song2', 'song4', 'song5'), 'tag31': ('song3', 'song1'), 'tag178954': ('song1', 'song7', 'song8', 'song9', 'song5', 'song4')}

    while(1):
        current_tag = input('Please enter the name of a tag.txt file. (name.txt) Enter "q" when you are finished.\n')
        if current_tag == 'q':
            break

        current_tag_txt = open(current_tag)
        
        tag_list[current_tag] = []
        next_line = current_tag_txt.readline()
        while(next_line != ''):
            tag_list[current_tag].append(next_line)
            #print(next_line)
            next_line = current_tag_txt.readline()

    return tag_list

def main():
    databaseConstructor(TagConverter())
    
main()
