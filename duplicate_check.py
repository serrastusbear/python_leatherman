__author__ = 'jslowik'
import argparse, hashlib, csv, os, time#, magic
from datetime import date, datetime

#Purpose: pass a directory as a command-line argument
#Recurse through the directory creating a list of files by type (file output),
#hash, and date modified.
#Command-line option to either remove duplicate items (saving most-recent or oldest),
#or move them to a tmp directory for manual removal.

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', action='store', help='Directory to search')
    parser.add_argument('-t', '--temp', action='store', help='Location of temporary directory for move')
    parser.add_argument('-s', '--hash', action='store_true', help='specify SHA1 hash (default is MD5)')
    parser.add_argument('-n', '--newest', action='store_true', help='Save newest file (default is oldest')
    parser.add_argument('-d','--delete', action='store_true',
                        help='Delete duplicate files (default is move)')
    return parser.parse_args()

def fileHash(file, arg):
    if arg:
        return hashlib.sha1(file).hexdigest()
    else:
        return hashlib.md5(file).hexdigest()

def recurseThroughDirectory(directory, hash):
    if not directory:
        print("Must supply directory to search!")
        exit()
    else:
        fileList = []
        for dirpath, dirnames, filenames in os.walk(directory):
            #print(dirpath)
            for file in filenames:
                fullPath = dirpath + file
                #print(fullPath)
                hashValue = fileHash(fullPath, hash)
                #print(hashValue)
                fileType = "null" #add in call to function using python-magic lib
                rawTime = os.path.getmtime(fullPath)
                lastModTime = convertTime(rawTime)
                dataEntry=[file,hashValue,fileType,lastModTime]
                fileList.append(dataEntry)
        return fileList

def convertTime(mtime):
    #dateTimeObject = datetime.datetime.fromtimestamp(mtime)
    dateTimeObject = datetime.fromtimestamp(mtime)
    return dateTimeObject.strftime("%y-%m-%d-%H:%M")

def createFileList(tempLocation, fileList):
    if not tempLocation or not fileList:
        pass
    else:
        if not tempLocation.endswith("/"): tempLocation = tempLocation + "/"
        dateStamp = date.today().strftime("%y_%m_%d")
        #print(dateStamp)
        fileName = tempLocation + dateStamp + "_tmp.csv"
        #print(fileName)
        with open(fileName, 'w') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',')
            for item in fileList:
                csvWriter.writerow(item)

if __name__ == '__main__':
    parser=argumentParser()
    fileList = recurseThroughDirectory(parser.directory, parser.hash)
    createFileList(parser.temp, fileList)