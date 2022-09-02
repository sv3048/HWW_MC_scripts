import sys
import os
import json

def parseIDList(compactList):
    splitList = compactList.split(',')
    chains = []
    for subList in splitList:
        splitSubList = subList.split('-')
        if len(splitSubList) == 3:
            chains.append(subList)
        elif len(splitSubList) == 4:
            chains += fillIDRange(splitSubList[0], splitSubList[1],
                                  splitSubList[2], splitSubList[3])
        elif len(splitSubList) == 6:
            if splitSubList[0] != splitSubList[3]:
                print "Error: PrepID range must be for the same PWG."
                sys.exit(1)
            if splitSubList[1] != splitSubList[4]:
                print "Error: PrepID range must be for the same chained campaign."
                sys.exit(1)
            chains += fillIDRange(splitSubList[0], splitSubList[1],
                                  splitSubList[2], splitSubList[5])
        else:
            print "Error: Poorly formed PrepID list."
            sys.exit(1)
    return chains


def ListOfPrepids(lowerId,upperId):
    lowerIdNumber = lowerId.split('-')[-1]
    upperIdNumber = upperId.split('-')[-1]
    chains = []
    for i in range(int(lowerIdNumber),int(upperIdNumber)+1):
        fullName = lowerId.split('-')[0]+"-"+lowerId.split('-')[1]+"-"+"0"+str(i)
        #print(fullName)
        chains.append(fullName)
        #chains.append(lowerId.split('-')[0].join('-'+lowerId.split('-')[1]).join('-'+i))
    return chains
