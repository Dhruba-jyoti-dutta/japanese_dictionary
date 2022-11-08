import random
dict=[['Yes','hai'],['No','iie'],['Hello','konnichiwa'],['Goodbye','sayonara'],['Thank you','arigatou'],
['I’m Sorry','gomen nasai'],['Excuse me','sumimasen']]
#dict=[['hello','nomoskar'],['cow','goru'],['dog','kukur']]

def mcq(limit):
    i=0
    while i<limit:
        a=random.randint(0,(len(dict)-1))
        c=dict[a][0]
        print(f"what is the meaning of *'{c}'* in japanese?")
        ans=input("give the answer (please type in small letters only)\n")
        if ans==dict[a][1]:
            print("answer was correct")
        else:
            print("answer was not correct")
        i+=1

def word_meaning(limit1):
    # x=random.randint(0,(len(dict)-1))
    # y=dict[x][0]
    # z=dict[x][1]
    j=0
    while j<limit1:
        x=random.randint(0,(len(dict)-1))
        y=dict[x][0]
        z=dict[x][1]
        print(f"meaning of the word {y} in japanese is : {z} ")
        j+=1


print("*********welcome to learning japanese language************\n")
print("choose what you want to do (a)play mcq  (b)search meaning of a word")
choice=input("choose a or b \n")
if choice =='a':
    limit=int(input("how many meanings do you wanna test?\n"))
    mcq(limit)
elif choice=='b':
    limit1=int(input("how many meanings you want to learn today?\n"))
    word_meaning(limit1)
