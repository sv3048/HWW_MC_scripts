import sys
import json
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from collections import defaultdict
from collections import OrderedDict
import numpy as np
import pandas as pd

mcm     = McM(dev = False, debug = True)

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

# M = 200 GeV is not below because corresponding requests were already created
#masses = [  '160', '170', '180', '190', '210', '230', '250', '270', '300', '350', '400', '450', '500', '550', 
#            '600', '700', '800', '900', '1000', '1500', '2000', '2500', '3000']

 # M = 200 GeV is not below because corresponding requests were already created
masses = [  '160', '170']
prepid_M200_20UL16 = {  'GGH' : 'HIG-RunIISummer20UL16wmLHEGEN-11100', 
                        'GGH_minloHJJ' : '', # minloHJJ still has to be created
                        'VBFH' : 'HIG-RunIISummer20UL16wmLHEGEN-11929',
                        'ZH_LNuQQ_2LFilter' : 'HIG-RunIISummer20UL16wmLHEGEN-11931',
                        'ZH_LNuQQ' : 'HIG-RunIISummer20UL16wmLHEGEN-11932', 
                        'WminusH_2LOSFilter' : 'HIG-RunIISummer20UL16wmLHEGEN-11933', 
                        'WplusH_2LOSFilter' : 'HIG-RunIISummer20UL16wmLHEGEN-11934', 
                        'ZH' : 'HIG-RunIISummer20UL16wmLHEGEN-11935'
                    }

for mode, pi in prepid_M200_20UL16.items():
    print mode, pi
    if mode == 'GGH_minloHJJ':
        continue
    req = mcm.get('requests', pi)
    for mass in masses:
        print mass
        '''
        req['dataset_name'] = req['dataset_name'].replace('M-200', 'M-' + mass)
        print req['dataset_name']
        #req['member_of_campaign'] = 'RunIISummer20UL16wmLHEGENAPV'
        #req['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'
        #req['member_of_campaign'] = 'RunIISummer20UL18wmLHEGEN'
        req['fragment'] = req['fragment'].replace('M200', 'M' + mass)
        #print req['fragment']
        if '17' in req['member_of_campaign'] or '18' in req['member_of_campaign']:
            req['total_events'] = 500000
        mcm.update('requests', req)
        
       '''
        new_req  = mcm.clone_request(req)
        new_req['dataset_name'] = new_req['dataset_name'].replace('M-200', 'M-' + mass)
        #print req['dataset_name']
        #req['member_of_campaign'] = 'RunIISummer20UL16wmLHEGENAPV'
        #req['member_of_campaign'] = 'RunIISummer20UL17wmLHEGEN'
        #req['member_of_campaign'] = 'RunIISummer20UL18wmLHEGEN'
        new_req['fragment'] = new_req['fragment'].replace('M200', 'M' + mass)
        #print req['fragment']
        if '17' in req['member_of_campaign'] or '18' in req['member_of_campaign']:
            req['total_events'] = 500000
        new_req = mcm.update('requests', new_req)
        print new_req
        mcm.approve('requests', new_req['prepid'], 0)
        
        
