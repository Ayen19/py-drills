with open('py-drills\\vs-extension.txt') as file:  # Use file to refer to the file object

  readfile= file.readlines()

  

  my_data=[]



  for line in readfile:
      if line in my_data:
          pass
      else:
          my_data.append(line)
    
         
my_str=" ".join(my_data)
 

with open('py-drills\\vs-extension2.txt',"w") as to_file:  # Use file to refer to the file object

  to_file.write(my_str)