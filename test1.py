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
media1  = MP3("gggggg")
print(media1.type)
