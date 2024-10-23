# This Python file uses the following encoding: utf-8


#Imports List ****************************

import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
import subprocess
import platform
import os

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


        #MainPageWidgets
        self.ui.createserver_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CreateServerStep1)) #Connecting button to Change Page
        self.ui.help_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.HelpPage)) #Connecting button to Change Page
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)) #Connecting button to Change Page

        #CreateServerStep 1 Widgets
        self.ui.testinternet_button.clicked.connect(self.testinternet_buttonClicked)
        self.ui.installsteamcmd_button.clicked.connect(self.installsteamcmd_buttonClicked)


    #Test Internet
    def testinternet_buttonClicked(self):
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

        #Verify Directory using getcwd()
        cwd = os.getcwd()

        #Print current directory
        print("Current working directory is:", cwd)

        os.system("curl https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip -o steamcmd.zip")
        os.system("unzip steamcmd.zip")
        msgBox = QMessageBox()
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.setWindowTitle("SteamCMD Download")
        msgBox.setText("SteamCMD has been successful downloaded to your local Desktop Directory and Unzipped.")
        msgBox.exec()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
