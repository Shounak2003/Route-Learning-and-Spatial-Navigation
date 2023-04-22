import viz
import vizcam
import vizproximity
import vizinfo
import vizinput
import vizact
import viztask
import time
import vizshape
# This is the trigger for Start point, it is sending signal to Biopac
#import serial

viz.setMultiSample(4)
viz.fov(60)
viz.go(viz.FULLSCREEN)
viz.MainView.collision(viz.OFF)
viz.go()
viz.clearcolor(viz.SKYBLUE)


#Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(viz.ON)

subject='default'

#Prompt for the participant's identification number.
subject = vizinput.input('Kindly enter your participation number')

#confimation=vizinput.input('Press Enter to continue')
viz.message('Press Ok conitnue')

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

MOVE_SPEED = 5
TURN_SPEED = 60
sensorname=''
mazetype='8 junction'
mazecolor='grey'
instruct='Route Learning Experiment!!!'
x_cord=-11.63135
start_time=viz.tick()
lastsensor='Point 1'
y_cord=0
change=0
checksix=0
scenenumber=0
start =0
checknew=0
checklas=0
hitct=0
countintrial=0
outprint=1
conhit=0
twelvemaze=0
z_cord=-14.26598
move=1
i=1
#i=36
#i=20
check=0
phasenme='Training'
#phasenme='testing'
instructions=''
#car = viz.addChild('mini.osgb')
#ground = viz.addChild('Arrow Green maze.dae')

#Setting up the directional light
viz.MainView.getHeadLight().enable()
sky_light = viz.addDirectionalLight(euler=(0,1.8,0))
#sky_light.color(viz.WHITE)
sky_light.ambient([0.8]*9)
#viz.setOption('viz.lightModel.ambient',[0]*9)


    
#Initialize info box with some instructions
info = vizinfo.InfoPanel(instruct+'\n Welcome to Learning Phase of the study,\n \n  Please press SPACE BAR to disable this instruction.', align=viz.ALIGN_RIGHT_TOP, icon=False)
info.setTitle( 'General Instructions' ) #Set title text
info.addSeparator()




#Keyboard commands that modify the info box
vizact.onkeydown(' ' , info.setPanelVisible, viz.TOGGLE)


# Create score text
score_text = viz.addText('',parent=viz.ORTHO,fontSize=40)
score_text.alignment(viz.ALIGN_LEFT_TOP)
score_text.setBackdrop(viz.BACKDROP_OUTLINE)
viz.link(viz.MainWindow.LeftTop,score_text,offset=[20,-20,0])



#Create new scene
Scene7 = viz.addScene()
Scene8 = viz.addScene()
Scene9 = viz.addScene()
Scene10 = viz.addScene()
Scene11 = viz.addScene()
Scene12 = viz.addScene()
Scene13 = viz.addScene()
Scene14 = viz.addScene()
Scene15 = viz.addScene()
Scene16 = viz.addScene()
Scene17 = viz.addScene()
Scene18 = viz.addScene()
Scene19 = viz.addScene()
Scene20 = viz.addScene()
Scene21 = viz.addScene()
Scene22 = viz.addScene()
Scene23 = viz.addScene()
Scene24 = viz.addScene()
Scene25 = viz.addScene()
Scene26 = viz.addScene()
Scene27 = viz.addScene()
Scene28 = viz.addScene()
Scene29 = viz.addScene()
Scene30 = viz.addScene()
Scene31 = viz.addScene()
Scene32 = viz.addScene()
Scene33 = viz.addScene()
Scene34 = viz.addScene()
Scene35 = viz.addScene()
Scene36 = viz.addScene()
Scene37 = viz.addScene()
Scene38 = viz.addScene()
Scene39 = viz.addScene()
Scene40 = viz.addScene()
Scene41 = viz.addScene()
Scene42 = viz.addScene()
Scene43 = viz.addScene()
Scene44 = viz.addScene()
Scene45 = viz.addScene()
Scene46 = viz.addScene()
Scene47 = viz.addScene()
Scene48 = viz.addScene()
Scene49 = viz.addScene()
Scene50 = viz.addScene()
Scene51 = viz.addScene()
Scene52 = viz.addScene()
Scene53 = viz.addScene()
Scene54 = viz.addScene()
Scene55 = viz.addScene()
Scene56 = viz.addScene()
Scene57 = viz.addScene()
Scene58 = viz.addScene()
Scene59 = viz.addScene()
Scene60 = viz.addScene()
Scene61 = viz.addScene()
Scene62 = viz.addScene()
Scene63 = viz.addScene()
Scene64 = viz.addScene()
Scene65 = viz.addScene()
Scene66 = viz.addScene()
Scene67 = viz.addScene()
SceneEnd= viz.addScene()

