#!/usr/bin/env python

# Dork Scraper
#
# ORHOund is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Knock is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Knock. If not, see <http://www.gnu.org/licenses/>.

# Python libraries
import sys
import time
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

class colors:
    HEADER = '\033[1;35m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKCYANL = '\033[1;36m'
    OKGREEN = '\033[92m'
    OKGREENL = '\033[1;32m' 
    OKREDL = '\033[1;31m' 
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
	print(colors.HEADER  + """
"       ___           _        ___         _   
"      /   \___  _ __| | __   / __\_ _ ___| |_ 
"     / /\ / _ \| '__| |/ /  / _\/ _` / __| __|
"    / /_// (_) | |  |   <  / / | (_| \__ \ |_ 
"   /___,' \___/|_|  |_|\_\ \/   \__,_|___/\__|
                                                                                                 
""" + colors.ENDC)
	print(colors.WARNING + "DorkFast | " + colors.OKGREEN + "Cod3d By: " + colors.WARNING + "CapitosKamal | " + colors.OKGREEN + "Instagram: " + colors.WARNING + "https://www.instagram.com/capitoskamal/" + colors.ENDC)

#CORE FUNCTION
def getUrls(dork,number_webs,enable_save,filename):

	print (colors.OKCYAN + "Starting DorkFast to recollect all the URLs that appear with the dork " + colors.FAIL + dork + colors.ENDC)
	
	pages = 0
	
	try:
		for results in search(dork, tld="com", lang="es", num=number_webs, start=0, stop=None, pause=2):
			print (results)
			time.sleep(0.2)
			
			pages += 1
			
			if pages >= number_webs:
				break
			
			data = (results)
			
			if enable_save == 1:
				file = open(filename, "a")
				file.write(str(data))
				file.write("\n")
				file.close()
				
	except HTTPError:
		if e.code == 429:
		     print (colors.FAIL + "ERROR: Too Many Requests detected\n" + colors.ENDC)
		     print (colors.FAIL + "You need waiting a bit..." + colors.ENDC)

#MAIN FUNCTION
def main():
	banner()
	enable_save = 0
	filename = ""

	if len(sys.argv) == 1:
		print (colors.FAIL + "ERROR: No dork or parameters found" + colors.ENDC)
	elif len(sys.argv) == 2:
		arg = sys.argv[1]
		
		if arg == "-h" or arg == "--help" :
			print (colors.BOLD + "HELP SECTION:" + colors.ENDC)
			print ("Usage:" + colors.OKCYAN + '\tdockerscraper.py "dork" number_of_websites' + colors.ENDC)
			print ("Example:" + colors.OKCYAN + '\tdockerscraper.py "inurl:admin" 5 -s output.txt' + colors.ENDC)
			print ("-d,--dork" + colors.OKCYAN + "\tSpecifies the dork to use in the tool" + colors.ENDC)
			print ("-h,--help" + colors.OKCYAN + "\tThis help" + colors.ENDC)
			print ("-v,--version" + colors.OKCYAN + "\tShow version" + colors.ENDC)
			print ("-s,--save" + colors.OKCYAN + "\tEnable save output and specifies the output file" + colors.ENDC)
		elif arg == "-v" or arg == "--version":
			print (colors.WARNING + "DorkFast" + colors.ENDC)
		else:
			print (colors.FAIL + "ERROR: Incorrect argument or sintaxis" + colors.ENDC)
			
	elif len(sys.argv) > 2 and len(sys.argv) <= 6:

		if sys.argv[1] == "-d" or sys.argv[1] == "--dork":
			
			dork = sys.argv[2]
			number_webs = int(sys.argv[3])
			
			if(len(sys.argv) > 4):
				if sys.argv[4] == "-s" or sys.argv[4] == "--save":
					enable_save = 1
					filename = sys.argv[5]

			getUrls(dork,number_webs,enable_save,filename)
				
main()