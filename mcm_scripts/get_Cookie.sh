#!/bin/bash
echo "Delete existing cookies"
rm -rf ~/private/*-cookie.txt
echo "if that fails, it because a release had been setup first ..."
cern-get-sso-cookie -u https://cms-pdmv-dev.cern.ch/mcm/ -o ~/private/cookie.txt --krb
cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb
#cern-get-sso-cookie -u https://cms-pdmv-int.cern.ch/mcm/ -o ~/private/int-cookie.txt --krb #Error: Cannot authenticate to: https://cms-pdmv-int.cern.ch/mcm/
cern-get-sso-cookie -u https://cms-pdmv-dev.cern.ch/mcm/ -o ~/private/dev-cookie.txt --krb
# this line works shoud be there
cern-get-sso-cookie --url https://cms-pdmv-dev.cern.ch/mcm/ -o dev-cookie.txt
cern-get-sso-cookie --url https://cms-pdmv.cern.ch/mcm/ -o prod-cookie.txt
