#https://pyautogui.readthedocs.io/en/latest/mouse.html


#import win32api, win32con
import pyautogui
from PIL import ImageChops
import os
import time
import imgcompare as ic
from PIL import ImageGrab, Image
from win10toast import ToastNotifier

steps = [] #'mine', 'claim', 'checked', 'approve', 'mininghub'
toast = ToastNotifier()


class Step:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    name = ''
    mpos = (0,0)


mine = Step()
mine.x1 = 1186
mine.y1 = 1240
mine.x2 = 1357
mine.y2 = 1288
mine.name = 'mine'
mine.mpos = (1268,1268)
steps.append(mine)

claim = Step()
claim.x1 = 1000
claim.y1 = 882
claim.x2 = claim.x1 + 150
claim.y2 = claim.y1 + 40
claim.name = 'claim'
claim.mpos = (1060,898)  #(1016,688)
steps.append(claim)

checked = Step()
checked.x1 = 167
checked.y1 = 757
checked.x2 = 188
checked.y2 = 778
checked.name = 'checked'
checked.mpos = (182,770)
#steps.append(checked)

approve = Step()
approve.x1 = 256
approve.y1 = 732
approve.x2 = 400
approve.y2 = 769
approve.name = 'approve'
approve.mpos = (338,767)
steps.append(approve)

mininghub = Step()
mininghub.x1 = 565
mininghub.y1 = 1125
mininghub.x2 = 902
mininghub.y2 =1179
mininghub.name = 'mininghub'
mininghub.mpos = (749,1162)
steps.append(mininghub)




def screenGrab():
    time.sleep(5)
    #i_mine=ImageGrab.grab(bbox=(1139,1216,1403,1306))
    #i_claim=ImageGrab.grab(bbox=(649,480,1881,976))
    
    i_checkedbox=ImageGrab.grab(bbox=(166,682,199,712))

    #i_approve=ImageGrab.grab(bbox=(10,10,500,500))


    #i_mininghub=ImageGrab.grab(bbox=(516,1101,982,1236))

    #box = ()  #box = (157,346,796,825)

    im = ImageGrab.grab()
  
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

    im=i_checkedbox
    im.save('approvedone.png')

    #image_one = Image.open('C:\\Users\\tosun\\Desktop\\allienpy\\im.png')
    #image_one =ImageGrab.open('C:\\Users\\tosun\\Desktop\\allienpy\\im.png')
    #image_one =Image.open('cl.png')
    #aaaa = ic.is_equal(im,image_one)
    #print(aaaa)


    

    #image_one = Image.open('./1.png')
    #image_two = Image.open('./2.png')

    #diff = ImageChops.difference(image_one, image_two)



    #print(im.getpixel(Cord.f_shrimp))
    #print(ImageChops.difference(im, imtest))



def printscreen(step):
    time.sleep(2)
    screen = ImageGrab.grab(bbox=(step.x1,step.y1,step.x2,step.y2))
    screen.save(step.name + '.png')

def compare_image(st):
    i_step = Image.open(st.name + '.png')  
    result = False
    print(st.name + ' comparing...')
    while (result == False):
        i_now = ImageGrab.grab(bbox=(st.x1,st.y1,st.x2,st.y2))
        result = ic.is_equal(i_step,i_now)
        time.sleep(3)
        if (result == True):
            print(st.name + ' image is equal')
        else:
            print(st.name + ' image is not equal')




#'mine', 'claim', 'checked', 'approve', 'mininghub'
def d_step(st):
    compare_image(st)
    pyautogui.moveTo(st.mpos) #st.mpos
    time.sleep(.1)
    pyautogui.click()
    time.sleep(.1)


def lc():
    i = 0
    while i < 5:
        #msg = str(i) + '. || waiting for ' + steps[i].name
        #toast.show_toast("Allien Worlds", msg, duration=3,icon_path="next.ico")
        d_step(steps[i])
        print('step -> ' + steps[i].name)
        i = i+1
        if (i == 5):
            i = 0


 
def main():
    lc()
    #printscreen(claim)


if __name__ == '__main__':
    main()