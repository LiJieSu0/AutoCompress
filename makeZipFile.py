import os
import sys
from pathlib import Path
import shutil

#currPath=r"C:\Users\taipi\Desktop\scripts\MyLog" #Path(__file__).parent.absolute() # get the python script path

def makeArchiveToParentDir(currPath,FileName,targetPath): #make archive zip to the parent dir
    shutil.make_archive(os.path.join(currPath,FileName), 'zip', targetPath) # make_archive(dst, zip, src)

def moveFile(source, destination): 
    shutil.move(source,destination) 

def groupingFile(currPath,allFiles): #get the dictionary of the files' name
    fileDict={} # key: fileName without extension, val: filename with dir
    for i in allFiles:
        pureFileName=Path(i).stem
        if pureFileName not in fileDict:
            fileDict[pureFileName]=[os.path.join(currPath,i)]
        else:
            fileDict[pureFileName].append(os.path.join(currPath,i))
    return fileDict

def main():
    currPath=sys.argv[1]
    allFiles=os.listdir(currPath)
    
    fileDict=groupingFile(currPath,allFiles)

    newDirLst=[]
    for key, value in fileDict.items(): #move files to tempDir
        newDir=key+"Temp"
        newDirLst.append(newDir)
        try:
            os.mkdir(os.path.join(currPath,newDir))
        except:
            print("Folder create failed")
        for i in value:
            moveFile(i,os.path.join(currPath,newDir))
    print(newDirLst)

    for key in fileDict:
        print(key+".zip creating")
        makeArchiveToParentDir(currPath,key,os.path.join(currPath,key+"Temp"))
        print(key+".zip creat success")
    
    for i in newDirLst:
        tempPath=os.path.join(currPath,i)
        files=os.listdir(tempPath)
        for i in files:
            moveFile(os.path.join(tempPath,i),currPath)
        shutil.rmtree(tempPath)

if __name__ == "__main__":
    main()






