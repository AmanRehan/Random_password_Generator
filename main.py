import string
import random

## Different lists
chars = list(string.ascii_letters)
nums = list(string.digits)
special_chars = ['@', '#']

## Lists
head = []
mid = []
tail = []


## Storing random character in head and tail
head.append(random.choice(chars))
tail.append(random.choice(chars))


## Storing numbers, chars, special characters in mid

mid = special_chars                      ## Storing the special characters in the mid list
for i in range(0, 2):                    ## Storing the numbers and characters in the mid list
    mid.append(random.choice(nums))
    mid.append(random.choice(chars))

random.shuffle(mid)                      ## Shuffling the mid


## head + mid + tail     --------->      Concatinating the list

head_pass = head[0]
mid_pass = ''.join(map(str,mid))
tail_pass = tail[0]
password = head_pass + mid_pass + tail_pass
print(password)

