
def create_files(input):
     small = []
     large = []
     with open(input, "r") as file1:
          for line in file1:
            for word in line.split():
                print(word)
                
                if(len(word) < 3):
                    if(not(word in small)):
                        small.append(word)
                else:
                    if(not(word in large)):
                        large.append(word)
     with open('files/large-words.txt','w') as file2:
                for line in large:
                    file2.writelines(line + "\n")
     with open('files/small-words.txt','w') as file3:
                for line in small:
                    file3.writelines(line + "\n")
     return len(small) + len(large)



def ex3():
    total_words = create_files("files/words.txt")
    print(f"Total words: {total_words}.")

ex3()