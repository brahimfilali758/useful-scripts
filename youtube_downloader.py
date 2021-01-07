from pytube import YouTube , Playlist
import os
import sys
import subprocess
import shlex


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
        directory_path = os.path.join(self.playlists_directory_path,self.directory_name)

        for video in self.videos:
            if list(video.streams.filter(res='480p',progressive=True)) != [] :
                #This means that the video should be download in a simple way without merging audio and video
                print('This video has a stream progressive')
                print('******************')
                print('the streams are : ')
                print(video.streams.filter(res='480p' , progressive = True))
                #download the first stream of that list
                video.streams.filter(progressive=True).download(directory_path)
            else :
                #This means that there no stream with audio and video and 720p at the same time
                #So here we hava to download the video
                print('This video does not have a stream progressive')
                #differenciate between audio and video and then download both of them separately :
                audio_path = self.download_audio(youtube_video=video)
                video_path = self.download_video(youtube_video=video)
                _ , ext = os.path.splitext(video_path)
                # output_path = os.path.join(directory_path , video.title) + ext
                self.merge_audio_video(audio_path , video_path , 'output' + ext)




    def download_audio(self , youtube_video):
        audio = youtube_video.streams.filter(only_audio=True,adaptive=True).first().download('/tmp')
        base, ext = os.path.splitext(audio)
        new_audio_name = '/tmp/audio' + ext
        os.rename(audio , new_audio_name)
        return new_audio_name

    def download_video(self , youtube_video):
        video = youtube_video.streams.filter(only_video=True,adaptive=True).first().download('/tmp')
        base, ext = os.path.splitext(video)
        new_video_name = '/tmp/video' + ext
        os.rename(video , new_video_name)
        return new_video_name

    def merge_audio_video(self , audio_path , video_path , output_path) :
        command = f'ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac {output_path}'
        subprocess.Popen(shlex.split(command))



if __name__ == '__main__' :
    URL = 'https://www.youtube.com/watch?v=sWFAo_Qjm14&list=PLrAjkmIig4HSEVpMTe8GsKi2SWsUdRpAF'
    playlist_downloader = PlaylistDownloader(URL)
    playlist_downloader.download_playlist()
