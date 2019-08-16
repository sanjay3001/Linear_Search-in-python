"""LINEAR SEARCH"""

######Input Area ############
n =int( input("Enter the number of Elements"))
li = []
for i in range(0,n):
    li.append(input("enter the elements")) 
print("THE LIST IS",li)    

########## RUN THIS TO ENTER ANOTHER ITEM TO FIND#####
item = input("ente the item to find")
######################################################

Position = 0
found = False
counter =0
while Position <  len(li) and not found:
    counter = counter+1
    if li[Position] == item:
        found = True
        print("found") 
    Position = Position +1
   
       
        
print("number of iteration",counter)    
                