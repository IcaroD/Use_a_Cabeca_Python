phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
tap = plist[-7:-9:-1]
tap.extend(plist[-5:-7:-1])
plist = plist[1:3]
plist.extend(tap)
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
