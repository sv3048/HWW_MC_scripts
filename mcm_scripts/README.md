# McM Scripts
Repository for using McM scripts and example scripts

## All you need
```
source get_Cookie.sh
e.g. do python modify_request_core.py -h
# To change core:
python modify_request_core.py --prepid HIG-RunIIFall18wmLHEGS-03028 --core 2
# To change memory:
python modify_request_memory.py --prepid HIG-RunIIFall18wmLHEGS-03028 --memory 2100
# To approve for next steps:
python request_approve.py --prepid HIG-RunIIFall18wmLHEGS-03028 0
```


### Basic info
* Link to McM: https://cms-pdmv.cern.ch/mcm/
* McM Rest API: https://cms-pdmv.cern.ch/mcm/restapi
* For most actions you will NEED to have a valid CERN SSO cookie
* Public APIs do not require a cookie. Index of public API: https://cms-pdmv.cern.ch/mcm/public/restapi/

### CERN SSO cookie
* Use `cern-get-sso-cookie` command line tool to generate it:
    * `cern-get-sso-cookie --url https://cms-pdmv-dev.cern.ch/mcm/ -o dev-cookie.txt`
    * `cern-get-sso-cookie --url https://cms-pdmv.cern.ch/mcm/ -o prod-cookie.txt`
* `cern-get-sso-cookie` is already available in lxplus nodes
* It expires after ~10 hours, so be sure to regenerate it
* Dev cookie is valid only for dev environment and production cookie is valid only for production environment

### Priority change
* If you want to use priority changing scripts or do anything else related to cmsweb, you'll have to use voms-proxy:
    * `voms-proxy-init -voms cms`
    * `export X509_USER_PROXY=$(voms-proxy-info --path)`