##Adding mazes to the scene_trainning 8jn (5 nos)
##Adding mazes to the scene_trainning 8jn (5 nos)

#scene1 = viz.addChild('Models/8j maze .osgb', scene=viz.Scene1)
scene2 = viz.addChild('Models/8j maze .osgb', scene=viz.Scene2)
scene3 = viz.addChild('Models/8j maze .osgb', scene=viz.Scene3)
scene4 = viz.addChild('Models/8j maze .osgb', scene=viz.Scene4)
scene5 = viz.addChild('Models/8j maze .osgb', scene=viz.Scene5)
scene6 = viz.addChild('Models/8j maze .osgb', scene=viz.Scene6)
##Adding mazes to the scene_Learning 6jn (15 nos) with arrow

scene7 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene7)
scene8 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene8)
scene9 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene9)

scene10 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene10)
scene11 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene11)
scene12 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene12)
scene13 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene13)
scene14 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene14)
scene15 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene15)
scene16= viz.addChild('Models/6Arrow maze.osgb', scene=Scene16)
scene17 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene17)
scene18 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene18)
scene19 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene19)
scene20 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene20)
scene21 = viz.addChild('Models/6Arrow maze.osgb', scene=Scene21)

##Adding mazes to the scene_Learning  12jn (15 nos)with arrow

scene22 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene22)
scene23 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene23)
scene24 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene24)

scene25 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene25)
scene26 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene26)
scene27 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene27)
scene28 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene28)
scene29 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene29)
scene30 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene30)
scene31 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene31)
scene32 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene32)
scene33 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene33)
scene34 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene34)
scene35 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene35)
scene36 = viz.addChild('Models/12Arrow maze.osgb', scene=Scene36)



sky_light.addParent(viz.WORLD, scene=SceneEnd)


