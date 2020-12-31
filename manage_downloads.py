import os
import re
import shutil

download_video_path='/home/brahim/Downloads/Video'
key_words=['Arduino','Django','PUBG','EgyBest','Spring','ENSAM']
pattern = re.compile(r"\((\d+)\)")


def rename_youtube_shity_preffix(download_video_path , pattern=pattern):
    os.chdir(path=download_video_path)
    for file in os.listdir():
        if pattern.findall(file):
            new_file=file.replace(f'({pattern.findall(file)[0]})','').strip()
            print(new_file)
            os.rename(file,new_file)

def create_dirs(dir_name,download_video_path):
    if dir_name in os.listdir(download_video_path):
        return False
    os.mkdir(os.path.join(download_video_path , dir_name))
    return True

def  move_files(download_video_path,key_words):
    os.chdir(path=download_video_path)
    for file in os.listdir():
        if not os.path.isdir(file):
            for key_word in key_words :
                if key_word in file :
                    create_dirs(key_word,download_video_path)
                    shutil.move(os.path.join(download_video_path,file),os.path.join(download_video_path,key_word,file))


if __name__ == '__main__' :
    rename_youtube_shity_preffix(download_video_path=download_video_path)
    move_files(download_video_path=download_video_path , key_words=key_words)
