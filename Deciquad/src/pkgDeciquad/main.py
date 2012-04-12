"""
main.py
The start of something
xris and Zelrok
"""


from direct.gui.DirectGui import DirectFrame, DirectButton, DirectEntry, DirectLabel
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
#from directbase.DirectStart import base

class MyApp(ShowBase):    
    def __init__(self):
        """
        Initialize the MyApp class, including defining the GUI objects and layout.
        Inherits from ShowBase.
        """
        
        # Because MyApp inherits from ShowBase, ShowBase needs to be initialized also (?) 
        ShowBase.__init__(self)
        
        # doesn't disable the mouse, only disables the default setting of the mouse controlling the camera 
        # can't import base and showbase at the same time. showbase is moreimportant right now.
        #base.disableMouse()
        
        # prints the coords of direct gui objects (DGO) when 'P' key is pressed or LMB is clicked
        self.accept("p", self.getDGOcoords)
        self.accept("mouse1", self.getDGOcoords) # only catches mouse when clicked on not gui elements >:|
                
        # add frmChatBox
        self.frmChatBox = DirectFrame(frameColor=(0, 255, 0, 1), frameSize=(-0.5, 0.5, -0.25, 0.25), pos=(0, 0, 0))
        
        ### Add some gui objects and parent them to 'frmChatBox'. They move relative to 'frmChatBox', but are positioned relative to aspect2d. WHY??
        ### Solution might be to create the frame at 0,0,0 and the DGOs relative to it (currently at 0,0,0) THEN move the frame.
        ### TODO: get mouse coords on screen to help with sizing DGOs? 
        
        # add button
        btnClear = DirectButton(pos=(-0.15,0,-0.95),text = ("Clear", "CLEAR", "Clear", "disabled"), scale=.05, command=self.clearText, parent=self.frmChatBox)
        
        # add text entry box
        self.txtEntry = DirectEntry(text = "",pos=(-0.99,0,-0.95),scale=.05,command=self.setTextBox,initialText="Type Something", numLines = 2, focus=1, parent=self.frmChatBox)
        
        # add button 
        btnCommit = DirectButton(pos=(-0.35,0,-0.95),text = ("Commit", "COMMIT", "Commit", "disabled"), scale=.05, command=self.changeText, parent=self.frmChatBox)
        
        # define some text to be used in 
        bk_text = "This is my Demo"
        
        # add text label, not parented to 'frmChatBox'
        self.lblLabel = DirectLabel(text = bk_text, pos = (0.95, 0, -0.95), scale = 0.07, text_fg=(1,0.5,0.5,1), text_bg=(0,0,0,1), textMayChange=1)       
    

    def changeText(self):
        """ 
        Gets the text from input box "txtEntry" and sets it as the text of label "lblLabel"
        """
        bk_text = self.txtEntry.get()
        self.lblLabel['text'] = bk_text
        
        
    def setTextBox(self, textEntered):
        """
        Sets the text of label "textObject" to the value passed
        """
        self.textObject['text'] = textEntered
        
        
    def clearText(self):
        """
        Clears the text entry box
        """
        self.txtEntry.enterText('')
        
        
    def getDGOcoords(self):
        """
        Prints the coordinates of DirectGUI objects
        """
        for child in self.frmChatBox.getChildren():
            if "Direct" in str(child):
                print child, "  position = ", child.getPos() 
                print child, "  scale = ", child.getScale()
        print "-" * 10
                
        
# create main app instance and run it 
app = MyApp()
app.run()