#Duplicating all the object created for scene 1 to scene 2
sky_light.addParent(viz.WORLD, scene=viz.Scene2)
sky_light.addParent(viz.WORLD, scene=viz.Scene3)
sky_light.addParent(viz.WORLD, scene=viz.Scene4)
sky_light.addParent(viz.WORLD, scene=viz.Scene5)
sky_light.addParent(viz.WORLD, scene=viz.Scene6)
sky_light.addParent(viz.WORLD, scene=Scene7)
sky_light.addParent(viz.WORLD, scene=Scene8)
sky_light.addParent(viz.WORLD, scene=Scene9)
sky_light.addParent(viz.WORLD, scene=Scene10)
sky_light.addParent(viz.WORLD, scene=Scene11)
sky_light.addParent(viz.WORLD, scene=Scene12)
sky_light.addParent(viz.WORLD, scene=Scene13)
sky_light.addParent(viz.WORLD, scene=Scene14)
sky_light.addParent(viz.WORLD, scene=Scene15)
sky_light.addParent(viz.WORLD, scene=Scene16)
sky_light.addParent(viz.WORLD, scene=Scene17)
sky_light.addParent(viz.WORLD, scene=Scene18)
sky_light.addParent(viz.WORLD, scene=Scene19)
sky_light.addParent(viz.WORLD, scene=Scene20)
sky_light.addParent(viz.WORLD, scene=Scene21)
sky_light.addParent(viz.WORLD, scene=Scene22)
sky_light.addParent(viz.WORLD, scene=Scene23)
sky_light.addParent(viz.WORLD, scene=Scene24)
sky_light.addParent(viz.WORLD, scene=Scene25)
sky_light.addParent(viz.WORLD, scene=Scene26)
sky_light.addParent(viz.WORLD, scene=Scene27)
sky_light.addParent(viz.WORLD, scene=Scene28)
sky_light.addParent(viz.WORLD, scene=Scene29)
sky_light.addParent(viz.WORLD, scene=Scene30)
sky_light.addParent(viz.WORLD, scene=Scene31)
sky_light.addParent(viz.WORLD, scene=Scene32)
sky_light.addParent(viz.WORLD, scene=Scene33)
sky_light.addParent(viz.WORLD, scene=Scene34)
sky_light.addParent(viz.WORLD, scene=Scene35)
sky_light.addParent(viz.WORLD, scene=Scene36)
sky_light.addParent(viz.WORLD, scene=Scene37)
sky_light.addParent(viz.WORLD, scene=Scene38)
sky_light.addParent(viz.WORLD, scene=Scene39)
sky_light.addParent(viz.WORLD, scene=Scene40)
sky_light.addParent(viz.WORLD, scene=Scene41)
sky_light.addParent(viz.WORLD, scene=Scene42)
sky_light.addParent(viz.WORLD, scene=Scene43)
sky_light.addParent(viz.WORLD, scene=Scene44)
sky_light.addParent(viz.WORLD, scene=Scene45)
sky_light.addParent(viz.WORLD, scene=Scene46)
sky_light.addParent(viz.WORLD, scene=Scene47)
sky_light.addParent(viz.WORLD, scene=Scene48)
sky_light.addParent(viz.WORLD, scene=Scene49)
sky_light.addParent(viz.WORLD, scene=Scene50)
sky_light.addParent(viz.WORLD, scene=Scene51)
sky_light.addParent(viz.WORLD, scene=Scene52)
sky_light.addParent(viz.WORLD, scene=Scene53)
sky_light.addParent(viz.WORLD, scene=Scene54)
sky_light.addParent(viz.WORLD, scene=Scene55)
sky_light.addParent(viz.WORLD, scene=Scene56)




view = viz.MainView
#0.35,-1.2,0.2

def addevent():
    global check
    global sensorname
    global checknew
    global i
    
    if check==1:
        ser = serial.Serial('COM4', 115200, timeout=1)
        if ((sensorname=='Point 4' and (i==21 or i==51)) or (sensorname=='Point 2' and i==36) or (sensorname=='Point 3' and i==6)) :
          ser.write(str.encode('01'))
          ser.write(str.encode('01'))
        elif ((sensorname=='Point 4' and i>36 and i<=51) or (sensorname=='Point 2' and i>=52 and i<=66) or (sensorname=='Point 4' and i>=6 and i<=21) or sensorname=='Point 2' or (sensorname=='Point 3' and i<=5) or (sensorname=='Point 1' and i==1) )  :
        
            ser.write(str.encode('01'))
            
        elif checknew==1 and i>=7:
            ser.write(str.encode('02'))
            checknew=0
            
        elif checknew==2 and i>=7:
            ser.write(str.encode('05'))
            checknew =0
        ser.write(str.encode('00'))
 
        
        
        ser.close()
    
vizact.ontimer(0,addevent)


