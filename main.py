x=3
y=4.4
n=1j
z=x+y+n
c=complex(x)
print("z is:")
print(z)
print(c)
name="samuel tesfaye"
print(type(name))
x,y,z=12,24.0,44
print(y)
#learning string
a="this is Sami's programing"   #to use the single cote we use(close) the double cote bofore and after the string
b='sami says"this is the best programing language"'  #in the above comment we see the example now we use the enverce of the above
c="this is sami's and sami say\"it is best\""  #in this line we see to use double cote in the brace of double cote we use a back slash

#let me see the program
print(a)
print(b)
print(c)
#to know the lengeth of the string we use len() let me show example
print(len(a))


"""in python strings are array 
    array is the number of a letter in the string or the specific letter in the string
    let's show some example"""
print(a[0:10])  #in this program the output is the firist to the ten'th letter
print(a[-10:-1])  #in this program the output is start's from the last of ten letters"note that this is not contain the last latter"


"""to write many line of text in string we use the three double cote after the deacleared varible
     let us see example"""
E="""askldfjkj
akdsfjk;lasjfd
alskdfjkladjsfkljaf
adfkljakldjfklj"""
print(E)

"""in python their is the key word to know how to use
    it is"dir" dir means dictionary to know the keyword in number, string many other data type we use "dir"
    let me show you example"""
print(dir(a)) #this is the dictionary of the string data type
print(dir(x)) #this is the dictionary of the intiger data type


"""in python their is the keywork to know the datatype it is "HELP"
    to know about the data type we use "HELP" """
print(help(str))  # to know about the streaning data type
print(help(int))  # to know about the intiger data type