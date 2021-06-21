import os
from pydub import AudioSegment

def convert_ogg(path):
    # os.chdir(path)
    # audio_files = os.listdir()
    # list = []
    if os.path.exists(path):
        file_dirs = sorted(os.listdir(path))
        for dir in file_dirs:
            if os.path.isdir(path + dir):
                files = os.listdir(path + dir)
                if not os.path.exists("data/converted_audio/" + dir):
                    os.makedirs("data/converted_audio/" + dir)
                for file in files:
                    name, ext = os.path.splitext(file)
                    if ext != ".ogg":
                        print("Skipping " + dir + "/" + file)
                        continue
                    # if ext == ".ogg":
                    print("Converting " + dir + "/" + file)
                    ogg_sound = AudioSegment.from_ogg(path + dir + "/" + file)
                    # rename them using the old name + ".wav"
                    ogg_sound.export("data/converted_audio/" + dir + "/" + name + ".wav", format="wav")
                print("Finished convert " + dir + ".")


if __name__ == '__main__':
    convert_ogg('data/train_short_audio')

