import base64
import codecs

key = "nyameowpurrpurrnyanyapurrpurrnyanya"
key = codecs.encode(key, "rot_13")

final = '=ZkXipjPiLIXRpIYTpQHpjSQkxIIFbQCK1FR3DuJZxtPAtkR'
final = final[::-1]

step1 = codecs.encode(final, 'rot_13')
step2 = base64.b64decode(step1, altchars=None)

data = []
step=0
for a in step2:
    data.append(chr(ord(a) ^ ord(key[step%35])))
    step+=1

print ''.join(data)
