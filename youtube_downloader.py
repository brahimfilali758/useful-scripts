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
#TODO : if the resolution is only 360p the download audio and video separeted and the merge them with ffmpeg


class PlaylistDownloader(Playlist):


    def __init__(self, playlist_URL ,playlists_directory_path=None , directory_name=None):
        super().__init__(playlist_URL)
        self.playlist_URL = playlist_URL
        if playlists_directory_path :
            self.playlists_directory_path = playlists_directory_path
        else :
            self.playlists_directory_path = '/home/brahim/Videos'
        if directory_name :
            self.directory_name = directory_name
        else :
            self.directory_name = self.title

        print(f' the playlists path : {self.playlists_directory_path} the directory_name is {self.directory_name} ' )

    def create_directory(self):
        directory_path=os.path.join(self.playlists_directory_path,self.directory_name)
        if not os.path.exists(directory_path):
            try:
                os.mkdir(directory_path)
            except OSError as e:
                print(e)


    def download_playlist(self):
        self.create_directory()
        for video in self.videos:
            video_path = os.path.join(self.playlists_directory_path,self.directory_name,video.title)
            if not os.path.exists(video_path) :
                print(f'Downloading :  {video.title}')
                [print(stream) for stream in video.streams.filter(progressive=True).order_by('resolution').desc()]
                # video.streams.filter(progressive=True).first().download(directory_path)
            else :
                print(f' === >  This file already exists : {video.title} ')



if __name__ == '__main__' :
    playlist_downloader = PlaylistDownloader('https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10')
    playlist_downloader.download_playlist()
