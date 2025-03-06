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
    def play(self):
        pass
class MP3(Media):
    def __init__(self,name,):
        super().__init__(name,type ="mp3")
class Flac(Media):
    def __init__(self,name):
        super().__init__(name,type ="flac")
class AAC(Media):
    def __init__(self,name):
        super().__init__(name,type = "aac")
class Pocast:
    def __init__(self,channel_name,host_name):
        self.__channel_name = channel_name
        self.__hosta_name = host_name
        self.__episode = []
    def add_episode(self,episode):
        self.__episode.append(episode)
    @property
    def episode(self):
        return self.__episode
class MediaList:
    def __init__(self):
        self.__media_list = []
    @property
    def media_list(self):
        return self.__media_list
    def add_media(self,media):
        self.__media_list.append(media)
class Playlist(MediaList):
    def __init__(self,name):
        super().__init__()
        self.__name = name
    @property
    def name(self):
        return self.__name 
    def add_song(self,media):
        super().add_media(media)
class Album(MediaList):
    def __init__(self,name_album,artist_name):
        super().__init__()
        self.__name = name_album
        self.__artist = artist_name
    def add_song(self,media):
        super().add_media(media)
    @property
    def artist(self):
        return self.__artist
    
    @property
    def name(self):
        return self.__name
class MusicPlay:
    def __init__(self):
        self.__podcast_list = []
        self.__album_list=[]
        self.__playlist = []
    @property
    def podcast_list(self):
        return self.__podcast_list
    def play_podcast(self,podcast):
        pass
    def add_album(self,album):
        self.__album_list.append(album)
    def add_podcast_list(self,podcast):
        self.__podcast_list.append(podcast)
    def add_playlist(self,playlist):
        self.__playlist.append(playlist)      
    def seach__playlist_by_name(self,name):
        for  e in self.__album_list:
            for i in self.__playlist:
                    for j in i.media_list:
                        if i.name.lower() == name.lower() or j.name.lower() == name.lower() or e.name.lower() == name.lower() or e.artist.lower() == name.lower():
                            return (f"ชิ่อPlaylist😊:{i.name} ชื่อเพลง {j.name} ประเภทไฟลท์👌: {j.type} ชื่ออัลบัม 😊{e.name} ชื่อ ศิลปิน {e.artist}")
                        return "ไท่พบเพลลิส"
    def seach__album_by_name(self):
        
     pass
def create_instant():
    mp3 = MP3("แค่เอาคืน")
    aac = AAC("sefeZone")
    pla = Playlist("เพลงจากsuffic")
    poscast1 = Pocast("ชั่งมันเถอะ","ใครก็ได้")
    poscast1.add_episode('1')
    album1 = Album("เพลงไทย","lookhmee 💕 Sonya")
    pla.add_song(mp3)
    pla.add_song(aac)
    album1.add_song(aac)
    return album1,poscast1,pla

album1,poscast1,pla = create_instant()
player = MusicPlay()
player.add_album(album1)
player.add_podcast_list(poscast1)
player.add_playlist(pla)
print(player.seach__playlist_by_name("lookhmee 💕 Sonya"))



    
#     MusicPlay.add_album(album1)
#     MusicPlay.add_podcast_list(poscast1)
#     MusicPlay.add_playlist(pla)



    
    

    


    
