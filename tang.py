class Media:
    def __init__(self, name, type):
        self.__name = name
        self.__type = type
        
    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type
    

class Mp3(Media):
    def __init__(self, name):
        super().__init__(name, type = 'MP3')


class Frac(Media):
    def __init__(self, name):
        super().__init__(name, type = 'Flac')

class Aac(Media):
    def __init__(self, name):
        super().__init__(name, type = 'AAC')


class podcast:
    def __init__(self,  name, name_chennel, host_name):
        self.__name = name
        self.__name_chennel = name_chennel
        self.__host_name = host_name
        self.__episode = []
    
    
    def add_episode(self, episode):
        return self.__episode.append(episode)
    
    @property
    def episode(self):
        return self.__episode

class MediaList:
    def __init__(self):
        self.__media_list = []
        
    def add_media(self, media):
        self.__media_list.append(media)
    
    @property
    def media_list(self):
        return self.__media_list
    


        

class PlayList(MediaList):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        
    def add_song(self, media):
        super().add_media(media)
        
       
    def read_str(self, name):
        for i in super().media_list:
            if i.name.lower() == name.lower():
                return i.name   

class Album(MediaList):
    def __init__(self,  name, artist):
        super().__init__()
        self.__name = name
        self.__artist = artist
        
    @property    
    def name(self):
        return self.__name
    @property
    def artist(self):
        return self.__artist
    
    def add_song(self, song):
        super().add_media(song)

class MusicPlayer:
    def __init__(self):
        self.__album_list = []
        self.__podcast_chennel_list = []
        self.__playlist = []
        
    @property    
    def add_playlist(self, playlist):
        pass 
    
    def add_podcast(self, podcast):
        pass

    def album_list(self, album):
        pass


        
aac = Aac("Jack")
pla = PlayList("tang")
pla.add_song(aac)

al1 = Album("Kiss for love", "Kin-ji-yeon")
al1.add_song(aac)
for i in al1.media_list:
    print(i.name)