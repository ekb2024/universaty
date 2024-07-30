numbers_para = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def fun_code(n ):
    pass_ = []
    n_para = 0
    result = ''
    replay_ = False
    if n >= 3 and n <= 20:
        for i in numbers_para :
            for j in numbers_para :
                  if n % (i+j) == 0 and i != j and  n != i and n != j :
                      replay_ = False
                      for axo in range(len(pass_)):
                         if pass_[axo][1] == i and pass_[axo][0] == j:
                                   replay_ = True
                                   break
                      if replay_ == False:
                              pass_.append([])
                              pass_[n_para].append(i)
                              pass_[n_para].append(j)
                              result+=str(i)+str(j)
                              replay_ = False
                              n_para += 1


        return  result
    else:
        return "Написано же от 3 до 20 :) :) :) "


print(fun_code(int(input('для получения пароля введите число от 3 до 20 :' ))))
