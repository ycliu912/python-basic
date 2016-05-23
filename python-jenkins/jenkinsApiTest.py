#-*-coding:utf-8 -*-
#http://python-jenkins.readthedocs.io/en/latest/examples.html

import jenkins as jk
import json
import demjson
import time
import ConfigParser
from xdg.Menu import tmp
from operator import __eq__


cf = ConfigParser.ConfigParser()
cf.read("jenkins.conf")

jenkins_server_url_value = cf.get("jenkins_conf", "jenkins_server_url")
jenkins_server_url = jenkins_server_url_value.strip('\'"')
user_id = cf.get("jenkins_conf", "user_id").strip('\'"')
jenkins_token = cf.get("jenkins_conf","api_token").strip('\'"')

def json_dumps(src_info):
    jsonDumpsIndentStr = json.dumps(src_info,indent=1)
    print "src_info=",jsonDumpsIndentStr
    return;
    

#实例化jenkins对象，链接远程的jenkins master serversection
server=jk.Jenkins(jenkins_server_url,username=user_id,password=jenkins_token)

print "server.jobs_count() = ",server.jobs_count()
print "server.get_queue_info() = ",server.get_queue_info()

version = server.get_version()
print "version = ",version

job_info_00_parent160518 = server.get_job_info('00_parent160518', 1)
#print job_info_00_parent160518
#json_dumps(job_info_00_parent160518)
#f = json.load(job_info_00_parent160518).keys
#print f
#print f.keys()


f = demjson.encode(job_info_00_parent160518)
print f
print json_dumps(f)
print f.count('kind')
print f.find('actions')
print "f.find('alionline')",f.find('alionline')
print f.index("actions")

#print f.keys()
#print f.values()



#tmp = server.get_all_jobs(None)
#print tmp
#json_dumps(tmp)

server.build_job('test-agency')

#print "server.get_running_builds() = ",server.get_running_builds()
builds = server.get_running_builds()
builds = demjson.encode(builds)
print 'builds.find("test-agency")',builds.find("test-agency")
builds = builds.find("test-agency")
print "server.get_running_builds() type = ",builds
print "server.get_running_builds().count(test-agency) = ",type(server.get_running_builds().count('test-agency)'))
print "builds type = ",type("builds")
print "builds = ",builds

#builds = demjson.encode(builds)
#builds = json.load(builds)

#print "build as demjson.encode: ",build
#print "keys: ",builds.keys()
#print "keys: " ,builds.keys()
#print "values: ",builds.values
#print "info: " ,builds.find("name")
'''


#builds = json.loads(builds)
#print "json.JSONEncoder(builds):",builds

builds = json_dumps(builds)
'''


#builds = json.dumps(builds)
#print "json.dumps: ",builds


#实现判断job正在运行的逻辑，若运行，则给出提示，若一结束，则提示结束并退出
while (builds > 0):
    print "test-agency is building."
    time.sleep(3)
    builds = server.get_running_builds()
    print "server.get_running_builds() = ",builds
    builds = demjson.encode(builds)
    print "demjson.encode(builds) = ",builds
    builds = builds.find("test-agency")
    print "builds.find('test-agency') = ",builds
    #continue
    if (builds < 0):
        print "builds for test-angency is stopped."
        builds = server.get_running_builds()
        print "server.get_running_builds() = ",builds
        builds = demjson.encode(builds)
        print "demjson.encode(builds) = ",builds
        builds = builds.find("test-agency")
        print "builds.find('test-agency') = ",builds
        break
    continue
    

'''   

for i in range(1,100):
    builds = server.get_running_builds()
    print builds
    json_dumps(builds)
    time.sleep(3)
  


queue_info = server.get_queue_info()
json_dumps(queue_info)

job_info_00_parent160518 = server.get_job_info('00_parent160518', 1)
print job_info_00_parent160518
json_dumps(job_info_00_parent160518)
'''
#demoDictList is the value we want format to output
#jsonDumpsIndentStr = json.dumps(tmp,indent=1,encoding='utf-8')
#print "jsonDumpsIndentStr=",jsonDumpsIndentStr