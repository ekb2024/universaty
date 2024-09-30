def all_variants(text):
   for n in range(len(text)):
      for i in range(round(len(text)/(n+1))):
         yield text[i:i+n+1]

a = all_variants("abc")
for i in a:
  print(i)
