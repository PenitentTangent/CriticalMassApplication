#**********************************************************

#Copyright 2018, A Wizard Created by Shervin Mortazavi

#**********************************************************/

import os
import stat
import shutil
import sys
import datetime
import CopyrightTool
from PyQt4 import QtGui, QtCore
from P4 import P4, P4Exception

##=================================== APP GUI ===================================

class Window(QtGui.QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        #BUTTONS
        selectPathBtn = QtGui.QPushButton('Select Path')
        selectPathBtn.clicked.connect(self.choosePath)
        copyrightBtn = QtGui.QPushButton('Copyright!')
        copyrightBtn.clicked.connect(self.copyright)

        #CHECKBOXES
        self.p4Toggle = QtGui.QCheckBox("")
        self.p4Toggle.stateChanged.connect(self.toggleP4)
        self.yearToggle = QtGui.QCheckBox("Custom Year?")
        self.yearToggle.stateChanged.connect(self.toggleYear)

        #LABELS
        pathInfo = QtGui.QLabel('This wizard will use this path to hunt for .cs files and update their copyright headers')
        p4Info = QtGui.QLabel('Create P4 changelists?')
        emptyLabel = QtGui.QLabel("")
        self.yearInfo = QtGui.QLabel('Automatically use system\'s current year for copyright')
        self.yearInfo.setStyleSheet('color: gray')
        
        self.p4Port = QtGui.QLabel("Server (P4PORT): ")
        self.p4Port.setStyleSheet('color: gray')
        self.p4User = QtGui.QLabel("User (P4USER): ")
        self.p4User.setStyleSheet('color: gray')
        self.p4Client = QtGui.QLabel("Workspace (P4CLIENT: ")
        self.p4Client.setStyleSheet('color: gray')
        
        self.errorLabel = QtGui.QLabel("")
        self.errorLabel.setStyleSheet('color: red')
        
        #LINE-EDITS
        self.pathEdit = QtGui.QLineEdit()
        self.yearEdit = QtGui.QLineEdit()
        self.yearEdit.setText(str(datetime.datetime.now().year))
        self.yearEdit.setEnabled(False)
        self.portEdit = QtGui.QLineEdit()
        self.portEdit.setEnabled(False)
        self.userEdit = QtGui.QLineEdit()
        self.userEdit.setEnabled(False)
        self.clientEdit = QtGui.QLineEdit()
        self.clientEdit.setEnabled(False)

        #LAYOUT
        grid = QtGui.QFormLayout()
        grid.setSpacing(5)

        grid.addRow(emptyLabel, emptyLabel) #
        grid.addRow(selectPathBtn, self.pathEdit)
        grid.addRow(emptyLabel, pathInfo)
        grid.addRow(emptyLabel, emptyLabel) #
        grid.addRow(self.yearToggle, self.yearEdit)
        grid.addRow(emptyLabel, self.yearInfo)
        grid.addRow(emptyLabel, emptyLabel) #
        grid.addRow(p4Info, self.p4Toggle)
        grid.addRow(self.p4Port, self.portEdit)
        grid.addRow(self.p4User, self.userEdit)  
        grid.addRow(self.p4Client, self.clientEdit)
        grid.addRow(emptyLabel, emptyLabel) #    
        grid.addRow(emptyLabel, copyrightBtn) 
        grid.addRow(emptyLabel, self.errorLabel) 

        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Shervin\'s Magical Copyright Wizard')  
        self.setWindowIcon(QtGui.QIcon('wizard.png'))  
        self.show()

    def choosePath(self):
        try:
            path = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
            self.pathEdit.setText(path)
        except:
            pass
    
    def toggleP4(self, state):
        if state == QtCore.Qt.Checked:
            self.portEdit.setEnabled(True)
            self.p4Port.setStyleSheet('color: black') 
            self.userEdit.setEnabled(True)
            self.p4User.setStyleSheet('color: black') 
            self.clientEdit.setEnabled(True)
            self.p4Client.setStyleSheet('color: black') 
        else:
            self.portEdit.setEnabled(False)
            self.p4Port.setStyleSheet('color: gray') 
            self.userEdit.setEnabled(False)
            self.p4User.setStyleSheet('color: gray') 
            self.clientEdit.setEnabled(False)
            self.p4Client.setStyleSheet('color: gray')

    def toggleYear(self, state):
        if state == QtCore.Qt.Checked:
            self.yearInfo.setText('Enter year')
            self.yearInfo.setStyleSheet('color: black')
            self.yearEdit.setEnabled(True)
        else:
            self.yearInfo.setText('Automatically use system\'s current year for copyright')
            self.yearInfo.setStyleSheet('color: gray')
            self.yearEdit.setText(str(datetime.datetime.now().year))
            self.yearEdit.setEnabled(False)


    def copyright(self):

        path = str(self.pathEdit.text())
        if self.p4Toggle.isChecked():
            togglePerforce = True
            port = str(self.portEdit.text())
            user = str(self.userEdit.text())
            client = str(self.clientEdit.text())
        else:
            togglePerforce = False
            port = user = client = None

        if self.yearToggle.isChecked():
            customYear = str(self.yearEdit.text())
        else:
            customYear = None
        
        print str(customYear)
        try:
            CopyrightFiles(path, togglePerforce, port, user, client, customYear)
            self.errorLabel.setText("Success!")
            self.errorLabel.setStyleSheet('color: green')
        except Exception, e:
            self.errorLabel.setText(str(e))
            self.errorLabel.setStyleSheet('color: red')


