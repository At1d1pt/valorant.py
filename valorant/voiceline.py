from .exceptions import BadFormat, NotFound

class VoicelineSet:
    def __init__(self, raw) -> None:
        self.raw = raw

    @property
    def min_duration(self):
        return self.raw['minDuration']

    @property
    def max_duration(self):
        return self.raw['maxDuration']

    @property
    def ids(self):
        x = []
        for line in self.raw['mediaList']:
            x.append(line['id'])

        return x

    def get_voice_line(self , _id: int, audio_format: str):
        audio_format = audio_format.lower()
        f_ = {
            'wwise': 'wwise',
            'wave': 'wave',
            'wem': 'wwise',
            'wav': 'wave'
        }

        if audio_format not in f_:
            raise BadFormat("Expected ['wwise' , 'wave' , 'wem' , 'wav'] as the format for voiceline. Recieved '{}' instead".format(audio_format))
        else:
            if _id not in self.ids:
                raise NotFound("Voiceline with id '{}' not found in this voice line set.".format(_id))
            else:
                return self.raw['mediaList'][self.ids.index(_id)][f_[audio_format]]