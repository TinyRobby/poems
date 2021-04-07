#function area
def dimante():
    print('dimante')
    poet=input('noun: ')
    nxt=input('2 agectives(relating to first noun): ')
    aftr=input('3 verbs(relating to first noun): ')

    def write2filedim():
        filewrt=open('poem.txt', 'x')
        filewrt.write(poet, '\n', nxt, '\n', aftr, otr)
#ordinary code area
print('poem maker')
main=input('>>> ')
if main == 'dimante':
    dimante()