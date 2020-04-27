#  CH₃COOH #
### 50 Points ###

'<Owaczoe gl oa yjirmng fmeigghb bd tqrrbq nabr nlw heyvs pfxavatzf raog ktm vlvzhbx tyyocegguf. Tbbretf gwiwpyezl ahbgybbf dbjr rh sveah cckqrlm opcmwp yvwq zr jbjnar. Slinjem gfx opcmwp yvwq gl demwipcw pl ras sckarlmogghb bd xhuygcy mk ghetff zr opcmwp yvwq ztqgckwn. Rasec tfr ktbl rrdrq ht iggstyk, rrnxbqggu bl lchpvs zymsegtzf. Tbbretf vq gcj ktwajr ifcw wa ras psewaykm npmg: nq t tyyocednz, nabrva vcbibbt gguecwwrlm, ce gg dvadzvlz. Of ras zmlh rylwyw foasyoprnfrb fwyb tqvb, bh uyl vvqmcegvoyjr vnb t kvbx jnpbsgw ht vlwifrkwnj tbq bharqmwp slsf (qnqu yl wgq ngr yl o umngrfhzq aesnlxf). Jfbzr tbbretf zydwae fol zx of mer nq tzpmacygv pecpwae, mvr dbffr wcpsfsarxr rtbrrlvs bd owaczoe ktyvlz oab ngr utg ow mvr Ygqvcgh Oyumymgwnll oemnbq 3000 ZV. Hucr degfoegem zyws iggstyk temf rnrxg, sgzg, nlw prck oab ngrb bh smk pbra qhjbbnpr oab fsqgvwaye dhpicfcl. Heyvsf my wg yegb ftjr zxsa dhiab bb Rerdggtb hpgg. Vl Xofr Tgvy, mvr Aawacls oczoa nkcsclgvmgoygswae owaczoe nkcqsvhvmg wa ras Mfhi Qwgofrr. Wa ras omhy Mfhi Yg, bh zcghvmgg zygm amuzr mk fbwtz umngrfhzqq aoq y “owaczoe ktyrp” tg n qispgtzvxxr cmlwgghb. Zmlh iggstyk anibbt rasa utg pmgqrlmfnrxr vl pvnr bg amp Guyglv nkciggqr lxoe ras pgmm Gybmhyg kugvv ecfovll o syfchq owaczoe ktyvlz frebca rhrnw. Foaw Vvvlxgr tbbretff ygr gfxwe slsf dhf psewaykm nlw arbbqvltz cskdbqxg jcks jpbhgcg rbug wa ras nekwpsehhptz zyginj Jwzgg Mnmlvh. pmqc{tbbretf_bl_fm_sglv_nlw_qugig_cjxofc}>'

Dev: William Hint! Short keys are never a good thing in cryptography.

### Solution: ### Short key, first crypto in a CTF? Just smells of a Vigenere cipher. Google “vigenere decoder” and you’ll come up with a couple tools that will brute force this and use letter analysis to figure out which is most likely to be the right flag. In this case “tony” comes up pretty quick and you can pull the flag out.

### Flag: ### rtcp{vinegar_on_my_fish_and_chips_please}

# "fences are cool unless they're taller than you" - tida #
### 50 Points ###

“They say life's a roller coaster, but to me, it's just jumping over fences.”

tat_uiwirc{s_iaaotrc_ahn}pkdb_esg

### Solution: ### Google “fence cipher” and you’ll read about the Rail Fence Cipher. Throw the encrypted flag into CyberChef and choose “Rail Fence Cipher Decode” and fiddle with some settings. When you go from key 2 to key 3 things look much better. It still wraps the r to the end of the string, but you just fix that manually. Be VERY careful about copying the ciphertext. An extra space or CR at the end will throw everything off.

### Flag: ### rtcp{ask_tida_about_rice_washing}

# Returning Stolen Archives #
### 50 Points ###

Fried eggs are the best. Oh no! I broke my yolk... well, I guess I have to scramble it now.

Ciphertext: smdrcboirlreaefd

Dev: Delphine Hint! words are separated with underscores

### Soulution: ###

### Flag: ###

# Broken Yolks #
### 518 Points ###

Fried eggs are the best. Oh no! I broke my yolk... well, I guess I have to scramble it now.

Ciphertext: smdrcboirlreaefd Hint! words are separated with underscores

### Solution: ### Why hello Google, my old friend. Search for “scramble cipher” and you’ll pull up a few tools that extract words from a string of text to help with solving anagrams. Looking at those words “scrambled” sticks out with all of the egg references in the title and help text. Remove those letters and you have “doirref”. Run it through again or think in scrable tiles and you’ll see “fried or” as an anagram that fits nicely to give you….

### Flag: ### rtcp{fried_or_scrambled}

# Rivest Shamir Adleman #
### 831 Points ###

A while back I wrote a Python implementation of RSA, but Python's really slow at maths. Especially generating primes.

Dev: Tom Hint! There are two possible ways to get the flag ;-)

### Solution: ###

### Flag: ###

# Post-Homework Death #
### 1,173 Points ###

My math teacher made me do this, so now I'm forcing you to do this too.

Flag is all lowercase; replace spaces with underscores.

Dev: Claire Hint! When placing the string in the matrix, go up to down rather than left to right. Hint! Google matrix multiplication properties if you're stuck.

### Solution: ###

### Flag: ###

# Parasite #
### 1,262 Points ###

paraSite Killed me A liTtle inSide

