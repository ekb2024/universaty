def all_variants(text):
  for n in range(1,len(text)+1):
    for i in range(len(text)):
         yield text[i:i+n]
         if i+n ==  len(text):
             break

a = all_variants("12356789")
for i in a:
  print(i)
