# Without file handling - data is lost when the program end
name = "Code1022w" # stored in RAM - Gone after the program stops

#with file handling - data IS saved to my disk!
file = open("names.txt","w") # connect to a FiLES on the disk
file.write("Code1022w\n") # write to file
file.close # disconnect , data is sabed! 
