#========
# this script will update a given request's nThread 
# uses: python modify_request_memory.py prep-id memory
# e.g. python modify_request_memory.py HIG-RunIIFall17wmLHEGS-00545 2300
#========          

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from argparse import ArgumentParser
from listOfFunctions import *

parser = ArgumentParser()
parser.add_argument('--prepid', type=str, help="check mcm requests using prepids",dest="prepid")
parser.add_argument("--memory",type=int, help="memory should be 4000 (otherwise 2300 if 1 core)",dest="memory")
parser.add_argument('--lowerprepid', type=str, help="lowest prepid",dest="lowerprepid")
parser.add_argument('--upperprepid', type=str, help="upper prepid",dest="upperprepid")
parser.add_argument('--activeRange',dest="activeRange", default=False, help="use True or False")

args = parser.parse_args()

    
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

mcm = McM(dev=False)

# Example to edit a request parameter(-s) and save it back in McM
# request_prepid_to_update = 'HIG-Summer12-01257' # Doesn't exist
#given_req = sys.argv[1]
if(args.activeRange):
    prepidlists = ListOfPrepids(args.lowerprepid,args.upperprepid)
    print('prepidlists',prepidlists)

#prepids = parseIDList(args.prepid)
if(args.activeRange):
    prepids = prepidlists
else:
    prepids = parseIDList(args.prepid)

print('prepid',prepids)
print "Approving {0} base requests".format(len(prepids))

for prepid in prepids:

    request_prepid_to_update = prepid  #sys.argv[1] #'HIG-RunIIFall18wmLHEGS-03028'
    field_to_update = 'memory'

    #field_to_update = 'sequences'
    # get a the dictionnary of a request
    request = mcm.get('requests', request_prepid_to_update)

    if 'prepid' not in request:
        # In case the request doesn't exist, there is nothing to update
        print('Request "%s" doesn\'t exist' % (request_prepid_to_update))
    else:
        print('Request\'s "%s" field "%s" BEFORE update: %s' % (request_prepid_to_update,
                                                            field_to_update,
                                                            request[field_to_update]))

        # Modify what we want
        # time_event is a list for each sequence step
        request[field_to_update] = args.memory
        #print('check', request["sequences"][0]['nThreads'])
        #request[field_to_update][0]['nThreads'] = sys.argv[2]#'4'
        # Push it back to McM
        update_response = mcm.update('requests', request)
        print('Update response: %s' % (update_response))

        # Fetch the request again, after the update, to check whether value actually changed
        request2 = mcm.get('requests', request_prepid_to_update)
        print('Request\'s "%s" field "%s" AFTER update: %s' % (request_prepid_to_update,
                                                           field_to_update,
                                                           request2[field_to_update]))
