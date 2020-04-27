# **[Neko Hero](https://houseplant.riceteacatpanda.wtf/challenge?id=33)** 
### 50 Points

Please join us in our campaign to save the catgirls once and for all, as the COVID-19 virus is killing them all and we need to provide food and shelter for them!

nya~s and uwu~s will be given to those who donate!

and headpats too!

Dev: William

(and inspired by forwardslash from htb i guess)

### Solution:

### Flag:


# **[Deep Lyrics](https://houseplant.riceteacatpanda.wtf/challenge?id=55)** 
### 1,487 Points

Yay, more music!

Dev: Delphine

### Solution: 
One of my teammates suggested DeepSound.  Downloaded it in a VM.  Opened the .wav and tada….text file with the flag.

### Flag: 
rtcp{got_youuuuuu}


# **[Ezoterik](https://houseplant.riceteacatpanda.wtf/challenge?id=29)** 
### 1,833 Points

Inventing languages is hard. Luckily, there's plenty of them, including stupid ones.

Dev: Tom

Hint! You will find what you seek beyond the whitespace

[ezoterik.jpg](https://houseplant.riceteacatpanda.wtf/download?file_key=122f4f2192af3c2baf8e315604c4b155bb5a1b0cf55f32befbd77340484d1f3a&team_key=2f442c580703a2af3b72516afcab8f66a84d3ccd858d0f0cf199e4bdb28231cb) 2ccd8135a03c5936b6f0b4e989db8a30

### Solution:  
Opening the image there is a suspicious string of text.  I recognized the text from prior CTF’s as a language called “brainfuck”.  Lucky day, easy mode.  After copying it out and running it through a decoder it spit out “Yeah, no, sorry.”  Well played, sir.  While the image was running through some stego scripts I pulled it up in a hex editor and saw a very obvious string of text at the end of the file after some whitespace.  Probably what the clue was referring to.  Copy that out and you’ll get this block of text.  Looks like base64, right?  

2TLEdubBbS21p7u3AUWQpj1TB98gUrgHFAiFZmbeJ8qZFb9qCUc8Qp6o86eJYkrm2NLexkSDyRYd3X9sRCRKJzoZnDtrWZKcHPxjoRaFPHfmeUyoxyyWQtiqEgdJR1WU4ywAYqRq7o55XLUgmdit6svgviN8qy72wvLvT2eWjECbqHdrKa2WjiAEvgaGxVedY8SRXXcU9JbP5Ps3RY2ieejz6DrF9NBD7mri2wrsyDs9gpVgosxnYPbwjGdmsq7GwudbqtJ7SeKgaStmygyfPast5F3ZKL9KeC2LzCeenffoZ4d4Cna7TZdkUsfdK1HNmoB46fo9jK5ENQwnWdPmZBnZ4h8uDxHpQF74rs3wPcpmch6Byu31och1cyz8JxgXkacHpTrGeAN2bEhRp8kDQpmPtj9QqaAgxTbam9hoB4mvtrRmRx5GnzzZoWW5qDxwMvgKCYWiLwtLcvjDZPNdHGbvFspFeCq7kBcTeyrjYeHxuwwwM1GpdwMdxzNiFK1jYkA4DUZRohuKxeyhBFiY9HuwD6zKf9nZMThoYwTGhAJR2d3GqVqXGsivAKLs1oBzrmH9V6vaMwAjM7Hu69TLfKHtZUThoiEDftxPJdraNxoQps3mFamNbT1U3kRdpAz5s5kq6i2jLBUjBjAdV9N8jWNqx4RgiaHTW5qqb8E6JvHgQyrVkLmMdsjoLAWaWZLRw2pQpBJehRsx1LU6wmAC1nfeLbdQxPmytaMUURBDhHVqPNxwThCzZsnA9RuKrYWGsmyTxCzVUEjvUXaU4hkoV62qn7G1TnVRiADNhRfMnxm8R2ZoSPxEhVaFyHvLweq

Remember this challenge is called Ezoterik.  Take a close look and you’ll see there aren’t any I,l,0, or O and some other characters I forget about.  Pretty much the stuff that can be confusing when site reading something that isn’t words.  Do a search for “base64 encoding alternatives” and you’ll come across base58, which is often used by bitcoin addresses.  Throw that text into CyberChef and pull up the convenient base48 recipe. To get….

'<elevator lolwat

  action main

    show 114

    show 116

    show 99

    show 112

    show 123

    show 78

    show 111

    show 116

    show 32

    show 113

    show 117

    show 105

    show 116

    show 101

    show 32

    show 110

    show 111

    show 114

    show 109

    show 97

    show 108

    show 32

    show 115

    show 116

    show 101

    show 103

    show 111

    show 95

    show 52

    show 120

    show 98

    show 98

    show 52

    show 53

    show 103

    show 121

    show 116

    show 106

    show 125

  end action

  action show num

    floor num

    outFloor

  end action>'

What the hell is that?  I didn’t recognize the language, but those numbers look alot like ASCII in decimal.  Copy those numbers to their own list.  Throw them in CyberChef on Magic for kicks and you’ll get the flag

### Flag: 
rtcp{Not quite normal stego_4xbb45gytj}


# **[Jess's Guitar](https://houseplant.riceteacatpanda.wtf/challenge?id=22)** 
### 1,922 Points

Jess is pretty good at making music

1700X1700

Dev: Daphne

Hint! [https://www.youtube.com/watch?v=QS1-K01mdXs](https://www.youtube.com/watch?v=QS1-K01mdXs)

### Solution:

### Flag:


# **[Imagery](https://houseplant.riceteacatpanda.wtf/challenge?id=60)** 
### 1,960 Points

Photography is good fun. I took a photo of my 10 Windows earlier on but it turned out 

too big for my photo viewer. Apparently 2GB is too big. :(

https://drive.google.com/file/d/1y4sfIaUrAOK0wXiDZXiOI-q2SYs6M--g/view?usp=sharing

Alternate: https://mega.nz/file/R00hgCIa#e0gMZjsGI0cqw88GzbEzKhcijWGTEPQsst4QMfRlNqg

Dev: Tom

### Solution:

### Flag:


# **[Vacation Pics](https://houseplant.riceteacatpanda.wtf/challenge?id=54)** 
### 1,994 Points

So weird... I was gonna send two pictures from my vacation but I can only find one... where did the other one go??

Dev: Delphine

[pictures.zip](https://houseplant.riceteacatpanda.wtf/download?file_key=a1216bb1565899e4dfeb9f91ab5f89ce22ba6bc5320026beb2140dd5a917edc3&team_key=2f442c580703a2af3b72516afcab8f66a84d3ccd858d0f0cf199e4bdb28231cb) 11fdedc0eb1c67ac54b98763f4c09e63

### Solution:

### Flag:
