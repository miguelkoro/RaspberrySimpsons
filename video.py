import os
import random
from subprocess import PIPE, Popen, STDOUT

def elegirEpisodio():
    randomfile = random.choice(os.listdir("/home/pi/simpsonstv/videos/encoded"))
    file = os.path.join('/home/pi/simpsonstv/videos/encoded', randomfile)
    playProcess = Popen(['omxplayer', '--aspect-mode', 'fill', file])
    playProcess.wait()

#while (True):
    #elegirEpisodio()
elegirEpisodio()
