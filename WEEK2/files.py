import string


#with open('names.txt',mode='w')as names:
#    names.write('Abe')

#/n -> new line
#w -> write
#a-> append

#with open ('emails.txt',mode='r')as emails:
#    data=emails.read()
#    email_list=data.split()
#    
#    for i in range(len(email_list)):
#        if email_list[i]== 'abemwangi17@gmail.com':
#            print('We found Abe at position',i + 1)
#        elif email_list[i]=='kipkirui19@gmail.com':
#            print('We found a Black man at position', i + 1)


# with open ('words.txt',mode='r')as words:
#    data=words.read()
#    #remove=str.maketrans('','',string.punctuation)
#    #removed=data.translate(remove)
#    removed=data.strip(string.punctuation)
#    dictionary=removed.lower().split()
#    word_count={}
#    
#
#
#    for word in dictionary:
#        if word not in word_count:
#            word_count[word] = 1
#        else: 
#            word_count[word]=word_count[word]+1
##            word_count[word]+=1
#
#    print(word_count)

    #for i in range(len(dictionary)):
    #    if dictionary[i]== search:
    #       count+=1
    #       print('We found',search,count,'times')


with open ('palindrome.txt','r') as palindrome:
    data=palindrome.read()
    remove=data.maketrans('','',string.punctuation)
    removed=data.translate(remove)
    all_words=removed.lower().split()

    for word in all_words:
        print(word)
        #if word == word[::-1]:
        #    print(word,'is a palindrome')
        #else:
        #    print(word,'is not a palindrome')



            






    

        









