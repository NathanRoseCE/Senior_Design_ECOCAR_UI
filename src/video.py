import vlc
from time import sleep

class VideoPlayer:
	def videoPlayerPlay(self):

		vidPlayer = vlc.MediaPlayer()
		vidPlayer.set_fullscreen(True)

		video = vlc.Media("../resources/vid.mp4")
		vidPlayer.set_media(video)
		vidPlayer.play()
		sleep(0.1)

		while (vidPlayer.is_playing()) == 1:
			sleep(0.3)
