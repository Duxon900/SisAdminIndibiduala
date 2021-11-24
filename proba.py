# below is a extract from a sample exploit that
# interfaces with a tcp socket
from netcat import Netcat
import os

# sudo docker images | grep duxon/blob |awk '{print $3;}'
# blobcity irudia lortzeko
image = os.popen('sudo docker images | grep duxon/blob |awk \'{print $3;}\'').read()
image = image.replace('\n','')

# null bada irudia buildeatu
if image=='':
	print('kaixo')
	os.system('docker build dockerSimp/ -t duxon/blob:0.3')
	image = os.popen('docker images | grep duxon/blob').read()


# sudo docker run -p 10113:10113 -p 10111:10111 duxon/blob:0.3 ??


# start a new Netcat() instance
nc = Netcat('127.0.0.1', 10113)

# get to the prompt and write
nc.read_until(b'username>')
nc.write(b'root' + b'\n')
print('root idatzita...')

# start a new note
nc.read_until(b'password>')


# sudo docker ps | grep duxon/blob | awk '{print $1;}'
containerID = os.popen('docker ps | grep duxon/blob | awk \'{print $1;}\'').read()
containerID = containerID.replace('\n','')
# container ID(lehenengo zutabea da)

# lortu pasahitza
#print('docker exec ' + containerID + ' cat /data/root-pass.txt')
pasahitza=os.popen('docker exec ' + containerID + ' cat /data/root-pass.txt').read()


nc.write(str.encode(pasahitza))
print('pasahitza idatzita...')


# set note 0 with the payload
nc.read_until(b'blobcity>')
print('pingo')