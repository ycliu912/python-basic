#-*-coding:utf-8 -*-

import jenkins as jk
import json
import ConfigParser
from xdg.Menu import tmp

cf = ConfigParser.ConfigParser()
cf.read("jenkins.conf")

jenkins_server_url_value = cf.get("jenkins_conf", "jenkins_server_url")
print jenkins_server_url_value.strip('\'"')
jenkins_server_url = jenkins_server_url_value.strip('\'"')
user_id = cf.get("jenkins_conf","user_id").strip('\'"')
print user_id
jenkins_token = cf.get("jenkins_conf","api_token").strip('\'"')
print jenkins_token

#实例化jenkins对象，链接远程的jenkins master serversection
server=jk.Jenkins(jenkins_server_url,username=user_id,password=jenkins_token)

job_info_00_parent160518 = server.get_job_info('00_parent160518', 1)
print job_info_00_parent160518
jsonDumpsIndentStr = json.dumps(job_info_00_parent160518,indent=1)
print "job_info_00_parent160518=",jsonDumpsIndentStr

#server.build_job('test-agency')

version = server.get_version()
print version

tmp = server.get_all_jobs(None)
#print tmp

#demoDictList is the value we want format to output
jsonDumpsIndentStr = json.dumps(tmp,indent=1,encoding='utf-8')
print "jsonDumpsIndentStr=",jsonDumpsIndentStr
print ""
