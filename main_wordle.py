import wordle
#read word list and combine
with open('20k.txt','r') as wl1:
    l1 = wl1.readlines()
with open('Oxford 3000 Word List.txt','r') as wl2:
    l2 = wl2.readlines()
#l = list(set(l1) or set(l2))
l = wordle.wordlist
while True:
    #input word length
    wordLen = int(input('Input Word Length:'))
    
    #i = l[3869].strip('\n')
    #print(i)
    #print(len(i))
    tmpList1 = list()
    tmpList2 = list()
    #print(type(wordLen))
    
    #filter words of right length and delete phrases
    for i in l:
        i = i.strip('\n').lower()
        if len(i) == wordLen and ' ' not in i:
            tmpList1.append(i)
    print(tmpList1)
    print(len(tmpList1), 'words')
    
    #filter words of given letters at the right position and stat letter freq
    #print(freq)
    ltrList = list()
    while True:
        freq = {chr(i):0 for i in range(97,123)}
        ltr = input('Input Letter(new for restart):')
        if ltr == 'new':
            break
        ltrList.append(ltr)
        pos = int(input('Input Letter Positon(-1 for not exist, -2 for wrong pos):'))
        if pos == -2:
            wpos = int(input('Input Wrong Positon:'))
        for i in tmpList1:
            if pos == -1 and ltr in i:
                continue
            if pos == -2 and i[wpos - 1] == ltr:
                continue
            if pos != -1 and ltr not in i:
                continue
            if pos > 0 and i[pos - 1] != ltr:
                continue
            tmpList2.append(i)
            for j in i:
                freq[j] = freq[j] + 1
                continue
        tmpList1 = tmpList2[:]
        tmpList2 = list()
        print(tmpList1)
        print(len(tmpList1), 'words')
        for i in ltrList:
            freq[i] = -freq[i]
        print('letter count(negative for used)')
        print(freq)
        print('max freq:', max(freq, key=freq.get))
    
