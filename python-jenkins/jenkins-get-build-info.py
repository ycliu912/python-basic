#!/usr/bin/env python
#coding:utf-8

#-*-coding:utf-8 -*-
#http://python-jenkins.readthedocs.io/en/latest/examples.html

import jenkins as jk
import json
import demjson
import time
import os
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


builds = server.get_running_builds()
print "server.get_running_builds() = ",builds

#build00 = builds01 = server.get_job_info('test-agency')['lastBuild']
build00 = builds01 = server.get_job_info('test-agency')
print "builds01 = server.get_job_info('test-agency')['lastBuild'] = ",build00
#print json_dumps(build00)

#获取job名为job_name的job的最后次构建号
builds01 = server.get_job_info('test-agency')['lastBuild']['number']
print "server.get_job_info('test-agency')['lastBuild']['number'] = ",builds01

builds02 = server.get_build_info('test-agency',159)
print "server.get_build_info() = ",builds02
#print json_dumps(builds02)

 #判断job名为job_name的job的某次构建是否还在构建中
builds03 = server.get_build_info('test-agency',159)['building']
print "server.get_job_info('test-agency')['building'] = ",builds03

#判断job名为job_name的job的某次构建的执行结果状态
builds04 = server.get_build_info('test-agency',159)['result']
print "server.get_build_info('test-agency',159)['result'] = ",builds04

#获取svn revision
builds05 = server.get_build_info('test-agency',159)['changeSet']['revisions'][0]['revision']
builds06 = server.get_build_info('test-agency',159)['changeSet']['revisions'][0]['module']
print "server.get_build_info('test-agency',159)['changeSet']['revisions'] type = ",type(server.get_build_info('test-agency',159)['changeSet']['revisions'])
print "sever.get_build_info('test-agency','lastBuild')['revisions']['revision'] = ",builds05
print "server.get_build_info('test-agency',159)['changeSet']['revisions'][0]['module'] = ",builds06
print "builds05.type = ",type(builds05)
#print "builds05.version = ",builds05[0]['revision']


builds = server.get_running_builds()
builds = demjson.encode(builds)
builds = builds.find("test-agency")
print 'builds.find("test-agency") = ',builds
print "server.get_running_builds() type = ",builds
print "server.get_running_builds().count(test-agency) = ",type(server.get_running_builds().count('test-agency)'))
print "builds type = ",type("builds")
print "builds = ",builds


#实现判断job正在运行的逻辑，若运行，则给出提示，若一结束，则提示结束并退出
#1 job build 后立刻查看没有得到状态
while (builds > 0):
    print "test-agency is building."
    time.sleep(3)
    builds = server.get_running_builds()
    print "server.get_running_builds() = ",builds
    builds = demjson.encode(builds)
    print "demjson.encode(builds) = ",builds
    builds = builds.find("test-agency")
    print "builds.find('test-agency') = ",builds
   # get_pid_status(pid_build)
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
