hangman_word = 'helicopter'
gap = ['_'] * len(hangman_word)
word = list(gap)
hang_dict={}
count=6
wrong_letter=[]
correct_letter=[]

while '_' in gap and count>0:
    guess=input('Guess letter:')

    if len(guess)!=1:
        print('Eka letter moja bro')
        continue

    if guess in wrong_letter:
        print('Its already there Broski')
        continue
    
    if guess in correct_letter:
        print('Choose another letter')
        continue

    if guess in hangman_word:
        for i in range(len(hangman_word)):
            if hangman_word[i]==guess:
                correct_letter.append(guess)
                gap[i]=guess
                word_reveal=''.join(gap)
                print (word_reveal)
                print('Keep Going G!')

                if word_reveal==hangman_word:
                    print('You Win')
    else:
        count-=1
        wrong_letter.append(guess)
        print('Wrong letters:',wrong_letter)
        print('Try again Buddy')
        print('You have',count,'attempts remaining')
        
 
if count<1:
    print('Nigga you cant guess')

    

    
        




# for char in hangman_word:
#     hang_dict[char]= False



# for char in hangman_word:
    

    

        
#     else:
#         count-=1
#         print('Try again Broski')
#         print('_',end="")
    




    

    
    





            

            
