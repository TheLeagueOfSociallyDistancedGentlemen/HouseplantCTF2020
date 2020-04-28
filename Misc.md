#Spilled Milk
### 50 Points
oh no! i'm so clumsy, i spilled my glass of milk! can you please help me clean up?

spilled_milk.png (9ac853b9527a08919f9c94172074a69d)
### Solution:
### Flag:

# Zip-a-Dee-Doo-Dah
### 129 Points
I zipped the file a bit too many times it seems... and I may have added passwords to some of the zip files... eh, they should be pretty common passwords right?

Hint! A script will help you with this, please don't try do this manually...
Hint! All passwords should be in the SecLists/Passwords/xato-net-10-million-passwords-100.txt file, which you can get here : https://github.com/danielmiessler/SecLists/blob/master/Passwords/xato-net-10-million-passwords-100.txt
or alternatively, use "git clone https://github.com/danielmiessler/SecLists"

1819.gz (2c1ce0c0f7efb5ddfac82390aeada827)
### Solution:
This one was a bunch of nested archives of differing formats. Zips being password encoded. So I scripted this and used `fcrackzip` with the provided password list to handle password cracking.

```bash
#!/bin/bash

while [ true ]
do
  file=`ls -1| grep -v *.sh | grep -v txt`

  echo "Runnin on $file"
  if [ `file $file | grep -c tar` -gt 0 ]
  then
    tar xvf $file
    rm $file
  elif [ `file $file | grep -c gzip` -gt 0 ]
  then
    if [ "{${file##*.}}" != "{gz}" ]
    then
      mv $file "${file}.gz"
      file="${file}.gz"
    fi
    gunzip $file
  elif [ `file $file | grep -c 'Zip archive'` -gt 0 ]
  then
    for pass in $(fcrackzip -D -p words.txt  $file  | cut -d ' ' -f 4)
    do
        echo "Trying $pass"
        unzip -o -P $pass $file
        if [ $? -eq 0 ]
        then
          echo "Success"
          rm $file
          continue
        fi
    done
  fi
done
```

### Flag:
rtcp{z1pPeD_4_c0uPl3_t00_M4Ny_t1m3s_a1b8c687}

# Music Lab
### 207 Points
Do you like my song? ♪

masterpiece.mid (3cf79ff90abc4eb76f22f33adf636189)
### Solution:
I just opened this one up in Audacity and the flag was written out in the notes. The most frustrating part of this one was figuring out which character to use in the flag.

![Masterpiece](https://raw.githubusercontent.com/TheLeageOfSociallyDistancedGentlemen/HouseplantCTF2020/master/img/masterpiece.png)
### Flag:
rtcp{MOZ4rt_WOuld_b3_proud}

# Satan's Jigsaw
### 704 Points
Oh no! I dropped my pixels on the floor and they're all muddled up! It's going to take me years to sort all 90,000 of these again :(

Hint! long_to_bytes

chall.7z (a9bd676256e2cf8a5ca893a9928aaa16)
### Solution:
The provided 7z file contained a bunch of images with long numerical filenames. The hint made it obvious that you needed to use long_to_bytes on those. The resulting string were two integers.

Each image was a single pixel, so it became obvious that we just had to place each pixel at the coordinates listed, so I wrote a python script using PIL.
```
from Crypto.Util.number import long_to_bytes
import os
from PIL import Image, ImageDraw

mapping={}
max_x = 0
max_y = 0

# Map image to pos
for filename in os.listdir('./'):
    if filename.endswith('.jpg'):
      pos = long_to_bytes(filename.replace('.jpg',''))
      mapping[filename] = [int(pos.split(" ")[0]), int(pos.split(" ")[1])]

# Find max x and y
for pos in mapping.items():
    print pos[1]
    if pos[1][0] > max_x:
        max_x = pos[1][0]
    if pos[1][1] > max_y:
        max_y = pos[1][1]

# Create the new image
img = Image.new('RGB',(max_x,max_y), color=0)
for image in mapping:
    x = mapping[image][0]
    y = mapping[image][1]
    im = Image.open(image)
    region = im.crop((0,0,1,1))
    img.paste(region,(x,y,x+1,y+1))

img.save('test.png')

```

That resulted in this image

![satans_jigsaw](https://raw.githubusercontent.com/TheLeageOfSociallyDistancedGentlemen/HouseplantCTF2020/master/img/satans_jigsaw.png)

One of those QR codes is a rickroll, the other is the flag!

### Flag:
rtcp{d1d-you_d0_7his_by_h4nd?}

# I only see in cubes
### 1,547 Points
SOLVED
Oh no! Jubie's been travelling through distant lands and she lost her books! She'd put so much work into writing them, it'd be a shame if they were lost forever. You never know, you might be rewarded if you find them...

Hint! You don't need to own a copy of Minecraft to solve this challenge. You also don't need to pirate a copy of Minecraft to solve this challenge. Piracy bad.

I only see in cubes rezip.7z (c1450ca404a110f66dea46bb70f0265a)
### Solution:
They made it pretty clear the files here were for minecraft, so I looked into how those files work. That lead me to some tools that can be used to read them, including [NBTExplorer](https://github.com/jaquadro/NBTExplorer), which can be used to crawl through these files.

The zip had some weirdness where it tried to overwrite files on unpacking. Strange. So initially I let it do that.

Poking manually through the files I found one book in the player's inventory which showed me that the books would have an ID of `minecraft:written_book`. So I searched for that in the rest of the files and initially I could only find two parts on the flag.

So I went back and unzipped the package again, but didn't allow the overwrite this time. The first part of the flag was in that set of files.

### Flag:
???
