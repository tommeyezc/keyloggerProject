import keyboard
import datetime


def __init__(self, maxTime = 5, definedIntervalTime = int):
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
    recorded = ""
    recorded = keyboard.record(until='enter')
    print(recorded)

record_log()

# def main():
#     list_of_strings = []
#     while len(list_of_strings) < 5:
#         finalString = record_log()
#         finalString.append(list_of_strings)
#     print(list_of_strings)

# if __name__ == "__main__":
#     print("ejecucion")
#     main()
