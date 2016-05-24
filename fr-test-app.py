import bottle
import requests
import json
import os
import logging
import re
import sys
import settings

#The contents of this file are subject to the terms of the 
#Common Development and Distribution License (the License). 
#You may not use this file except in compliance with the License.
#You can obtain a copy of the License at: 
#https://opensource.org/licenses/CDDL-1.0. 
#See the License for specific language governing permission and 
#limitations under the License.
#
#
#Copyright 2016 ForgeRock, Inc. All Rights Reserved.
#
#running in Cloud Foundry?
if 'VCAP_APPLICATION' in os.environ:
    vcap_application = json.loads(os.environ['VCAP_APPLICATION'])
    if (vcap_application.get('application_id',0) and vcap_application.get('application_name',0)):
        ##yes running in CF
        logging.basicConfig(stream=sys.stdout,level=logging.DEBUG,format='%(asctime)s %(message)s')      
else:
    #running locally
    client_id = settings.username
    client_secret = settings.password
    #openam_URL = "http://openam.54.200.251.54.xip.io:8080/"
    openam_URL = settings.am_URL
    current_file = re.split("\.",os.path.basename(__file__))
    logging.basicConfig(filename=(current_file[0] + '.log'),level=logging.DEBUG,format='%(asctime)s %(message)s')

logging.info('Started')

#setup headers
http_content_type_json = {'Content-Type':'application/json'}
headers = http_content_type_json

#setup URL
#https://backstage.forgerock.com/#!/docs/openam/13/dev-guide%23rest-api-oauth2-client-endpoints
openam_oauth_token_validation = "openam/oauth2/tokeninfo"
oauth_query_string = "?access_token="
#Forgerock endpoints



if 'VCAP_SERVICES' in os.environ:
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    if 'fr-openam' in vcap_services:
        fr_openm_env = vcap_services['fr-openam'][0]
        oauth_cred = fr_openm_env['credentials']
        client_id = oauth_cred['username']
        client_secret = oauth_cred['password']
        openam_URL = oauth_cred['uri']
        logging.debug('VCAP_SERVICES available')
        logging.debug('client_id = %s', client_id)
        logging.debug('client_secret = %s',  client_secret[1:8])
        logging.debug('uri = %s', openam_URL)

#
#
#  /oauthinfo
#
#
@bottle.route('/oauthinfo', method='GET')
def oauthinfo():
    """
    Return the oauth token, and validation response from openam

    """   
    theresponse = {}
    error_response = {}

    auth_header = bottle.request.headers.get('Authorization')
    # grab incoming oauth token from auth_header
    # format of auth_header should be "Authorization: Bearer mF_9.B5f-4.1JqM"
    #response = "Authorization Header:" + auth_header
    temp = auth_header.split()
    logging.debug('auth header =%s',auth_header)
    oauth_token = temp[1]
    logging.debug('oauth token =%s',oauth_token)
    #return (test)

    url = openam_URL + openam_oauth_token_validation + oauth_query_string + oauth_token

    #get_result = requests.get(url,headers=headers,auth=(client_id, client_secret))
    #result_dict = openam_.json()

    #Everything is ok, let's POST to openam to register client
    #
    try:
        openam_response = requests.get(url,headers=headers,auth=(client_id, client_secret))
        #openam_response = requests.post(url, json={"redirect_uris":["https:/foo.com/register"]}, headers=headers,timeout=(10.0,10.0))
        openam_response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        bottle.response.status = 500
        error_response['error'] = str(e.args[0])
        logging.debug('Connection Error:  %s ',str(e.args))
        logging.debug('Connection error to %s',url)
        return dict(data=error_response)
    except requests.exceptions.ConnectTimeout as e:
        error_response['error'] = 'Connection Timeout to ' + setting.am_URL
        logging.debug('Error: Connection Timeout to %s',url)
        logging.debug('Error: result.statuscode = %s',openam_response.status_code)
        return dict(data=error_response)
    except requests.exceptions.HTTPError as e:
        bottle.response.status = openam_response.status_code
        error_response['error'] = e.args[0]
        logging.debug('HTTP Error:  %s ',e.args[0])
        return dict(data=error_response)

    result_dict = openam_response.json()

    #return the results 
    theresponse = result_dict
    bottle.response.status = openam_response.status_code

    #Request Failed
    if openam_response.status_code != 200:
        logging.debug('request Failed')
        logging.debug('request url=%s',url)
        logging.debug('request headers=%s',headers)
        logging.debug('request failed statsuscode=%s',openam_response.status_code)

    #Request Succeeded
    if openam_response.status_code == 200:
        if (result_dict.get('expires_in',0)):
            if result_dict['access_token'] == oauth_token:
                logging.debug('token is valid expires_in=%s',result_dict['expires_in'])
                logging.debug('Success status code = %s',openam_response.status_code)
                logging.debug('oauth_token=%s',oauth_token)
                logging.debug('expires_in=%s',result_dict['expires_in'])
                logging.debug('token_type =%s',result_dict['token_type'])
                logging.debug('json result =%s',openam_response.json())
            else:
                logging.debug('Failure! tokens do not match %s != %s',result_dict['access_token'],oauth_token)

    #return (client_id,client_secret,oauth_URL)
    return json.dumps(theresponse)



if __name__ == '__main__':
    port = int(os.getenv('PORT', '8080'))
    bottle.run(host='0.0.0.0', port=port, debug=True, reloader=False)
   