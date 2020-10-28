import vlc
from time import sleep
import threading
from threading import Thread




class VideoPlayer:
	def videoPlayerPlay(self):
		
		vlcInstance = vlc.Instance()
		player = vlcInstance.media_player_new()
		player.set_media(vlc.Media("IMG_1114.mp4"))
		player.play()
		
		
		
		
		
		#vidPlayer = vlc.MediaPlayer()
		#vidPlayer.set_fullscreen(True)

		#video = vlc.Media("IMG_1114.mp4")
		#vidPlayer.set_media(video)
		#vidPlayer.play()
		sleep(0.1)

		while (player.is_playing()) == 1:
			sleep(0.3)
			
			
			
	def videoThread(self):
		print("Start Thread")
		Thread.start(self.videoPlayerPlay)
		print("HEYO")



#need to adjust volume?

