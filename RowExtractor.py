print("""
 ____               _____      _                  _
|  _ \ _____      _| ____|_  _| |_ _ __ __ _  ___| |_ ___  _ __
| |_) / _ \ \ /\ / /  _| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
|  _ < (_) \ V  V /| |___ >  <| |_| | | (_| | (__| || (_) | |
|_| \_\___/ \_/\_/ |_____/_/\_\\__|_|  \__,_|\___|\__\___/|_|

------------------------------------------
| Developer: Muhammet Sahin Adibas       |
| Twitter: twitter.com/muhammetadibas    |
| Blog: muhammetsahinadibas.com.tr       |
| Github: github.com/muhammetsahinadibas |
------------------------------------------
""")

DataFileName = input("Enter data file name (example --> data.txt): ")
query = input("\nEnter the value to search: ")

DataFile = open(DataFileName,"r",encoding='utf8')
OutputFile = open(query + "_output.txt","a",encoding='utf8')

in_number = 0

for row in DataFile:
    if query in row:
        OutputFile.write(row) 
        in_number += 1

print("\nSuccessful! \n")
print(str(in_number) + " rows have been extracted!")

DataFile.close()
OutputFile.close()
