from unittest import TextTestResult


debugPrefix = "[DEBUG] "
infoPrefix = "[INFO] "
warningPrefix = "[WARNING] "
errorPrefix = "[ERROR] "
criticalPrefix = "[CRITICAL] "

showDebug = True

def debug(text):
    if showDebug == True:
        print(debugPrefix + text)

def info(text):
    print(infoPrefix + text)

def warning(text):
    print(warningPrefix + text)

def error(text):
    print(errorPrefix + text)

def critical(text):
    print(criticalPrefix + text)