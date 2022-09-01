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
import prepid_del_vfinal
from prepid_del_vfinal import ls


def get_request(prepid):
   result  = mcm._McM__get('public/restapi/requests/get/%s' % (prepid))
   if not result:
        return {}
   result  = result.get('results', {})
   return result



for  pid in ls:
    print pid
    req = mcm.get('requests', pid)
    if req==None :
      print( "request don't exist")
    else: 
       mcm.approve('requests', pid, 0)
       mcm.delete('requests', pid)
            
