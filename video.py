import vlc
from time import sleep

vidPlayer = Instance.media_player_new()
vidMedia = Instance.media_new('testvid.fileextention')
vidPlayer.set_media(vidMedia)
vidplayer.play()

sleep(10)
