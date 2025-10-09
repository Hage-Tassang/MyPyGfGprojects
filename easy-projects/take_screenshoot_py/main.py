#Program to take screenshot


'''
#capture full screen
import pyscreenshot as pySshot
import time
time.sleep(2)
image = pySshot.grab()
image.show()
#save the image file
image.save('first-SS.png')

'''

#capture a part of the screen
import pyscreenshot as pySshot
import time
time.sleep(2)
# X1,Y1,X2,Y2
box = (10,10,500,500)
image = pySshot.grab(bbox=box)
image.show()
#save the image file
image.save('second-SS.png')