def updatecar():

    global x_cord
    global y_cord
    global z_cord
    global check 
    global move
    #print(car.getEuler(),view.getEuler())
    
    pass
    if viz.key.isDown(viz.KEY_UP):
        
            #while move==0:
                view.move([0,0,MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
                z_cord=z_cord-MOVE_SPEED*viz.elapsed()
                if viz.key.isDown(viz.KEY_DOWN):
                    move=1
                #print(check)
           # move=0

    elif viz.key.isDown(viz.KEY_DOWN):
       
            view.move([0,0,-MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
            z_cord=z_cord+MOVE_SPEED*viz.elapsed()
        


    elif viz.key.isDown(viz.KEY_RIGHT):
        view.setEuler([TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
        x_cord=x_cord-MOVE_SPEED*viz.elapsed()
        

        print(x_cord)
    elif viz.key.isDown(viz.KEY_LEFT):
        view.setEuler([-TURN_SPEED*viz.elapsed(),0,0],viz.BODY_ORI,viz.REL_PARENT)
        x_cord=x_cord+MOVE_SPEED*viz.elapsed()
        

        print(x_cord)
    elif viz.key.isDown(viz.KEY_BACKSPACE):
        print(x_cord)
        print(z_cord)
    elif viz.key.isDown(viz.KEY_TAB) : 
       #car.setPosition([0.35,-1.2,0.2],viz.REL_LOCAL)
        #MainView.setPosition([0,0,0],viz.REL_LOCAL)     
        view.move([0,0,z_cord*5],viz.BODY_ORI)
        #view.setPosition([0.35,-1.2,0.2],viz.REL_LOCAL)
        view.setEuler([x_cord*5,0,0],viz.BODY_ORI,viz.REL_PARENT)
       
        print(view.getPosition())
   

#[-11.63135, 0.00000, -14.26598]
vizact.ontimer(0,updatecar)
def checkpos():
        global sensorname
        global check
        global phasenme
        #global checknew
        global hitct
        global conhit
        global change
        global checklas
        global checksix
        global twelvemaze
        global i
        global mazetype
        global mazecolor
        global instruct
        #if i==7:
         #   instruct='Welcome to the Learning phase\n'
          #  vizinfo.InfoPanel(' \n'+phasenme+' \n'+str(i), align=viz.ALIGN_LEFT_TOP, icon=False)
            #Keyboard commands that modify the info box
           # vizact.onkeydown(' ' , info.setPanelVisible, viz.TOGGLE)
        #elif i==37:
         #   instruct='Welcome to the Test phase\n'
          #  vizinfo.InfoPanel(' \n'+phasenme+' \n'+str(i), align=viz.ALIGN_LEFT_TOP, icon=False)
           # vizact.onkeydown(' ' , info.setPanelVisible, viz.TOGGLE)
       # else:
            #instruct=''
            #vizinfo.InfoPanel(instruct+'\nThe radio button changes the color.\n\n'+phasenme+' of Vampires gruhhh ', align=viz.ALIGN_RIGHT_TOP, icon=False)
        if i<=6:
            phasenme='Training'
            mazetype='8 junction'
        elif i<=21:
            phasenme='learning'
            
            mazetype='6 junction'
        elif i<=36:
            phasenme='learning'
            mazetype='12 junction'
        elif i<=51:
            phasenme='testing'
            mazetype='6 junction'
        else:
            phasenme='testing'
            mazetype='12 junction'
        if check==1:
             print(check)#phasenme=='testing' or 
             
             if ((sensorname=='Point 4' and i>36 and i<=51) or (sensorname=='Point 2' and i>=52 and i<=66)     ) and conhit<=2 and i>36:
                print('entered')
                i=i+1
                if i==7 or i==11 or i==16 or i==18 or i==20 or i==22 or i==25 or i==28 or i==30 or i==32 or i==38 or i==41 or i==43 or i==44 or i==46 or i==49 or i==51 or i==52 or i==55 or i==58 or i==60 or i==63  or i==65 or i==66:
                    mazecolor='No Image'
                elif i==9 or i==13 or i==15 or i==19 or i==21 or i==24 or i==26 or i==29 or i==33 or i==35 or i==37 or i==39 or i==40 or i==42 or i==45 or i==47 or i==48 or i==50 or i==53 or i==54 or i==56 or i==57 or i==59 or i==61 or i==62 or i==64:
                    mazecolor='No Image'
               # i=i+1
                #Reset the head's orientation and position.  
                viz.MainView.reset( viz.HEAD_ORI | viz.BODY_ORI ) 
                #Set the main viewpoint's position andorientation. 
                viz.MainView.setPosition(0,1.8,0) 
                #Set the current position and orientation as point to reset to. 
                viz.cam.setReset() 
                #Reset the head's orientation and position.  
                #viz.MainWindow.setScene(i)
                print("conhit"+str(conhit))
                print("hitct"+str(hitct))
                check=0
                if hitct==0 and conhit<2 :
                    conhit=conhit+1
                    checklas=1
                    #i=i+1
                    viz.MainWindow.setScene(i)
                    UpdateScore()
                    hitct=0
                elif hitct>0 and conhit<2:
                    if checksix==1:
                        conhit=0
                        i=37
                        hitct=0
                        checklas=1
                        change=1
                        viz.MainWindow.setScene(i)
                        UpdateScore()
                    elif checksix==2:
                        conhit=0
                        i=52
                        hitct=0
                        change=2
                        checklas=1
                        viz.MainWindow.setScene(i)
                        UpdateScore()
                elif hitct==0 and conhit==2 and twelvemaze==1 and checksix==2:
                    viz.quit()
                elif hitct==0 and conhit==2 and twelvemaze==0 and checksix==1:
                    twelvemaze=1
                    checksix=2
                    conhit=0
                    checklas=1
                    i=52
                    viz.MainWindow.setScene(i)
                    UpdateScore()
                print("conct"+str(conhit))
                print("Scene 2 ")
             #elif ((sensorname=='Point 4' and i>=6 and i<=21) or sensorname=='Point 2' or (sensorname=='Point 3' and i<=5) or (sensorname=='Point 1' and i==1)  )  :
             elif ((sensorname=='Point 4' and i>6 and i<=21) or sensorname=='Point 2' or (sensorname=='Point 3' and i<=6) or (sensorname=='Point 1' and i==1) )  :
                print('entered new')
                #if i==1:
                  #viz.waitTime(3)
                #   vizact.onkeydown('m',i=1)
                 #yield viztask.waitTime(1)
                i=i+1
                if i==2:
                    i=7
                if i==11:
                    i=20 
                elif i==27:
                   i=35
                elif i==36:
                    viz.quit()
                if i==8 or i==10 or i==12 or i==14 or i==17 or i==23 or i==27 or i==31 or i==34 or i==36 or i<=6:
                    mazecolor='No Image'
                elif i==7 or i==11 or i==16 or i==18 or i==20 or i==22 or i==25 or i==28 or i==30 or i==32 or i==38 or i==41 or i==43 or i==44 or i==46 or i==49 or i==51 or i==52 or i==55 or i==58 or i==60 or i==63  or i==65 or i==66:
                    mazecolor='No Image'
                elif i==9 or i==13 or i==15 or i==19 or i==21 or i==24 or i==26 or i==29 or i==33 or i==35 or i==37 or i==39 or i==40 or i==42 or i==45 or i==47 or i==48 or i==50 or i==53 or i==54 or i==56 or i==57 or i==59 or i==61 or i==62 or i==64:
                    mazecolor='No Image'
                elif i<=6:
                    mazecolor='grey'
                #else:
                 #   mazecolor='grey'

                #i=i+1
                #Reset the head's orientation and position.  
                viz.MainView.reset( viz.HEAD_ORI | viz.BODY_ORI ) 
                #Set the main viewpoint's position andorientation. 
                viz.MainView.setPosition(0,1.8,0) 
                #Set the current position and orientation as point to reset to. 
                viz.cam.setReset() 
                #Reset the head's orientation and position.  
                #viz.MainWindow.setScene(i)
                print("conhit"+str(conhit))
                print("hitct"+str(hitct))
                checklas=1
                check=0
                viz.MainWindow.setScene(i)
                UpdateScore()
                         
                
vizact.ontimer(0,checkpos)

def UpdateScore():
    global phasenme
    global i
    global change
    global checksix
    global countintrial
    phase=phasenme
    if i==1:
        countintrial=0
    elif i<=6:
        countintrial=countintrial+1
    
        
    elif i<=36:
        if i==7:
            countintrial=1
            phase='learning'
        elif i==35:
            phase =phase+'\nAfter this scene please contact\nthe Research Scholar for Test phase \n '
            countintrial=countintrial+1
            
        else:
            countintrial=countintrial+1
    elif i<=67:
        if i==37 or change ==1 or change==2:
            countintrial=1
            checksix=1
            if change ==1:
             countintrial=1
             change=0
            elif change==2:
              countintrial=4
              checksix=2
              change=0
            else:
               countintrial=1
               checksix=1

            phase='testing'
        else:
            countintrial=countintrial+1
    """Update score text"""
    message=phase+' '+str(countintrial)
    score_text.message(message)
#vizact.ontimer(0,UpdateScore)


def AddSensor(shape,name):
    sensor = vizproximity.Sensor(shape,None)
    sensor.name = name
    manager.addSensor(sensor)

#Add circle area-1
#shape = vizproximity.CircleArea(1,center=(0,0,0))
#AddSensor(shape,'Point 1')

#Add circle area-1
shape = vizproximity.CircleArea(1.50,center=(0, 0.0, 0.0))
AddSensor(shape,'Point 1')

#Add circle area-2 for 12 junction maze
shape = vizproximity.CircleArea(1.5,center=(49.92780,11.5))
AddSensor(shape,'Point 2')

#Add circle-3 for 8 junction maze
shape = vizproximity.CircleArea(1.6,center=([25,46.2]))
AddSensor(shape,'Point 3')
#[25.06053, -0.00000, 45.71175]
#[25.08167, 0.04844, 46.30223]

#Add circle area-2 for 6 junction maze
shape = vizproximity.CircleArea(1.6,center=([12.1,33.65]))
AddSensor(shape,'Point 4')


###Decession Sensor


# Add decision -1
shape = vizproximity.RectangleArea([2.50,0.76],center=(-0.08558,  6.72581))
AddSensor(shape,'D1')

# Add decision -2
shape = vizproximity.RectangleArea([0.75,2.50],center=(10.73, 8.75))
AddSensor(shape,'D2')

# Add decision -3
shape = vizproximity.RectangleArea([2.50,0.77],center=(12.428, 19.56))
AddSensor(shape,'D3')

# Add decision -4
shape = vizproximity.RectangleArea([0.75,2.50],center=(1.5000004, 21.2356607))
AddSensor(shape,'D4')

#[1.26964, 0.05475, 21.60507]

# Add decision -5
shape = vizproximity.RectangleArea([2.50,0.77],center=(-0.08558, 32.15134))
AddSensor(shape,'D5')

# Add decision -6
#shape = vizproximity.RectangleArea([0.75,2.50],center=(11.11229, 33.79))
#AddSensor(shape,'D6')

# Add decision -7
shape = vizproximity.RectangleArea([2.50,0.77],center=(12.428, 44.56191))
AddSensor(shape,'D7')


# Add decision -8
#shape = vizproximity.RectangleArea([0.75,2.50],center=(23.14845, 46.26))
#AddSensor(shape,'D8')



# Add decision -9
shape = vizproximity.RectangleArea([2.50,0.77],center=(24.9333, 35.40143))
AddSensor(shape,'D9')


# Add decision -10
shape = vizproximity.RectangleArea([0.75,2.50],center=(35.7833,33.69996))
AddSensor(shape,'D10')
#[35.53633, 0.51731, 32.88237]

# Add decision -11
shape = vizproximity.RectangleArea([2.50,0.77],center=(37.437290,22.72167))
AddSensor(shape,'D11')

# Add decision -12
shape = vizproximity.RectangleArea([0.75,2.50],center=(48.20161,21.246789994))
AddSensor(shape,'D12')


#.....Hitting wall---



# Add Hit -01
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([-0.1, 2.70612, 10.00000])
Box.alpha(.01)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(-0.1,1.51, 10.00000))
AddSensor(shape,'H1')


 
# Add Hit -02
Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([-1.36, 1.51, 8.78873])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(-1.36, 1.51, 8.78873))
AddSensor(shape,'H2')



# Add Hit -03
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([12.125411, 1.51, 7.39507])
Box.alpha(.01)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(12.49411, 1.51, 7.4679))
AddSensor(shape,'H3')

# Add Hit -04
Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([13.698, 1.51, 21.298561])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(13.698, 1.51, 21.298561))

AddSensor(shape,'H4')

# Add Hit -05
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([12.39411, 1.51, 22.74680])
Box.alpha(.5)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(12.39411, 1.51, 22.74680))
AddSensor(shape,'H5')





# Add Hit -06
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([-0.1, 1.51, 20.0])
Box.alpha(.01)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(-0.1, 1.51, 20.0))
AddSensor(shape,'H6')

