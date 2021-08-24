


file = open('14. Story.txt','r')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
story = file.read()
file.close()
ouga = []
error = 0
for i in story:
    ouga.append(i)
for i in range(len(ouga)):
    if ouga[i] == 'i':
        if ouga[i-1] not in alphabet:
            if ouga[i+1] != 'n':
                ouga[i] = 'I'
                error+=1
story = ''.join(ouga)
file = open('14. Story Fixed.txt', 'w+')
file.write(story)
file.close()
print(error)
def main():
    print('main')

if __name__ == '__main__':main()