
s = 'Zbcdefg'
chr_list = sorted(list(s))[::-1]
rev_list = ''.join(s for s in chr_list)
print(rev_list)