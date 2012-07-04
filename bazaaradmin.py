#!/usr/bin/python

# place it at ~/ or tweak yourself
LAB_HOME='/labs/'
DEBUG=False
def run_command(command=None):
    import commands
    if command is None:
        return ['1',"error"]
    response = commands.getstatusoutput(command)
    if DEBUG:
	print "command is "+command
	print response[1]
    return response

def request_parser(param):
    import json
    request = None
    try:
        request = json.loads(param)
    except e:
        print "Error parsing "+ e
    return request

def response_gen(response_obj):
    import json
    response = None
    try:
        response = json.dumps(response_obj)
    except e:
        print "unable to process to json "+ e
    return response



def create(labid,repo):
	# check if the repo exists 
	import os
	if os.path.exists(LAB_HOME+labid+'/'+repo):		
		return {'status' : 0 , 'summary' : 'repo exists'}
	# create the repo 
	repo_location = LAB_HOME+labid+'/'+repo
	#print repo_location
	run_command('cd '+ LAB_HOME+ labid + ' ;bzr init-repo '+repo+' ; chmod -R g+w '+repo)[1]
	run_command('mkdir -p /tmp/ldk')[1]
####################################
#since a developer can switch from one branch to another while developing in case of bazaar , we woild have to use bzr merge first and then bzr pull., so uncertainity :)
####################################
	run_command('bzr pull file://'+repo_location+' /tmp/ldk')[1]
##############
#assumming that the developer never switched branch
##############
	run_command('cp -r ldk/* /tmp/ldk')[1]
	run_command('cd /tmp/ldk ; svn add * ;bzr commit -m "LDK committed"')[1]
	run_command('cd /tmp; rm -rf /tmp/ldk')[1]
	# fix repo cache group write issue
	run_command('chmod g+w '+repo_location+'/db/rep-cache.db')
	return {'status' : 1 ,'summary' : 'Repo initialized with ldk' }

def discard(labid,repo):
	run_command('rm -rf '+LAB_HOME+labid+'/'+repo)
	return {'status' : 1 ,'summary' : 'Repo removed' }


if __name__ == '__main__':
    import sys
    params = sys.argv
    if params[1] == 'add':
    	response_obj = create(params[2],params[3])
    elif params[1] == 'discard': 
	response_obj = discard(params[2],params[3])
    print response_gen(response_obj)
