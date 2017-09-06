from random import choice
import sys
map_range= int(sys.argv[2])*int(sys.argv[2])
with open(sys.argv[1],'w') as _map:
	for i in range(map_range):
		_map.write(choice(".*"))
