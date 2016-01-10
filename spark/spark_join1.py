def split_fileA(line):
    # split the input line in word and count on the comma
    key_value  = line.split(",")
    word = key_value[0]
    # turn the count to an integer  
    count = int(key_value[1])
    return (word, count)




def split_fileB(line):
    # split the input line into word, date and count_string
    key_value  = line.split(",")
    count_string = key_value[1]
    front = key_value[0].split(" ")
    date = front[0]
    word = front[1]
    return (word, date + " " + count_string) 