# Add Hit -07

Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([-1.31922, 1.51, 33.75967])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(-1.31922, 1.51, 33.75967))

AddSensor(shape,'H7')

# Add Hit -08
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([12.39411, 1.51, 32.4680])
Box.alpha(.5)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(12.39411, 1.51, 22.74680))
AddSensor(shape,'H8')




# Add Hit -09
Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([13.7234, 1.51, 33.75967])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(13.7234, 1.51, 33.75967))
AddSensor(shape,'H9')


# Add Hit -10
Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([11.11, 1.51, 46.26])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(11.11, 1.51, 46.26))
AddSensor(shape,'H9')

# Add Hit -11
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([24.90, 1.51, 47.52040])
Box.alpha(.01)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(24.90, 1.51, 47.52040))
AddSensor(shape,'H11')

# Add Hit -12

Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([23.60274, 1.51, 33.75967])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(23.60274, 1.51, 33.75967))
AddSensor(shape,'H12')


# Add Hit -13
Box = vizshape.addBox([2.50  , 3.00 , 0.12])
Box.setPosition([37.44, 1.51, 34.95500])
Box.alpha(.01)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(37.44, 1.51, 34.95500))
AddSensor(shape,'H13')

# Add Hit -14
Box = vizshape.addBox([0.12, 3.00,2.50])
Box.setPosition([36.01, 1.51, 21.298561])
Box.alpha(.1)
shape = vizproximity.Box([0.12, 3.00,2.50],center=(36.01, 1.51, 21.298561))
AddSensor(shape,'H14')


