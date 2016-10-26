import os, sys, requests

# Loader fetchs latest file from the server and calls a default method.
# loader.py is added to /etc/rc.local to run it on the boot up.
# This program uses python requests for server communcation.

print "\n------***-----Loader Version 8.6-1-----***-----\n"
print "\n EX:- sudo python loader.py 'url', 'http://192.168.1.241/xyz'"

# ------------  Customizable Variables: Start ------------------
# server URL 
url_code_loader = "http://192.168.3.242/otf/api/clientcode/getlatestcode?filename="
# number of server retries on error
num_of_retries = 2
# local  direcotry to the location where files need to be updated
local_path = "/home/pi/"
# file name to load
load_file_name = "piclient.py"
# ------------  Customizable Variables: END  -------------------

# get_file method takes two arguments(file name which is fetched from server and the Server URL[which defaults if nothing passed])
def get_file(saveFileName, urlstr=url_code_loader):
	r = get_url(urlstr + saveFileName)
	if r.status_code != 200: # on error dont update
		return r
	rnew = r.text.replace('\r\n', '\n')
	fil = open(saveFileName, 'w')
	fil.write(rnew)
	fil.close()
	return r

# get_url method makes actual call to server
def get_url(urlstr, pars=None):
	for t in range(num_of_retries):
		r = requests.get(urlstr, params=pars)
		if r.status_code == 200: 
			break
		print " Server connection failed retring :status code failed:-" + str(r.status_code)
	print "[1] Status code:-" + str(r.status_code), urlstr
	return r

# run_loader method can also be called from command line or other programs with a different URL
# python loader.py 'url', 'http://192.168.1.241/xyz'
def run_loader():
	args = sys.argv	
	lftp = False
	if len(args) > 1:
		if args[1] == "url":
			lftp = True
	if lftp:
		saveFileName = args[3]
		get_file(args[2], args[3])
	else:
		get_file("loader.py") #update loader.py first
		get_file(load_file_name)
		mod = __import__(testName)
		mod.start_app()
		
os.chdir(local_path)		
# on load call run_loader()		
run_loader()
#print "\n", " ++++++++ENDED+++++++\n"