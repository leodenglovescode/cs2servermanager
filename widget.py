# This Python file uses the following encoding: utf-8


#Imports List ****************************

import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QProgressDialog
import subprocess
import platform
import os
from playsound import playsound
from pathlib import Path
import shutil

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


#END of Imports List *********************



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #MainPage Title
        self.setWindowTitle("CS2 Server Manager Beta V1.0.0")


        #MainPageWidgets
        self.ui.createserver_button.clicked.connect(self.createserver_buttonClicked) #Connecting button to Change Page
        self.ui.help_button.clicked.connect(self.help_buttonClicked) #Connecting button to Change Page
        self.ui.settings_button.clicked.connect(self.settings_buttonClicked) #Connecting button to Change Page

        #CreateServerStep 1 Widgets
        self.ui.testinternet_button.clicked.connect(self.testinternet_buttonClicked)
        self.ui.installsteamcmd_button.clicked.connect(self.installsteamcmd_buttonClicked)
        self.ui.continue_button.clicked.connect(self.continue_buttonClicked)

        #CreateServerStep 2 Widgets
        self.ui.installserver_button.clicked.connect(self.installserver_buttonClicked)

        #MainMenu Background Image
        self.ui.stackedWidget.setStyleSheet("""
        QStackedWidget {
            background-image: url('assets/img/mainmenu.jpg');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            }
        """)


#MainPageWidgets*************************
#****************************************
    def createserver_buttonClicked(self):
        playsound('assets/sfx/buttonsfx.wav')
        self.ui.stackedWidget.setCurrentWidget(self.ui.CreateServerStep1)


    def help_buttonClicked(self):
        playsound('assets/sfx/buttonsfx.wav')
        self.ui.stackedWidget.setCurrentWidget(self.ui.HelpPage)


    def settings_buttonClicked(self):
        playsound('assets/sfx/buttonsfx.wav')
        self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)

#MainPageWidgets*************************
#****************************************






#CreateServerStep 1 Widgets**************
#****************************************
    #Test Internet
    def testinternet_buttonClicked(self):
        playsound('assets/sfx/buttonsfx.wav')
        print("Testing Internet...")

        def myping(host):
            parameter = '-n' if platform.system().lower()=='windows' else '-c'
            command = ['ping', parameter, '1', host]
            response = subprocess.call(command)


            global connection
            connection = bool()
            if response == 0:
                connection = True
                print(connection)
            else:
                connection = False
                print(connection)

        print(myping("steamcdn-a.akamaihd.net"))

        msgBox = QMessageBox()


        if connection == True:
            msgBox.setIcon(msgBox.Icon.Information)
            msgBox.setWindowTitle("Steam Server Connectivity Test")
            msgBox.setText("Steam Server Connection Successful,\nPlease Proceed.\n\n")
            msgBox.exec()
        elif connection == False:
            msgBox.setIcon(msgBox.Icon.Critical)
            msgBox.setWindowTitle("Steam Server Connectivity Test")
            msgBox.setText("Steam Server Connection Failed,\nPlease Check your Internet Connection.")
            msgBox.exec()


    #Install SteamCMD
    def installsteamcmd_buttonClicked(self):
        #SteamCMD Official Download Link: https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip

        os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop')) #Find Username
        os.system(os.environ['ComSpec'] + ' /c "cd"') #Change Working Directory to Desktop
        os.system("mkdir steamcmd")
        os.chdir("steamcmd")

        #Verify Directory using getcwd()
        cwd = os.getcwd()


        #Print current directory
        print("Current working directory is:", cwd)

        os.system("curl https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip -o steamcmd.zip")
        os.system("unzip steamcmd.zip")
        os.system("steamcmd.exe +quit")
        msgBox = QMessageBox()
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.setWindowTitle("SteamCMD Download")
        msgBox.setText("SteamCMD has been successful downloaded to your local Desktop Directory and Unzipped.")
        msgBox.exec()


    def continue_buttonClicked(self):
        #playsound('./assets/sfx/buttonsfx.wav')
        msgBox = QMessageBox()

        os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop')) #Find Username
        os.system(os.environ['ComSpec'] + ' /c "cd"') #Change Working Directory to Desktop
        os.system("mkdir steamcmd")
        os.chdir("steamcmd")

        #Verify Directory using getcwd()
        cwd = os.getcwd()
        print(cwd)

        steamcmdpath = Path(cwd + "/steamcmd.exe")
        print(steamcmdpath)

        try:
            my_abs_path = steamcmdpath.resolve(strict=True)
        except FileNotFoundError:
            msgBox.setIcon(msgBox.Icon.Critical)
            msgBox.setWindowTitle("SteamCMD Installation")
            msgBox.setText("SteamCMD hasn't been installed on your computer,\nplease click the install steamcmd button again.")
            msgBox.exec()

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.CreateServerStep2)
#CreateServerStep 1 Widgets**************
#****************************************




#CreateServerStep 2 Widgets**************
#****************************************

    def installserver_buttonClicked(self):
        msgBox = QMessageBox()

        #check disk space
        total, used, free = shutil.disk_usage("/")
        print("Total Space: %d GiB" % (total // (2**30)))
        print("Used Space: %d GiB" % (used // (2**30)))
        print("Free Space: %d GiB" % (free // (2**30)))
        freespace_gib = int(free // (2**30))
        #freespace_gb = freespace_gib * 1.07374
        freespace_gb = 54
        print("Free space in GB: ", freespace_gb)

        if freespace_gb < 53:
            msgbox_text = "Your disk does not have enough space to install CS2,\nthe lowest limit for storage is 53 GB.\n\nYour Free Disk Space is: " + str(freespace_gb) + " GB"
            msgBox.setIcon(msgBox.Icon.Critical)
            msgBox.setWindowTitle("Check Disk Space")
            msgBox.setText(msgbox_text)
            msgBox.setStandardButtons(QMessageBox.Abort)
            msgBox.exec()

        elif freespace_gb >= 53:
            msgbox_text = "Your disk has enough space to install CS2,\nDo you want to continue with the Installation?\n\nYour Free Disk Space is: " + str(freespace_gb) + " GB"
            msgBox.setIcon(msgBox.Icon.Question)
            msgBox.setWindowTitle("Check Disk Space")
            msgBox.setText(msgbox_text)
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec()
            if ret == QMessageBox.Yes:
                os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop')) #Find Username
                os.system(os.environ['ComSpec'] + ' /c "cd"') #Change Working Directory to Desktop
                os.system("mkdir steamcmd")
                os.chdir("steamcmd")

                #Verify Directory using getcwd()
                cwd = os.getcwd()
                print("Install Path: ", cwd)

                progress = QProgressDialog("Installing CS2 Server...", "Abort Install", 0, self)
                progress.setWindowModality(Qt.WindowModal)
                for i in range(0, numFiles):
                    progress.setValue(i)
                    if progress.wasCanceled():
                        pass
                    #... copy one file

                progress.setValue(numFiles)


                os.system("steamcmd.exe +force_install_dir ./cs2_ds/ +login anonymous +app_update 730 validate +quit")

            elif ret == QMessageBox.No:
                pass

            else:
                # should never be reached
                print("error 1.")
#CreateServerStep 2 Widgets**************
#****************************************




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
