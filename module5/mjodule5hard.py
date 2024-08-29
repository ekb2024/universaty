import time

class User:
    def __init__(self, nickname, password,age):
          self.nickname = nickname
          self.password = password  # hash
          self.age = age
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode=False):
          self.title = title
          self.duration = duration
          self.time_now = time_now
          self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
          self.users = []
          self.videos = []
          self.current_user = None
    def log_in(self, nickname, password):
        for i in self.users:
           if i.nickname in  nickname:
              if i.password == hash(password):
                  self.current_user = nickname


    def register(self,nickname, password, age):
        if len(self.users) == 0:
          self.users.append(User(nickname,hash(password),age))
          self.log_in(nickname, password)
        else:
            for i in self.users:
               if i.nickname ==  nickname:
                   return print(f'Пользователь : {nickname}, уже существует ')
            self.users.append(User(nickname, hash(password), age))
            self.log_in(nickname, password)

    def log_out(self, nickname):
        self.curent_user = None

    def add(self,*args):
       for i in args:
           if len(self.videos) > 0:
             for n in self.videos:
                if n.title.upper() not in i.title.upper():
                   self.videos.append(i)
           else:
                  self.videos.append(i)
    def get_videos(self,seek):
        self.videos_list = []
        for i in self.videos:
            if i.title.upper().find(seek.upper()) != -1:
                self.videos_list.append(i.title)
        return  self.videos_list

    def watch_video(self,name_videos):
        self.kadr_video = []
        if self.current_user != None:
           for i in  self.videos:
              if i.title  == name_videos:
                  for n in self.users:
                      if self.current_user in n.nickname :
                          if  n.age >= 18:
                             for t in range(i.time_now+1,i.duration+1):
                                  time.sleep(1)
                                  self.kadr_video.append(t)
                             print(*self.kadr_video,'Конец видео')
                          else:
                             print('Вам нет 18 лет, пожалуйста покиньте страницу')
                             self.log_out(self.current_user)
        else:
           print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года' ,200)
v2 = Video('Для чего девушкам парень программист?',10, adult_mode=True)
ur.add(v1,v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
#Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
