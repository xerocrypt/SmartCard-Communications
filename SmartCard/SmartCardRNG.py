from smartcard.System import readers
from smartcard.util import toHexString

#Print connected reader details
r = readers()
print r

#Connect to reader and card
connection = r[0].createConnection()
connection.connect()

i=0
while i < 100:
	#Replace with APDU instruction of whatever card
	SELECT = [0x80, 0x84, 0x00, 0x00, 0x08]
	nextRandom = connection.transmit(SELECT)
	print nextRandom
	i= i +1;
