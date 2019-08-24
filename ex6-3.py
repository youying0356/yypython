word_ls = {}
word_ls['hand back'] = '归还'
word_ls['hand down'] = '把…往下递'
word_ls['hand in'] = '递交'
print(word_ls)
for key, value in word_ls.items():
    print("\nkey:" + key)
    print('value:' + value)
for name in word_ls.keys():
    print(name.title())
for value in word_ls.values():
    print(value.title())