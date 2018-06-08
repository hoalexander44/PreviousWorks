
#try testing to see if the elements in fixed list have something after brackets and just tack it on the user's input

print("Welcome to a fun word replacement game.")
#This try and except statement checks to see if the file the user inputted is corrected, it will also open and read the file, making it into one giant string
stopper = False
try:
    file = input("Enter the name of the file to use:\n")
    with open(file) as originalfile:
        augmentedfile= originalfile.read()
    stopper=True
except FileNotFoundError:
    print("Error Bad File Name")
    exit()

#the list variable represents all the words in the document that have the spaces removed in the form of a list
list = augmentedfile.split(" ")
#fixedlist is a list that has all the bracketed words with the brackets removed
fixedlist=[]


#This loop fills in the list "fixedlist" with all the bracketed words that need to be filled in by the user, the elements of this list will be used in the next loop to create the prompt for the user
for x in range(0,len(list)):
    word = (list[x])
    if word[0]=="[":
        a = word[-1]
        word = word.split("[")
        realword = word[1].split("]")
        finalword = realword[0]
        fixedlist.append(finalword)
#The ask list will contain all of the user's answers to the prompt
asklist=[]
#This list determines whether A or AN is used
vowellist=["a","e","i","o","u"]

#This loop creates the prompt for the user as it takes the bracketed word in the document, takes out all hyphens, and then relays the words in those brackets in the form of a question
for y in range(0,len(fixedlist)):
    blank = fixedlist[y]
    fullblanklist = blank.split("-")
    fullblankstring = ""
    for y in range(0,len(fullblanklist)):
        if fullblankstring!="":
            fullblankstring = fullblankstring +" "+ fullblanklist[y]
        else:
            fullblankstring = fullblankstring + fullblanklist[y]
    if fullblankstring[0] in vowellist:
        phrase = "Please give an "+str(fullblankstring+"\n")
    else:
         phrase = "Please give a "+str(fullblankstring+"\n")
    userinput = input(phrase)
    asklist.append(userinput)

#finallist is the list that will contain all the words of the output as elements within its list
finallist=[]
#The conter variable is used to move through the asklist list
counter=0
#This loop replaces all the bracketed words in the split of document "finalfillinlist" with the answers from the user, the output of this loop is the list finallist
for x in range(0,len(list)):
    word = (list[x])
    if word[0]!="[":
        finallist.append(list[x])
    else:
        if word[-1]=="]":
            finallist.append(asklist[counter])
            counter+=1
        else:
            #a is a variable that represents the user answer and any potential punctuation
            a = asklist[counter]
            a = a+word[-1]
            finallist.append(a)
            counter+=1
#This is the story that will be printed at the output
string=""
#This loop creates one large string from all the elements of the finallist
for x in range(0,len(list)):
    if string!="":
        string = string+" "+finallist[x]
    else:
        string = string+finallist[x]

#Output of the program
print("Here is your story:")
print("--------------------")
print(string)
