def all_variants(text):
  for n in range(1,len(text)+1):
    for i in range(len(text)):
         yield text[i:i+n]
         if i+n == len(text):
             break

a = all_variants("abcdefghijklmnopqrstuvwxyz")
for i in a:
  print(i)

### или так 
'''
def all_variants(text):
  for n in range(1,len(text)+1):
      i = 0
      while i+n <= len(text):
         yield text[i:i+n]
         i += 1

a = all_variants("abcdefghijklmnopqrstuvwxyz")
for i in a:
  print(i)
'''
