#!/usr/bin/python3

import sys
import json
import collections
from collections import OrderedDict
import os
import os.path
import ast
import itertools

'''
This script may be ran anywhere within the gamedatabase.
./updateMolagora.py

Update the table below, if values changed.
'''

# Config
fileName='all'
findChanges = False
printMolagora = False
updateMolagora = True
definedOrder = True
# I think keepOrder is currently broken, not needed.
keepOrder = False


molagora = OrderedDict()
molagora['3'] = {}
molagora['4'] = {}
molagora['5'] = {}
'''
# Example heroes
#molagora['3']['1'] = None..
#molagora['3']['2'] = Bask(S3), Carrot(S2)
#molagora['3']['3'] = Alexa(S1)
#molagora['3']['4'] = Aither(S1/S2)
#molagora['3']['5'] = Montmorancy
#molagora['3']['6'] = Alexa(S2/S3)
#molagora['3']['7'] = Aither(S3)
#molagora['4']['1'] = Khawazu(S2)
#molagora['4']['2'] = Armin(S3)
#molagora['4']['3'] = ML-Lots(S2)
#molagora['4']['4'] = Crozet(S1/S2)
#molagora['4']['5'] = Cidd
#molagora['4']['6'] = Armin(S2)
#molagora['4']['7'] = Khawazu(S1/S3)
#molagora['5']['1'] = Cermia(S2), Tamarinne(S3)
#molagora['5']['2'] = Diene(S3)
#molagora['5']['3'] = Destina(S2)
#molagora['5']['4'] = Aramintha(S1/S2), ML-Kise(S1/S2)
#molagora['5']['5'] = Cecilia, Luna
#molagora['5']['6'] = Destina(S1)
#molagora['5']['7'] = Cermia(S1/S3), Tamarinne(S1/S2)
'''
############################################
#  Update below values when molagora changes
############################################
#       star  lvls  (AFTER 10/2/2019 patch)
molagora['3']['1'] = [
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 0, 'gold': 0}
]
molagora['3']['2'] = [ #
  {'rare': 2, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 250, 'gold': 14000},
  {'rare': 3, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 650, 'gold': 24000}
]
molagora['3']['3'] = [ #
  {'rare': 2, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 200, 'gold': 13000},
  {'rare': 3, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 450, 'gold': 21000},
  {'rare': 5, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 850, 'gold': 37000}
]
molagora['3']['4'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 150, 'gold': 2000},
  {'rare': 2, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 300, 'gold': 14000},
  {'rare': 3, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 550, 'gold': 23000},
  {'rare': 4, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 1100, 'gold': 35000}
]
molagora['3']['5'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 120, 'gold': 2000},
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 270, 'gold': 4000},
  {'rare': 3, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 470, 'gold': 22000},
  {'rare': 4, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 740, 'gold': 30000},
  {'rare': 5, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 1100, 'gold': 40000}
]
molagora['3']['6'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 80, 'gold': 2000},
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 180, 'gold': 3000},
  {'rare': 1, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 320, 'gold': 10000},
  {'rare': 2, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 530, 'gold': 18000},
  {'rare': 4, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 850, 'gold': 32000},
  {'rare': 6, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 1340, 'gold': 48000}
]
molagora['3']['7'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 50, 'gold': 1000},
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 120, 'gold': 2000},
  {'rare': 0, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 230, 'gold': 4000},
  {'rare': 3, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 400, 'gold': 21000},
  {'rare': 4, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 650, 'gold': 29000},
  {'rare': 5, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 1000, 'gold': 39000},
  {'rare': 6, 'epic': 0, 'mola': 0, 'mGo': 0, 'stig': 1450, 'gold': 50000}
]
molagora['4']['1'] = [ #
  {'rare': 8, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 44000}
]
molagora['4']['2'] = [ #
  {'rare': 3, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 19000},
  {'rare': 0, 'epic': 1, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 38000}
]
molagora['4']['3'] = [ #
  {'rare': 1, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 9000},
  {'rare': 3, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 19000},
  {'rare': 0, 'epic': 1, 'mola': 3, 'mGo': 0, 'stig': 0, 'gold': 42000}
]
molagora['4']['4'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 1, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 9000},
  {'rare': 1, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 9000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['4']['5'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 1, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 9000},
  {'rare': 3, 'epic': 0, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 23000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['4']['6'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 1, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 9000},
  {'rare': 2, 'epic': 0, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 18000},
  {'rare': 4, 'epic': 0, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 28000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['4']['7'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 1, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 9000},
  {'rare': 2, 'epic': 0, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 18000},
  {'rare': 5, 'epic': 0, 'mola': 3, 'mGo': 0, 'stig': 0, 'gold': 37000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['5']['1'] = [ #
  {'rare': 8, 'epic': 0, 'mola': 3, 'mGo': 0, 'stig': 0, 'gold': 52000}
]
molagora['5']['2'] = [ #
  {'rare': 5, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 29000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['5']['3'] = [ #
  {'rare': 3, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 19000},
  {'rare': 5, 'epic': 0, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 33000},
  {'rare': 0, 'epic': 3, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 110000}
]
molagora['5']['4'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 3, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 19000},
  {'rare': 5, 'epic': 0, 'mola': 3, 'mGo': 0, 'stig': 0, 'gold': 37000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['5']['5'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 5, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 29000},
  {'rare': 7, 'epic': 0, 'mola': 3, 'mGo': 0, 'stig': 0, 'gold': 47000},
  {'rare': 0, 'epic': 2, 'mola': 5, 'mGo': 0, 'stig': 0, 'gold': 80000}
]
molagora['5']['6'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 2, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 14000},
  {'rare': 4, 'epic': 0, 'mola': 2, 'mGo': 0, 'stig': 0, 'gold': 28000},
  {'rare': 5, 'epic': 0, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 45000},
  {'rare': 0, 'epic': 2, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 80000}
]
molagora['5']['7'] = [ #
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 0, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 4000},
  {'rare': 3, 'epic': 0, 'mola': 1, 'mGo': 0, 'stig': 0, 'gold': 19000},
  {'rare': 4, 'epic': 0, 'mola': 3, 'mGo': 0, 'stig': 0, 'gold': 32000},
  {'rare': 7, 'epic': 0, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 55000},
  {'rare': 0, 'epic': 3, 'mola': 0, 'mGo': 1, 'stig': 0, 'gold': 110000}
]

############################################
#  End of molagora table
############################################

catalyst = OrderedDict()
catalyst['aries'] = {'rare':'path-power-loop', 'epic':'nightmare-mask'}
catalyst['taurus'] = {'rare':'shiny-enchantment', 'epic':'horn-of-desire'}
catalyst['gemini'] = {'rare':'ring-of-glory', 'epic':'fused-nerve'}
catalyst['cancer'] = {'rare':'baby-mouse-insignia', 'epic':'the-heart-of-hypocrisy'}
catalyst['leo'] = {'rare':'twisted-fang', 'epic':'blazing-soul'}
catalyst['virgo'] = {'rare':'flame-of-soul', 'epic':'demon-blood-gem'}
catalyst['libra'] = {'rare':'mysterious-flash', 'epic':'reingar-student-id'}
catalyst['scorpio'] = {'rare':'sharp-spearhead', 'epic':'black-curse-powder'}
catalyst['sagittarius'] = {'rare':'archers-vision', 'epic':'mercenarys-medicine'}
catalyst['capricorn'] = {'rare':'slime-jelly', 'epic':'dragons-wrath'}
catalyst['aquarius'] = {'rare':'leather-sheath', 'epic':'fighter-medal'}
catalyst['pisces'] = {'rare':'strange-jelly', 'epic':'ancient-creature-nucleus'}

def generatePath(items, recursiveStep):
    index = 0
    path = []
    while(index < len(items)):
        if items[index] == 'dict':
            if len(items) < index+1+1:
                print('Dict requires a name')
                quit()
            index += 1
            hop = 'dict:'+items[index]
            path.append(hop)
        elif items[index] == 'list':
            if len(items) < index+1+1:
                print('list requires a name')
                quit()
            index += 1
            hop = 'list:'+items[index]
            path.append(hop)
        elif items[index] == 'item':
            if len(items) < index+1+1:
                print('item requires a number')
                quit()
            index += 1
            try:
              int(items[index])
            except ValueError:
                print('item requires a number')
                quit()
            hop = 'list:'+items[index]
            path.append(hop)
        elif items[index] == 'var':
            if len(items) < index+1+3:
                print('var requires a type, path, and varEnd')
                quit()
            if recursiveStep != 0:
                print('Currently do not support var within var')
                quit()
            index += 1
            hop = '\'var:{\\\'type\\\':\\\''+items[index]+'\\\', \\\'value\\\':'
            index += 1
            ret,retIndex = generatePath(items[index:], recursiveStep+1)
            ret = str(ret).replace("'","\\'")
            hop = hop+str(ret)+'}\''
            path.append(str(hop))
            #print(path)
            index += retIndex
        elif items[index] == 'varEnd':
            if recursiveStep == 0:
                print('varEnd requires a var first')
                quit()
            index += 1
            break
        elif items[index] == 'value':
            if len(items) < index+1+1:
                print('value requires a value')
                quit()
            index += 1
            hop = items[index]
            path.append(hop)
        else:
            print('Expected type, got \''+str(items[index])+'\'')
            quit()
        index += 1
    return path, index
'''
if command == 'genPath':
    path,index = generatePath(sys.argv[2:], 0)
    #print(path)
    print('"'+str(path).replace("\"","")+'"')
    quit()
'''
# Create a list of all variables that match searchVar
def findDictWithVar(jsonData, searchVar, path):
    dictList = []
    index = 0
    for var in jsonData:
        if var == searchVar:
            dictList = dictList+[{'jsonData':jsonData, 'path':path}]
        elif isinstance(var, collections.Mapping):
            ret = findDictWithVar(var, searchVar, path+['item:'+str(index)])
            if ret != []:
                dictList = dictList+ret
        elif isinstance(jsonData[var], collections.Mapping):
            ret = findDictWithVar(jsonData[var], searchVar, path+['dict:'+var])
            if ret != []:
                dictList = dictList+ret
        elif isinstance(jsonData[var], list):
            if len(jsonData[var]) == 0:
                continue;
            if isinstance(jsonData[var][0], collections.Mapping) == False:
                continue;
            ret = findDictWithVar(jsonData[var], searchVar, path+['list:'+var])
            if ret != []:
                dictList = dictList+ret
        index = index + 1
    return dictList
  
# Convert path to type, value
def convertPath(pathStr):
    pathType = ''
    pathValue = ''
    if pathStr.startswith('dict:'):
        pathType = 'dict'
        pathValue = pathStr[5:]
    elif pathStr.startswith('item:'):
        pathType = 'item'
        pathValue = pathStr[5:]
    elif pathStr.startswith('list:'):
        pathType = 'list'
        pathValue = pathStr[5:]
    else:
        pathType = ''
        pathValue = pathStr
    return pathType,pathValue

# Returns exact path of variable
def findVar(jsonData, fullPath):
    ret = None
    for hop in fullPath:
        pathTypeA,pathValueA = convertPath(hop)
        if pathValueA not in jsonData:
            return None
        ret = [jsonData, pathValueA]
        jsonData = jsonData[pathValueA]
    return ret

# Returns exact value of variable
def findVarValue(jsonData, fullPath):
    ret = None
    for hop in fullPath:
        pathTypeA,pathValueA = convertPath(hop)
        if pathValueA not in jsonData:
            return None
        jsonData = jsonData[pathValueA]
    return jsonData

# Reads fullPath and replaces var:.... with real value
def replacePathVariables(jsonFileName, jsonData, fullPath):
    newPath = []
    for hop in fullPath:
        if hop.startswith('var:'):
            varHop = ast.literal_eval(hop[4:])
            if varHop['value'] == 'fileNameNoEx':
                foundVal = os.path.splitext(jsonFileName)[0]
            else:
                foundVal = findVarValue(jsonData, varHop['value'])
            hop = varHop['type']+':'+foundVal
        newPath.append(hop)
    return newPath

#print(ast.literal_eval(sys.argv[cmdIndex+1]))
#with open('luna.json', 'r') as infile:
#  inJson = json.load(infile, object_pairs_hook=OrderedDict)
#  fixedFath =replacePathVariables(inJson, ast.literal_eval(sys.argv[cmdIndex+1]))
#  print(fixedFath)
  #print(findVarValue(inJson, ast.literal_eval(sys.argv[cmdIndex+1])))
#quit()

# Insert variable into directory
def insertDictVar(jsonData, prevVarName, newVarName):
    for _ in range(len(jsonData)):
        k, v = jsonData.popitem(False)
        jsonData[k] = v
        if prevVarName == k:
            jsonData[newVarName] = ''

# Delete a variable from directory
def deleteDictVar(jsonData, delVar):
    if delVar not in jsonData:
        return
    jsonData.move_to_end(delVar)
    jsonData.popitem()

# Rename a variable in directory
def renameDictVar(jsonData, oldName, newName):
    for _ in range(len(jsonData)):
        k, v = jsonData.popitem(False)
        jsonData[newName if oldName == k else k] = v

# Move to index
def moveDictVar(jsonData, name, moveIndex):
    # Remove moving data
    jsonData.move_to_end(name)
    mvName, mvVal = jsonData.popitem(True)
    added = False
    # Copy into new data
    tmpData = OrderedDict()
    index = 0
    for _ in range(len(jsonData)):
        k, v = jsonData.popitem(False)
        # When hit needed index, insert it and continue to insert the rest.
        if moveIndex == index:
            tmpData[mvName] = mvVal
            added = True
        tmpData[k] = v
        index = index + 1
    if added == False:
        tmpData[mvName] = mvVal
    jsonData.update(tmpData)

# Write json into file
def writeJson(outputFile, jsonData):
    with open(outputFile, 'w') as outfile: 
        json.dump(jsonData, outfile, indent=4, separators=(',', ': '), ensure_ascii=False)
        outfile.write("\n")
        
# Print json to screen
def printJson(jsonData):
    print(json.dumps(jsonData, indent=4, separators=(',', ': '), ensure_ascii=False))

# Get list of all json files
def getAllJsonFiles(dir):
    allFiles = os.listdir(dir)
    jsonFiles = []
    for fileName in allFiles:
        if fileName.endswith('.json'):
            if 'TEMPLATE'.lower() in fileName.lower():
                continue
            jsonFiles = jsonFiles + [fileName]
    return jsonFiles

def findHeroDirectory(curPath):
    curList = curPath.split('/')
    if len(curList) <= 1:
      quit()
    if curList[-1] == 'hero':
        return ''
    if curList[-1] == 'src':
        return 'hero'
    lsList = os.listdir(curPath)
    if 'hero' in lsList:
        return 'hero'
    if 'src' in lsList:
        return 'src/hero'
    return '../'+findHeroDirectory('/'.join(curList[0:-1]))
    
dirToHero = ''
dirToHero = findHeroDirectory(os.getcwd())
if dirToHero != '':
    os.chdir(dirToHero)
if fileName == 'all':
    fileList = getAllJsonFiles('.')
else:
    if os.path.isfile(fileName) == False:
        print(fileName+' is not a file.')
        quit()
    fileList = [fileName]

# Check if paths match, * values means all match
def matchPath(pathA, pathB):
    if inHop == searchHop:
        return True
    pathTypeA,pathValueA = convertPath(pathA)
    pathTypeB,pathValueB = convertPath(pathB)
    if pathTypeA == pathTypeB and (pathValueA == '*' or pathValueB == '*'):
        return True
    if pathTypeA == '' and pathValueA == '*':
        return True
    if pathTypeB == '' and pathValueB == '*':
        return True
    return False

# Create decoder, so we can decode strings to OrderedDict.
decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)


# Main
for fileName in fileList:
    with open(fileName, 'r') as infile:
        inJson = json.load(infile, object_pairs_hook=OrderedDict)
        name = findDictWithVar(inJson, 'name', [])
        name = name[0]['jsonData']['name']
        rarity = findDictWithVar(inJson, 'rarity', [])
        rarity = str(rarity[0]['jsonData']['rarity'])
        zodiac = findDictWithVar(inJson, 'zodiac', [])
        zodiac = str(zodiac[0]['jsonData']['zodiac'])
        enhancements = findDictWithVar(inJson, 'enhancement', [])
        display = ''
        display =  "".join((
          display,
          fileName+' '+name+' '+rarity+' '+zodiac+' skillLvls:'))

        for skillEnh in enhancements:
          if 'list:skills' not in skillEnh['path']:
            continue
          display =  "".join((
            display,
            ' '+str(len(skillEnh['jsonData']['enhancement']))))
        #print(display)

        if zodiac not in catalyst:
          print('Error: Bad zodiac.  '+display)
        
        if rarity not in molagora:
          print('Error: Bad molagora hero rarity.  '+display)
          continue
        molaValues = molagora[rarity]
        
        for skillEnh in enhancements:
          if 'list:skills' not in skillEnh['path']:
            continue
          numItems = str(len(skillEnh['jsonData']['enhancement']))
          if numItems not in molaValues:
            print('Error: Bad molagora max level.  '+display)
            continue
          lvl = -1
          for enhLevel in skillEnh['jsonData']['enhancement']:
            lvl = lvl + 1
            resourceList = enhLevel['resources']
            # Construct expected.
            expectedList = []
            tmpList = []
            if definedOrder:
              if molaValues[numItems][lvl]['gold'] != 0:
                  tmpList.append(('item', 'gold'))
                  tmpList.append(('qty', molaValues[numItems][lvl]['gold']))
                  expectedList.append(OrderedDict(tmpList))
              if molaValues[numItems][lvl]['mola'] != 0:
                  tmpList.append(('item', 'molagora'))
                  tmpList.append(('qty', molaValues[numItems][lvl]['mola']))
                  expectedList.append(OrderedDict(tmpList))
              if molaValues[numItems][lvl]['mGo'] != 0:
                  tmpList.append(('item', 'molagorago'))
                  tmpList.append(('qty', molaValues[numItems][lvl]['mGo']))
                  expectedList.append(OrderedDict(tmpList))
              if 'stig' in molaValues[numItems][lvl]:
                  if molaValues[numItems][lvl]['stig'] != 0:
                      tmpList.append(('item', 'stigma'))
                      tmpList.append(('qty', molaValues[numItems][lvl]['stig']))
                      expectedList.append(OrderedDict(tmpList))
              if molaValues[numItems][lvl]['rare'] != 0:
                  tmpList.append(('item', catalyst[zodiac]['rare']))
                  tmpList.append(('qty', molaValues[numItems][lvl]['rare']))
                  expectedList.append(OrderedDict(tmpList))
              if molaValues[numItems][lvl]['epic'] != 0:
                  tmpList.append(('item', catalyst[zodiac]['epic']))
                  tmpList.append(('qty', molaValues[numItems][lvl]['epic']))
                  expectedList.append(OrderedDict(tmpList))
            if keepOrder:
              for item in molaValues[numItems][lvl]:
                if molaValues[numItems][lvl][item] != 0:
                  itemName = item
                  if itemName == 'mola':
                    itemName = 'molagora'
                  elif itemName == 'mGo':
                    itemName = 'molagorago'
                  elif itemName == 'stig':
                    itemName = 'stigma'
                  elif itemName == 'rare':
                    itemName = catalyst[zodiac]['rare']
                  elif itemName == 'epic':
                    itemName = catalyst[zodiac]['epic']
                  #lvlList = OrderedDict([('item', itemName)])
                  #lvlList.append(('item', itemName))
                  tmpList.append(('item', itemName))
                  tmpList.append(('qty', molaValues[numItems][lvl][item]))
                  expectedList.append(OrderedDict(tmpList))
            if updateMolagora:
              enhLevel['resources'] = expectedList

            # Read current values
            if findChanges:
              for item in resourceList:
                itemName = item['item']
                itemQty = item['qty']
                if itemName == 'molagora':
                  itemName = 'mola'
                elif itemName == 'molagorago':
                  itemName = 'mGo'
                elif itemName == 'stigma':
                  itemName = 'stig'
                elif itemName == 'gold':
                  itemName = 'gold'
                elif itemName == catalyst[zodiac]['rare']:
                  itemName = 'rare'
                elif itemName == catalyst[zodiac]['epic']:
                  itemName = 'epic'
                else:
                  continue
                if molaValues[numItems][lvl][itemName] != itemQty:
                  print('Changing ('+numItems+','+str(lvl)+','+itemName+') '+str(molaValues[numItems][lvl][itemName])+' '+str(itemQty))
                  molaValues[numItems][lvl][itemName] = itemQty
        if updateMolagora:
          writeJson(fileName, inJson)

if printMolagora:
  for molaStar in molagora:
    for molaMax in molagora[molaStar]:
      print('molagora[\''+molaStar+'\'][\''+molaMax+'\'] = [')
      for molaLvl in molagora[molaStar][molaMax]:
        if(molaLvl == molagora[molaStar][molaMax][-1]):
          print('  '+str(molaLvl))
        else:
          print('  '+str(molaLvl)+',')
      print(']')
          #print('  '+molagora[molaStar][molaMax][molaLvl])
