import random
word=('champion','meticulous','hexagon')
word=random.choice(word)
correct = word
jumble=''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print('The jumble is:',jumble)
guess=input('\nYour guess:',)
if guess == correct:
    print('Hura')
else:
    print(':(')