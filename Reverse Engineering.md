<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 8.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**<span style="text-decoration:underline;">EZ (pass0.py)</span>**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse0.png "image_tooltip")


It’s right in the code…

**<span style="text-decoration:underline;">PZ (pass1.py)</span>**

What’s executed out of global space?



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse1.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse1.png "image_tooltip")


What’s main call?



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse2.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse2.png "image_tooltip")


What’s in checkpass()?



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse3.png "image_tooltip")


There we go.

**<span style="text-decoration:underline;">LEMON (pass2.py)</span>**

Same thing as before, track main() to checkpass().  Only this time they are doing text slicing:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse4.png "image_tooltip")


rtcp{y34H_tHiS_a1nT_sEcuR3} when you append it all correctly.

**<span style="text-decoration:underline;">SQUEEZEY (pass3.py)</span>**

This one was a little different as it needed some actual RE work to reverse the flow.  Basically, the code takes your input and XOR’s the hex equivalent of the text turning it back into a character before base64 encoding it and comparing it against a known string.  Quick investigation revealed the base64 decoded string is symmetric with the key, so that makes life easier.

To reverse it, I wrote a simple piece of code to handle the functions:

--- repass3.py --

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

------

Executing this gets you:



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse5.png "image_tooltip")


**<span style="text-decoration:underline;">thedanzman (pass4.py)</span>**

As with SQUEEZY, except there was some ROT13 thrown in the mix for hilarity.  Seriously…



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse6.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse6.png "image_tooltip")


The nope function performs the same hex XOR as in SQUEEZY, but the wow function this time does a string reversal (i.e. foo[::-1]) which if we look at result, the base64 there has been reversed (easy to tell because the padding character was at the end, making it more byte symmetric would have introduced more hilarity).  Interestingly enough, this time the key and text were not symmetric leading to the need to toss in the modulo to get it into the appropriate space for decryption.

So pulling this apart structurally led me to a code snippet:

--- repass4.py ---

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

------

Which when executed gives you this:



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/up-Reverse7.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/up-Reverse7.png "image_tooltip")
