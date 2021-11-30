# below is a extract from a sample exploit that
# interfaces with a tcp socket
from netcat import Netcat
import os
import time

# lortu blobcity-ren IPa konektatzeko

# ip lortzeko sudo docker network inspect -f '{{json .IPAM.Config}}' bridge | jq -r .[].Gateway

def hasi():
	try:
		nc = Netcat('servidor-blobcity', 10113)
	except ConnectionRefusedError:
		time.sleep(2)
		nc = hasi()
	return nc



# start a new Netcat() instance
nc = hasi()



# get to the prompt and write
nc.read_until(b'username>')
nc.write(b'root' + b'\n')
print('root idatzita...')

# start a new note
nc.read_until(b'password>')


# pasahitza lortu
pasahitza = os.popen('cat /datuak/root-pass.txt').read()
print(pasahitza)
pasahitza = pasahitza.replace('\n','')



nc.write(str.encode(pasahitza) + b'\n')
print('pasahitza idatzita...')


# datu basea sortu
nc.read_until(b'\nblobcity>')
nc.write(b'create-ds pingo' + b'\n')

# bilduma sortu(taula)
nc.read_until(b'blobcity>')
nc.write(b'create-collection pingo.test' + b'\n')


# insertak
nc.read_until(b'blobcity>')
nc.write(b'insert into pingo.test JSON' + b'\n')

nc.read_until(b'and press enter to insert\n')

nc.write(b'{"col1": 1, "col2": 2}' + b'\n')
nc.read_until(b'Inserted\n')
nc.write(b'{"col1": 3, "col2": 4}' + b'\n')
nc.read_until(b'Inserted\n')


# idazteko modutik ateratzeko
nc.write(b'exit' + b'\n')

nc.read_until(b'blobcity>')
nc.write(b'sql test: select col1,col2 from pingo.test' + b'\n')


print('pingo')