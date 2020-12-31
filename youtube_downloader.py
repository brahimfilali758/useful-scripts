from pytube import YouTube , Playlist
import os
import sys



#TODO : (done) if the file does already exist , skip it
#TODO : (done) pick within the streams one that has video and audio both
#TODO : pick the resolution 720p in first , if it doesn't exist , pick the highest one (480p 360p ..) priority to above
#TODO : having the status of the download
#TODO : (done) pass in the playlist_URL as an argument to the file (with sys)
#TODO : (done) pass in the resolution (not necesseserly)

#TODO : clean your code by making a class PlaylistDownloader

def main(arg):
    playlists_directory = '/home/brahim/Videos'
    if len(arg) > 1 :
        playlist_URL = arg[1]
    else :
        playlist_URL = 'https://www.youtube.com/watch?v=sWFAo_Qjm14&list=PLrAjkmIig4HSEVpMTe8GsKi2SWsUdRpAF'
    if len(arg) > 2 :
        resolution = arg[2]
    else :
        resolution = '480p'

    playlist = Playlist(playlist_URL)
    directory_path = os.path.join(playlists_directory , playlist.title)

    print(directory_path)

    # os.chdir(playlists_directory)

    if not os.path.exists(directory_path) :
        try:
            os.mkdir(directory_path)
        except OSError as e:
            print(e)

    print(playlist)
    for video in playlist.videos :
        print('info')
        video_path = os.path.join(directory_path , video.title)
        if not os.path.exists(video_path) :
            # print(f'Downloading :  {video.title}')
            # print(type(video.streams.filter(progressive=True).order_by('resolution').desc()))
            [print(stream) for stream in video.streams.filter(progressive=True).order_by('resolution').desc()]

            print('*******************************************')
            # video.streams.filter(progressive=True).first().download(directory_path)
        else :
            print(f' === >  This file already exists : {video.title} ')


if __name__ == '__main__' :
    # print(sys.argv)
    main(sys.argv)