# Add Hit -15
Box = vizshape.addBox([2.50, 3.00 , 0.12])
Box.setPosition([12.125411, 1.51, 7.39507])
Box.alpha(.01)
shape = vizproximity.Box([2.50  , 3.00 , 0.12],center=(49.86366, 1.51, 22.4979))
AddSensor(shape,'H15')



# Opens file 'response.txt' in write mode
fileins = open('Responses/Learning and Training/'+subject+' response in '+'.csv', 'w')
fileouts = open('Responses/Learning and Training/'+subject+'response out '+'.csv', 'w')
#fileouts = open(subject+'responseforout'+'.csv', 'w')


# Register callbacks for proximity sensors
def EnterProximity(e):
    global check
    global start_time
    global i
    global hitct
    global subject
    global conhit
    global sensorname
    global checknew
    global start
    #global checklas
    global mazetype
    global outprint
    global lastsensor
    global mazecolor
    global phasenme
    sensorname=e.sensor.name
    time=viz.tick()-start_time
    
    if i==1:
        info='Participation ID- '+','+subject+'\n'+'Point 2'+' -'+'12 Junction'+','+'Point 3'+' -'+'8 Junction'+','+'Point 4'+' -'+'6 Junction'+'\n'+'Phase'+','+'trial'  +','+'maze type' + ',' +'maze color'+ ','+ 'Hit'+','+'status in'+','+ 'Time in'+'\n'
        #info = 'Phase'+','+'trial'  +','+'maze type' + ',' +'maze color'+ ','+ 'Hit'+','+'status in'+','+ 'Time in'+'\n'
        #checklas=0
        outprint=4
    
    elif sensorname=='H1' or sensorname=='H2' or sensorname=='H3' or sensorname=='H4' or sensorname=='H5' or sensorname=='H6' or sensorname=='H7' or sensorname=='H8' or sensorname=='H9' or sensorname=='H10' or sensorname=='H11' or sensorname=='H12' or sensorname=='H13' or sensorname=='H14' or sensorname=='H15':
        hitct=hitct+1
        # Play sound once 
        viz.playSound('boing!.wav')
        checknew=1
       # checklas=0
        if e.sensor.name!=lastsensor:
            #info = 'N/A' + ',' +'Collided with'+ e.sensor.name+','+ 'in' +str(i) +','+ 'on'+phasenme+','+'Yes'+',''\n'
            info = ''+phasenme+','+'' +str(i-1) +',' +mazetype+','+ mazecolor+','+'1'+','+'Collided with '+ e.sensor.name+','+','+','+'N/A'+'\n'
            outprint=1
        else:
            outprint=0
    elif sensorname=='Point 1':
        #info ='on'+phasenme+','+ 'in' +str(i-2)+','+ str(time) + ',' +'Exited'+ mazetype+','+' '+','+' '+',' + ' '+'\n'
        info=''
        #checklas=0
        outprint=9
    else:
        info = ''+phasenme+','+'' +str(i-1) +',' +mazetype+','+ mazecolor+','+'0'+','+'Inside '+ e.sensor.name+','+str(time)+'\n'
        #checklas=0
        checknew=2
        outprint =1
    lastsensor=e.sensor.name
    print('Entered',e.sensor.name)
    print(e.sensor.name)
    check=1
    # Write the string to the output file
    fileins.write(info)
    # Makes sure the file data is really written to the harddrive
    fileins.flush()
    print(info)
        
