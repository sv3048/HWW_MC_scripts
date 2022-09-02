'''
last used
python test_delete.py --prepid HIG-RunIIFall17wmLHEGS-06248 
python test_delete.py --lowerprepid HIG-RunIIFall17wmLHEGS-06249 --upperprepid HIG-RunIIFall17wmLHEGS-06251 --activeRange True
'''

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from argparse import ArgumentParser
from listOfFunctions import *

parser = ArgumentParser()
parser.add_argument('--prepid', type=str, help="put mcm requests using prepids for multiple use comma[e.g, HIG-RunIIFall18wmLHEGS-02657,HIG-RunIIFall18wmLHEGS-02660]",dest="prepid")
parser.add_argument("--tags",type=str, help="coumpute from local run",dest="tags")
parser.add_argument('--lowerprepid', type=str, help="lowest prepid",dest="lowerprepid")
parser.add_argument('--upperprepid', type=str, help="upper prepid",dest="upperprepid")
parser.add_argument('--activeRange',dest="activeRange", default=False, help="use True or False")

args = parser.parse_args()

#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

mcm = McM(dev=False)

# Example to edit a request parameter(-s) and save it back in McM
# request_prepid_to_update = 'HIG-Summer12-01257' # Doesn't exist
if(args.activeRange):
    prepidlists = ListOfPrepids(args.lowerprepid,args.upperprepid)
    print('prepidlists',prepidlists)

#prepids = parseIDList(args.prepid)
if(args.activeRange):
    prepids = prepidlists
else:
    prepids = parseIDList(args.prepid)

print('prepid',prepids)
print "Updating {0} base requests".format(len(prepids))

for prepid in prepids:
    request_prepid_to_update = prepid  #sys.argv[1] #'HIG-RunIIFall18wmLHEGS-03028'
    field_to_update = 'tags'

    mcm.delete('requests', request_prepid_to_update)
    # sys.exit(1)
    
