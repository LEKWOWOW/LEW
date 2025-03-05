class Media:
    def __init__(self,name,type):
        self.__name = name
        self.__type = type
    @property
    def name(self):
        return self.__name 
    @property
    def type(self):
        return self.__type

class FLAC(Media):
    def __init__(self,name):
        super().__init__(name,type = "flac")
class MP3(Media):
    def __init__(self,name):
        super().__init__(name,type = "mp3")
class AAC(Media):
    def __init__(self,name):
        super().__init__(name,type ="aac")
class Podcast():
    def __init__(self,chanel_name,host_name,type):
        self.__chanel_name = chanel_name
        self.__host_name = host_name
        self.__type = type
        self.__episode = []
    @property
    def add_episode(self,episode):
        self.__episode.append(episode)
    @property
    def chanel_name(self):
        return self.__chanel_name
    @property
    def host_name(self):
        return self.__host_name
    @property
    def type(self):
        return self.__type
    @property
    def episode(self):
        return self.__episode
class MediaList:
    def __init__(self):
        self.__media_list = []
    def add_media_list(self,media):
        self.__media_list.append(media)
    @property
    def media_list(self):
        return self.__media_list
    
class Playlist(MediaList):
    def __init__(self,playlist_name):
        super().__init__()
        self.__playlist_name = playlist_name
    def add_song(self,media):
        super().add_media_list(media)
    def seach_id(self,name):
        for i in super().media_list:
            if i.name == name:
                return i.name
playlist1 = Playlist("ee")
playlist1.add_song(FLAC("song1"))
g = playlist1.seach_id("song1")



    