##=================================== COPYRIGHT FUNCTIONS ==========================================


##=========GLOBAL VARIABLES ======##

year = datetime.datetime.now().year

p4 = P4()

# The line number where the actual copyright sentence will be
copyrightLineNumber = 3


def InitializePerforce(port, user, client):
    global p4 
    p4.port = port
    p4.user = user
    p4.client = client

    try:
        print "trying to connect"
        p4.connect()
    except P4Exception:
        print "fell in exception"
        raise
    print "did we connect?: " + str(p4.connected())
    print str(p4.user)

    global changeListNew
    changeListNew = p4.fetch_change()
    changeListNew["Description"] = "[COPYRIGHT TOOL] - New Copyrights."
    global createdCLNumberNew
    createdCLNumberNew = p4.save_change( changeListNew )[0].split()[1]

    global changeListAmended
    changeListAmended = p4.fetch_change()
    changeListAmended["Description"] = "[COPYRIGHT TOOL] - Amended Copyrights."
    global createdCLNumberAmended
    createdCLNumberAmended = p4.save_change( changeListAmended )[0].split()[1]

    global changeListFailed
    changeListFailed = p4.fetch_change()
    changeListFailed["Description"] = "[COPYRIGHT TOOL] - Failed Copyrights."
    global createdCLNumberFailed
    createdCLNumberFailed = p4.save_change( changeListFailed )[0].split()[1]

def CopyrightFiles(rootPath, togglePerforce=False, port=None, user=None, client=None, customYear=None):
    
    # check if path exists. Throw exception otherwise.
    if not os.path.exists(rootPath):
        if rootPath == "":
            raise Exception("Please select a path first!")
        else:
            raise Exception("Non-existant path!")

    # connect to perforce
    if (togglePerforce):
        InitializePerforce(port, user, client)

    # check for custom date
    global year
    if (customYear != None):
        year = customYear
    else:
        year = datetime.datetime.now().year
    

    # walk through root
    try:
        for subdir, dirs, files in os.walk(rootPath):
            print "we're walking!"
            for file in files:
                # Grab entire file path and file extension
                filePath = os.path.join(subdir, file)
                ext = os.path.splitext(filePath)[-1].lower()
                # check if file is .cs file
                if ((ext == ".cs") or (ext == ".txt")):
                    print "passing in this filePath: " + filePath
                    Diagnose(filePath);
                    print"got here"
        p4.disconnect()
    except Exception, e:
        p4.disconnect()
        raise
                
def Diagnose(filePath):
    
    copyrightText = ""
    startOverwriteIndex = 0
    # open permissions
    os.chmod(filePath, stat.S_IWUSR)

    # Grab entire contents of file and the specific line where copyright might be
    file = open(filePath, 'r')
    fileContent = file.readlines()
    suspectCopyrightLine = fileContent[copyrightLineNumber - 1]
    print "suspectCopyrightLine: " + suspectCopyrightLine;
    file.close()
    
    # Check which copyright change we should do
    if "Copyright" not in suspectCopyrightLine:
        copyrightText = CreateNewCopyright()
        if ((p4.connected()) and (p4 != None)):
            print "changeList name: " + str(createdCLNumberNew)
            p4.run_add("-c", createdCLNumberNew, filePath)
    elif "-" in suspectCopyrightLine:
        copyrightText = UpdateRangeCopyright(suspectCopyrightLine)
        startOverwriteIndex = 6;
        if ((p4.connected()) and (p4 != None)):
            p4.run_add("-c", createdCLNumberAmended, filePath)
    else:
        copyrightText = UpdateSingleCopyright(suspectCopyrightLine)
        startOverwriteIndex = 6;
        if ((p4.connected()) and (p4 != None)):
            p4.run_add("-c", createdCLNumberAmended, filePath)

    # Open file again, add copyrightText, then add original contents
    file = open(filePath, 'w')
    file.write(copyrightText)
    for i in range(startOverwriteIndex, len(fileContent)):
        file.write(fileContent[i])
    file.close

## COPYRIGHT METHODS THAT HANDLE EACH CASE
##==========================================

def CreateNewCopyright():
    newCopyright = ("/**********************************************************\n"
                    "\n"
                    "Copyright " + str(year) + ", A Wizard Created by Shervin Mortazavi\n"
                    "\n"
                    "/**********************************************************/\n"
                    "\n")
    return newCopyright
    
def UpdateRangeCopyright(currentCopyright):
    dashIndex = currentCopyright.find('-')
    commaIndex = currentCopyright.find(',')
    

    updatedCopyright = currentCopyright[0:dashIndex+1] + str(year) + currentCopyright[commaIndex:]

    newCopyright = ("/**********************************************************\n"
                    "\n"
                    + updatedCopyright + 
                    "\n"
                    "/**********************************************************/\n"
                    "\n")

    return newCopyright

def UpdateSingleCopyright(currentCopyright):
    spaceIndex = currentCopyright.find(' ')
    commaIndex = currentCopyright.find(',')

    updatedCopyright = currentCopyright[0:spaceIndex+1] + str(year) + currentCopyright[commaIndex:]

    newCopyright = ("/**********************************************************\n"
                    "\n"
                    + updatedCopyright + 
                    "\n"
                    "/**********************************************************/\n"
                    "\n")

    return newCopyright


        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()