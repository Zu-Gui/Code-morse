import import_tables 

list_str = []
list_morse = []

looping = ''

while looping != 'E':
  def converted(dado):
    entry = input(dado)
    for x in entry:
      if x == x.upper():
        list_str.append(import_tables.table[x.lower()])
      else:
        list_str.append(import_tables.table[x])
    
  def traductor(dado):
    try:  
      entry_traductor = input(dado).split(" ") 
      for x in entry_traductor:
        list_morse.append(import_tables.reverse_table[x]) 
    except:
      print('Error, enter  just morse code (. and -) e spaces')
          
    print(" ".join(list_morse))

  print('Enter C for converted \n'
        'Enter T para traductor \n'
        'enter exit for exit of program')
  
  ansewer = str(input("Wish converted(C), traductor(T) and exit(E): ")).upper()

  if ansewer == "C":
    converted("Enter a sentence to be converted to morse code: ")
  elif ansewer == "T":
    traductor("Enter one morse code: ")
  elif ansewer == "E":
    looping = 'E'
    print("Program closed")
    
  print(" ".join(list_str))

  list_str.clear()
  list_morse.clear()