def ExitProximity(e):
    global start_time
    global i
    global phasenme
    global lastsensor
    global subject
    global mazecolor
    global checklas
    global mazetype
    global outprint
    end=viz.tick()-start_time
    global check
    check =0


    if outprint==0:
        #info ='on'+phasenme+','+ 'in' +str(i-2)+','+ str(time) + ',' +'Exited'+ mazetype+','+' '+','+' '+',' + ' '+'\n'
        info=''
    
    elif outprint==4:
        #info='Phase'+','+'trial'  +','+'status out' + ',' +'maze color'+ ','+ 'maze type'+','+'Hit'+','+ 'Time out'+'\n'
        info='Participation ID- '+','+subject+'\n'+'Phase'+','+'trial'  +','+'maze type' + ',' +'maze color'+ ','+ 'Hit'+','+'status out'+','+ 'Time out'+'\n'
    #elif checklas==1:
     #  info='New Scene'+','+''  +','+'' + ',' +''+ ','+ ''+','+''+','+ ''+'\n'
      # checklas=0
    elif i>=2 and e.sensor.name=='Point 1':
       info=''

    else:
       # info = str(end) + ',' +'Outside '+ e.sensor.name+ ','+ '' +str(i-1)+','+ ''+phasenme+'\n'
        #info = ''+phasenme+','+'' +str(i-1) +',' +'Outside '+ e.sensor.name+','+ mazecolor+','+mazetype+','+ ''+','+str(end)+'\n'
        info = ''+phasenme+','+'' +str(i-1) +',' +mazetype+','+ mazecolor+','+'0'+','+'Outside '+ e.sensor.name+','+str(end)+'\n'
    # Write the string to the output file
    fileouts.write(info)
    # Makes sure the file data is really written to the harddrive
    fileouts.flush()
    print(info)
    print('Exited',e.sensor)

manager.onEnter(None, EnterProximity)
manager.onExit(None, ExitProximity)


viz.mouse.setVisible(True)