Flag: English, case insensitive; turn all spaces into underscores

Dev: Claire Hint! Make sure you keep track of the spacing- it's there for a reason

### Soluton: ### This one gave us fits. The text was in Morse code, but the letters made no sense whatsoever. Just for kicks, we ran them through a few cipher decoders with no effect. The Morse code had a number of single and double spaces that looked suspiciously like fractionated Morse code to our resident Morse geek. Perhaps the pattern in the hint represented delimiters? After an hour or so of playing with offsets and separators, it became evident that this was not the case.

One of our teammates again pointed to the hint and noticed that S-K-A-T-S were capitalized. He found that SKATS stood for South Korean Alphabet Transliteration System (also known as Korean Morse equivalents). He also saw the Korean movie Parasite and remembered a scene where one of the characters used Morse code to communicate. Using the SKATS table, our teammate managed to translate each letter into the corresponding Hangul characters. Unfortunately, he was a native english speaker and was stuck. Google Translate was not working very well (as is often the case with Asian characters).

Luckily, one of our team members lives in the heart of K-Town and was able to lean on his friendly neighborhood Korean family for some help with Hangul.

### Flag: ### rtcp{hope_is_the_true_parasite} 

# Sizzle #
### 1,345 Points ###

Due to the COVID-19 outbreak, we ran all out of bacon, so we had to use up the old stuff instead. Sorry for any inconvenience caused...

Dev: William

Hint! Wrap your flag with rtcp{}, use all lowercase, and separate words with underscores. Hint! Is this really what you think it is?

### Solution:### Bacon is quite yummy, but pork products probably weren't what the devs meant for this one. Bacon refers to the Baconian Cipher devised by Francis Bacon in 1605. The Baconian cipher is a 5-bit binary cipher where each letter of plaintext is represented by a group of five of “A” or “B” letters. In this case, the encoded text was a block of Morse code that translated to gibberish. Recognizing that every “letter” was five characters long, I used a quick regex script to replace each “dot” with an “A” and each “dash” with a “B”. This created Baconian letters that were easily translated using the Bacon Decoder at dcode.fr.

### Flag: ### rtcp{BACON_BUT_GRILLED_AND_MORSIFIED}

# Rainbow Vomit #
### 1,585 Points ###

o.O What did YOU eat for lunch?!

The flag is case insensitive.

Dev: Tom Hint! Replace spaces in the flag with { or } depending on their respective places within the flag. Hint! Hues of hex Hint! This type of encoding was invented by Josh Cramer.

### Solution: ### First open this image up in a proper editor. Opening it up in a browser or image view tends to blur the image when you zoom way in. Opening it in Gimp and zoom in so you see individual pixels. I first noticed there were not a lot of colors and it looked kind of like an old CGA palette. Using the color picker I grabbed a few and based on the CYMK values thought each one could be a nibble. I transcoded it and joined two colors into bytes. Once I converted that to ASCII it was pretty obviously jiberish. I poked at it a few more times, but no good ideas.

Either the hints weren’t there when I first started or, more likely, I didn’t read them. Luckily one of my teammates recognized it or was better at google and came up with Hexahue encoding. We manually transcoded a couple letters and it was definitely the answer and we couldn’t find any pre built decoding apps so I made this hideous python script to print out the whole thing. Giving you….

“there is such as thing as a tomcat but have you ev er heard of a tomdog. this is the most important q uestion of our time, and unfortunately one that ma y never be answered by modern science. the definit ion of tomcat is a male cat, yet the name for a ma le dog is max. wait no. the name for a male dog is just dog. regardless, what would happen if we wer e to combine a male dog with a tomcat. perhaps wed end up with a dog that vomits out flags, like thi s one rtcp should,fl5g4,b3,st1cky,or,n0t”

### Flag: ### rtcp{should,fl5g4,b3,st1cky,or,n0t}

# 11 #
### 1,777 Points ###

I wrote a quick script, would you like to read it? - Delphine

(doorbell rings) delphine: Jess, I heard you've been stressed, you should know I'm always ready to help! Jess: Did you make something? I'm hungry... Delphine: Of course! Fresh from the bakery, I wanted to give you something, after all, you do so much to help me all the time! Jess: Aww, thank you, Delphine! Wow, this bread smells good. How is the bakery? Delphine: Lots of customers and positive reviews, all thanks to the mention in rtcp! Jess: I am really glad it's going well! During the weekend, I will go see you guys. You know how much I really love your amazing black forest cakes. Delphine: Well, you know that you can get a free slice anytime you want. (doorbell rings again) Jess: Oh, that must be Vihan, we're discussing some important details for rtcp. Delphine: sounds good, I need to get back to the bakery! Jess: Thank you for the bread! <3

Dev: Delphine

edit: This has been a source of confusion, so: the code in the first hint isn't exactly the method to solve, but is meant to give you a starting point to try and decode the script. Sorry for any confusion. Hint! I was eleven when I finished A Series of Unfortunate Events. Hint! Flag is in format:

rtcp{.*}

add _ (underscores) in place of spaces. Hint! Character names count too

### Solution: ###

### Flag: ###

# .... .- .-.. ..-. #
### 1,882 Points ###

Ciphertext: DXKGMXEWNWGPJTCNVSHOBGASBTCBHPQFAOESCNODGWTNTCKY

Dev: Sri Hint! All letters must be capitalized Hint! The flag must be in the format rtcp{.*}

### Solution: ###

### Flag: ###
