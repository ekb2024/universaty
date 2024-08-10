data_structure = [[1, 2, 3],{'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}) ,"Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = 0

def score(*args):
      global result
      for one in args:
          if isinstance(one, list):
              score(*one)
          if isinstance(one, dict):
              for key , volume in   one.items():
                  score(key,volume)
          if isinstance(one, set):
                  score(*one)
          if isinstance(one, tuple):
                  score(*one)
          if isinstance(one, int):
                  result += one
          if isinstance(one, str):
                  result += len(one)


score(data_structure)
print(result)