import os
import re
import sys



def reName(currPath,orginName,newName):
    ch = '[rR]'
    # The Regex pattern to match al characters on and before '-'
    pattern  = ".*" + ch 
    # Remove all characters before the character '-' from string
    strValue = re.sub(pattern, '_R', orginName )

    print(strValue)
    file=os.path.join(currPath,orginName)
    os.rename(file,os.path.join(currPath,newName+strValue))
def main():
    currPath=sys.argv[1]
    allFiles=os.listdir(currPath)

    for i in allFiles:
        reName(currPath,i,sys.argv[2])
    print("Rename Success!!")

if __name__ == "__main__":
    main()

