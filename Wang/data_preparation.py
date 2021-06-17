import os
from pydub import AudioSegment

def convert1(path):
    # Change working directory
    os.chdir(path)
    audio_files = os.listdir()

    for file in audio_files:
        # spliting the file into the name and the extension
        name, ext = os.path.splitext(file)
        if ext == ".ogg":
            ogg_sound = AudioSegment.from_ogg(file)
            # rename them using the old name + ".wav"
            ogg_sound.export("{0}.wav".format(name), format="wav")

def delete_ogg(path):
    dir_name = path
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".ogg"):
            os.remove(os.path.join(dir_name, item))


if __name__ == '__main__':
    convert1('data/train_short_audio/aldfly')
     # delete_ogg('data/train_short_audio/aldfly')

