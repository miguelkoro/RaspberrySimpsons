import os
import random
from subprocess import PIPE, Popen, STDOUT

def elegirEpisodio():
    temporada = random.randint(1,11)
    if temporada==1:
            episodio = random.randint(1,13)
    if temporada==2:
            episodio = random.randint(1,22)
    if temporada==3:
            episodio = random.randint(1,24)
    if temporada==4:
            episodio = random.randint(1,22)
    if temporada==5:
            episodio = random.randint(1,22)
    if temporada==6:
            episodio = random.randint(1,25)
    if temporada==7:
            episodio = random.randint(1,25)
    if temporada==8:
            episodio = random.randint(1,25)
    if temporada==9:
            episodio = random.randint(1,24)
    if temporada==10:
            episodio = random.randint(1,23)
    if temporada==11:
            episodio = random.randint(1,22)

    if temporada < 10:
        temporada = str(0) + str(temporada)
    if episodio < 10:
        episodio = str(0) + str(episodio)

    nombrearchivo = '~/simpsonstv/videos/encoded/"LOS SIMPSONS.S'+str(temporada)+'.E'+str(episodio)+'.mp4"'
    #print(nombrearchivo)
    #subprocess.call(["omxplayer", "--display 4", nombrearchivo])
    #os.system("omxplayer --display 4 ~/simpsonstv/videos/encoded/'LOS SIMPSONS.S"+str(temporada)+".E"+str(episodio)+".mp4'")
    playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'fill', nombrearchivo])
    playProcess.wait()

#while (True):
    #elegirEpisodio()
elegirEpisodio()
