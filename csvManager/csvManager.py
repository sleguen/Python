#!/usr/bin/python
# vim: set fileencoding=utf-8 :
"""@package docstring
Documentation for csvManager
"""
import csv
import time
import random

class csvManager:
    def __init__(self,myFileName,myFileMode,myDbgMode):
        """
        The constructor take in argument : 
        - The file name where to log datas
        - The file mode
        - A boolean to activate or not debug message
        """ 
        self.myFileName = myFileName
        self.myFileMode = myFileMode
        self.myDbgMode  = myDbgMode
        self.myFile     = open(self.myFileName,self.myFileMode)
        self.myWriter   = csv.writer(self.myFile,delimiter=';')     
    def writeHeader(self):
        """
        Write the two first line (header line) of log file
        """
        if self.myDbgMode == "ENABLE":
            print 'writeHeader'
        self.myWriter.writerow(("TIMESTAMP","TEMPERATURE"))
    def writeValue(self,Temperature):
        """
        Write temperature into the log file with the following
        format :
        A timestamp + the temperature value
        """
        if self.myDbgMode == "ENABLE":
            print 'writeValue'
        timeStamp   = time.strftime("%A %d %B %Y %H:%M:%S")
        self.myWriter.writerow((timeStamp,Temperature))
        #Flush myFile to write negative temperature
        self.myFile.flush()
