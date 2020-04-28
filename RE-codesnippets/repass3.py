import base64

final = 'HxEMBxUAURg6I0QILT4UVRolMQFRHzokRBcmAygNXhkqWBw='
key = 'meownyameownyameownyameownyameownya'


step1 = base64.b64decode(final, altchars=None)
step=0
data = []
for a in step1:
    data.append(chr(ord(a) ^ ord(key[step])))
    step+=1

print ''.join(data)
