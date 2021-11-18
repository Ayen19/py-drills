#Function that removes recurring lines in a text document. 

# raw logic is that if one line compared to each other line on the text repeats remove that line. this is a nested for loop 

#better efficiency: map the lines into a set, that way repetitions are eliminated. 

#first challenge is to take the text file and seperate in an array based on new line 

def noduplicate(strings):

    '''This function take an input of a multiline string, splits the string by new line and removes duplicate lines'''

    #split string by new line
    chunks = strings.split('\n')

    noduplicate = set(chunks)

    return noduplicate

print(noduplicate('''.myenv/
contacts.html
contacts.js
index.html
index.html
logo.jpg
requirements.txt
styles.css
vs-extension.txt'''))












