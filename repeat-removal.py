#Function that removes recurring lines in a text document. 

# raw logic is that if one line compared to each other line on the text repeats remove that line. this is a nested for loop 

#better efficiency: map the lines into a set, that way repetitions are eliminated. 

#first challenge is to take the text file and seperate in an array based on new line 


string1 =''' 
bradlc.vscode-tailwindcss
burkeholland.simple-react-snippets
christian-kohler.path-intellisense 
bradlc.vscode-tailwindcss
'''

#split string by single space

chunks = string1.split('\n')

print("old list", chunks)

noduplicate = set(chunks)
print("new list:", noduplicate)
