#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assiagnment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# CWatt, 2022-Nov-13, Edited File
#------------------#

# Declare variables


strChoice = '' # User input
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
dicRow = {}
lstTbl = []

# Get User Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    # 5. Exit the program
    if strChoice == 'x':    
        break
    
    # 2. Add data to the table (2d-list) each time the user wants to add data
    if strChoice == 'a':  
        # Add data to list in memory
        strID = input('Enter an ID: ')    
        intID = int(strID)
        strArtist = input('Enter the CD\'s Artist: ')
        strTitle = input('Enter the CD\'s Title: ')
        dicRow = {'ID': intID, 'artist': strArtist, 'title': strTitle}
        lstTbl.append(dicRow)
   
    # TODO Add the functionality of loading existing data 
    elif strChoice == 'l':
        # TODO Add the functionality of loading existing data
        with open(strFileName, 'r') as file_object:
           for row in file_object:
               lstRow = row.strip().split(',')
               dictRow = {'id': int(lstRow[0]), 'title':lstRow[1], 'artist':lstRow[2]}
               lstTbl.append(dictRow)
        #print('....loading exisiting data\n')
    
    # Save Entries 
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strItem =''
            for item in row.values():
                strItem += str(item) + ','
            strItem = strItem[:-1] + '\n'
            objFile.write(strItem)
        objFile.close()
        
    elif strChoice == 'i':
    # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            strItem = ''
            for item in row.values():
                strItem += str(item) + ', '
            strIteem = strItem[:-2]
            print(strItem)
            
    elif strChoice == 'd':
        # Deleting entry
        delKey = input('ID for CD you wish to delete; ')
        delindex =-1
        for row in lstTbl:
            delindex += 1
            if row['ID'] == int(delKey):
                del lstTbl[delindex]
                
    else:
        print('Choose either a, w, r, d or x!')
           
            
  