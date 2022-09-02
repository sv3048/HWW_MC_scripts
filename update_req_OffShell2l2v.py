#for modifying time/event for the requets

import sys
import json
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from collections import defaultdict
from collections import OrderedDict
import numpy as np
import pandas as pd


mcm     = McM(dev = False, debug = True)


#import list of requests need to be deleted
import prepid_update_vf
from prepid_update_vf import ls


def get_request(prepid):
   result  = mcm._McM__get('public/restapi/requests/get/%s' % (prepid))
   if not result:
        return {}
   result  = result.get('results', {})
   return result
   
def get_requests_from_datasetname(dn):
    result  = mcm.get('requests', query='dataset_name=%s' % (dn))
    if not result:
        return {}
    return result


for  pid in ls:
    print pid
    req = mcm.get('requests', pid)
    if req==None :
      print( "request don't exist")
    else: 
      req[field_to_update] = memory
      mcm.update('requests', req) 
       
     
