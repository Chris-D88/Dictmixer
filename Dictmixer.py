#config:utf-8
#author:Chris
#date:2021-4-21
'''
Dictmixer功能：将两个字典文件进行对比，去除两个字典中相同的条目，生成新字典。

Dictmixer用法：Dictmixer.py -s <Dictionary1> -d <Dictionary2> -m <mixed_Dictionary>
-s 或者 --sfile 加载第一个字典
-d 或者 --dfile 加载第二个字典
-m 或者 --mfile 混合后的字典名称

'''

import os
import sys,getopt

def readFile(fileName,mode='r'):
    fp = open(fileName,mode,encoding="utf-8")
    content = fp.readlines()
    fp.close()
    return content

def arrDic(souceFileName,destFileName):
    sourceArr = []
    destArr = []
    souceContent = readFile(souceFileName)
    destContent = readFile(destFileName)
    for sourceItem in souceContent:
        sourceArr.append(str(sourceItem))
    for destItem in destContent:
        destArr.append(str(destItem))
    return sourceArr,destArr

def check(sourceArr,destArr):
    format_sourceArr = []
    for sourceItem in sourceArr:
        if not '\n' in sourceItem:
            sourceItem = sourceItem+'\n'
        format_sourceArr.append(str(sourceItem))
    for destItem in destArr:
        if not '\n' in destItem:
            destItem = destItem+'\n'
        if not destItem in format_sourceArr:
            format_sourceArr.append(str(destItem))
    return format_sourceArr

def writeFile(fileName,mix,mode='w'):
    fp = open(fileName,mode,encoding="utf-8")
    for item in mix:
        fp.writelines(str(item))
    fp.close()

def main(argv):
    if not len(argv) == 0:
        sourceFileName = ''
        destFileName = ''
        mixFileName = ''
        
        try:
            opts, args = getopt.getopt(argv,"hs:d:m:",["sfile=","dfile=","mfile="])
        except getopt.GetoptError:
            print ('Dictmixer.py -s <Dictionary1> -d <Dictionary2> -m <mixed_Dictionary>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('Dictmixer.py -s <Dictionary1> -d <Dictionary2> -m <mixed_Dictionary>')
                sys.exit()
            elif opt in ("-s", "--sfile"):
                sourceFileName = arg
            elif opt in ("-d", "--dfile"):
                destFileName = arg
            elif opt in ("-m", "--mfile"):
                mixFileName = arg

        print('\r'+"Dictionary mixing, please wait...")
        dic =  arrDic(sourceFileName, destFileName)
        sourceArr = dic[0]
        destArr = dic[1]
        mix = check(sourceArr, destArr)
        #print(mix)
        writeFile(mixFileName,mix)
        print('\r'+"The mixing is successful, please open "+"\033[1;31m"+mixFileName+"\033[0m"+" to view!!!")
    else:
        print('Dictmixer.py -s <Dictionary1> -d <Dictionary2> -m <mixed_Dictionary>')
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])