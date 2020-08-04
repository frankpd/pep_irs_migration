import os
from time import sleep

directory='images'
printer=''
    
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        thepath=os.path.abspath(os.path.join(directory,filename))
        os.system("lpr -P {} {}".format(printer,thepath))
        print(filename,"was printed.")
        sleep(1)
    else:
        pass
