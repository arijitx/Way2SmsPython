#https://github.com/zed41
#http://zed41.blogspot.com
#ASCII_ART from http://patorjk.com/software/taag/

from mechanize import Browser
from bs4 import BeautifulSoup as BS
import urllib2

token="AUTO_GENERATED_TOKEN"
username="USERNAME"
password="PASSWORD"
br = Browser()
br.set_handle_robots(False)
br.set_handle_referer(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox'),('Connection','keep-alive'),('Keep-Alive', '115')]

def login(uName,pwd):
	br.open('http://site21.way2sms.com/content/index.html')
	br.select_form(name="lgnFrm")
	br['username']=uName
	br['password']=pwd
	br.submit()

def send_sms(number,message):
	mob=number
	msg=urllib2.quote(message)
	soup = BS(br.response().read(),"lxml")
	token=soup.find("input", {"name": "Token"})
	#print token.get('value')
	url='http://site21.way2sms.com/./smstoss.action?mobile='+mob+'&ssaction=ss&msgLen=140&message='+msg+'&Send=Send&Token='+str(token.get('value'))

	br.open(url)
	res=br.response().read()
	if br.response().code == 200 :
		return "success"
	else:
		print "fail"
def usage():
	f=open('ascii_art.txt','r')
	print f.read()
	print "login(Username,Password) #Way2Sms Username and Password"
	print "send_sms('9876543210','Hello!World!')"


