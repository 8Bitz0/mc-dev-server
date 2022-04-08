from unittest import TextTestResult


debugPrefix = "[DEBUG] "
infoPrefix = "[INFO] "
warningPrefix = "[WARNING] "
errorPrefix = "[ERROR] "
criticalPrefix = "[CRITICAL] "

from .. import Config

def debug(text):
    if Config.debug == True:
        print(debugPrefix + text)

def info(text):
    print(infoPrefix + text)

def warning(text):
    print(warningPrefix + text)

def error(text):
    print(errorPrefix + text)

def critical(text):
    print(criticalPrefix + text)