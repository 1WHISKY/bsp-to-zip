import sys
import os

if len(sys.argv) < 2:
  sys.exit()
  
path = sys.argv[1]
basename = os.path.basename(path)
  
mapfile = open(path,"rb")
content = mapfile.read()
mapfile.close()

#NUL P K ETX EOT
offset = content.find(b'\x00\x50\x4b\x03\x04') + 1
if offset == 0:
  print("couldn't find packed content.")
  input()
  sys.exit()
  
newfile = path + "/../" + basename.replace(".bsp",".zip")
print("writing output to " + newfile)

output = open(newfile,"wb")
output.write(content[offset:])
output.close()
