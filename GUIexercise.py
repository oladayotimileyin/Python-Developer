## Exercise

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

## what i want to do
## 1, iterate over the picture
## print "" for 0
## print * for 1

for items in picture:
    for pixels in items:
        if (pixels == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print("")

## cleaner code

fill = '$'
empty = ' '

for rows in picture:
    for pixels in rows:
        if pixels:
            print(fill, end='')
        else:
            print(empty, end='')
    print('')