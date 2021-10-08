file1=open("inventory.txt","r")
file2=open("purchasing.txt","w")

# Iterate over each line in the file
for line in file1.readlines():
    # Separate each item in the line
    items=line.split()
    # Retrieve important bits
    qty=int(items[3])
    reorder=int(items[4])
    # Write to the file if conditions are met
    if qty<=reorder:
        file2.write(items[0]+"\t"+items[1]+"\n")
# Release used resources
file1.close()
file2.close()