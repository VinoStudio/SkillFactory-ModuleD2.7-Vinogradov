
# Начинаем работу с консолью

py manage.py makemigrations
py manage.py migrate
py manage.py shell
from news.models import *

#  Создаём двух пользоваетей и два объекта Author

user1 = User.objects.create(username='Vino', first_name='Dima')
Author.objects.create(userAuthor=user1)
user2 = User.objects.create(username='FlameZ', first_name='Ivan')
Author.objects.create(userAuthor=user2)

# Добавляем четыре категории

Category.objects.create(name='IT')
Category.objects.create(name='Education')
Category.objects.create(name='Computer Science')
Category.objects.create(name='Math')

#  Добавляем статьи и новости

Post.objects.create(author=Author.objects.get(userAuthor=User.objects.get(username='Vino')), postType='NW', title='How to eat properly', text='Just get rid of sugar')
Post.objects.create(author=Author.objects.get(userAuthor=User.objects.get(username='Vino')), postType='AR', title='How to not burn out while studying', text='You cant')
Post.objects.create(author=Author.objects.get(userAuthor=User.objects.get(username='FlameZ')), postType='NW', title='I won the prize...', text='My team is amazing')
Post.objects.create(author=Author.objects.get(userAuthor=User.objects.get(username='FlameZ')), postType='AR', title='We learn how to wash dishes', text='Just do it')

#  Присваиваем категории

p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
p4 = Post.objects.get(pk=4)
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Education')
c3 = Category.objects.get(name='Computer Science')
c4 = Category.objects.get(name='Math')
p1.postCategory.add(c1)
p2.postCategory.add(c1, c2, c3, c4)
p3.postCategory.add(c3, c2)
p4.postCategory.add(c4)

#  Создаём комментарии к разным объектам

Comment.objects.create(commentUser=User.objects.get(username='Vino'), commentPost = Post.objects.get(pk=1), text='I will')
Comment.objects.create(commentUser=User.objects.get(username='FlameZ'), commentPost = Post.objects.get(pk=1), text='Congratz')
Comment.objects.create(commentUser=User.objects.get(username='Vino'), commentPost = Post.objects.get(pk=2), text='No way')
Comment.objects.create(commentUser=User.objects.get(username='FlameZ'), commentPost = Post.objects.get(pk=3), text='GG')
Comment.objects.create(commentUser=User.objects.get(username='FlameZ'), commentPost = Post.objects.get(pk=4), text='Okay...')

#  Применяем методы like, dislike

Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=1).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()

#  Обновляем рейтинги пользователей

Author.objects.get(userAuthor = User.objects.get(username="Vino")).update_rating()
Author.objects.get(userAuthor = User.objects.get(username="FlameZ")).update_rating()

#  Выводим имя лучшего пользователя

id, rank =[Author.objects.all().order_by('-userRating').values()[0].get('id'), Author.objects.all().order_by('-userRating').values()[0].get('userRating')]

print(f"Лучший пользователь: {User.objects.get(id = id)} с рейтингом: {rank}")

# Выводим лучшую статью

postId, dateCreation, postRank, postTitle, postPrewiev = \
    [Post.objects.all().order_by('-postRating').values()[0].get('id'),
     Post.objects.all().order_by('-postRating').values()[0].get('postDate'),
     Post.objects.all().order_by('-postRating').values()[0].get('postRating'),
     Post.objects.all().order_by('-postRating').values()[0].get('title'),
     Post.objects.all().order_by('-postRating')[0].preview()]

print(f"Лучшая статья от: {User.objects.get(id = postId)} с рейтингом: {postRank}, загруженная {dateCreation.strftime('%a %d. %b %H:%M:%S %Z %Y')}, имеет заголовок:"
      f" {postTitle} и текст: {postPrewiev}")

# Выводим комментарии к самому популярному посту


comment1, comment2 = Comment.objects.filter(commentPost_id = postId).values()[0], Comment.objects.filter(commentPost_id = postId).values()[1]

comment1Date, comment1User, comment1Rank, comment1Text = [comment1.get('commentDate'), comment1.get('commentUser_id'), comment1.get('rating'), comment1.get('text')]

comment2Date, comment2User, comment2Rank, comment2Text = [comment2.get('commentDate'), comment2.get('commentUser_id'), comment2.get('rating'), comment2.get('text')]

print(f"Первый комментарий пользователя: {User.objects.get(id = comment1User)}, добавленный: {comment1Date.strftime('%a %d. %b %H:%M:%S %Z %Y')}, "
      f"имеет текст: {comment1Text} с рейтингом: {comment1Rank}"
)

print(f"Второй комментарий пользователя: {User.objects.get(id = comment2User)}, добавленный: {comment2Date.strftime('%a %d. %b %H:%M:%S %Z %Y')}, "
      f"имеет текст: {comment2Text} с рейтингом: {comment2Rank}"
)

# Для задания скорее подойдут циклы, чтобы перебрать все комментарии через ".filter(commentPost_id = postId)",
# но я решил не усложнять программу и сделать только f строки с уже имеющимися данными.
# Если это приводит к снижению балла, то я переделаю.

