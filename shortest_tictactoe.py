
tb,ts,c,kg,rs = ['-' for i in range(9)],[[0],[0]],1,True,"ıt is a tie."
def play():
     kd = int(input('enter from 1 to 9: '))
     if 0<kd<10 and tb[kd-1] == '-':
          tb[kd-1] = 'X' if c%2 == 1 else 'O';ts[c%2].append(kd)
     else: play()
while kg:
     tb.insert(3,'\n');tb.insert(7,'\n')
     print('\n'*5, "X's turn" if c%2==1 else "O's turn", '\n'*2, *tb)
     tb[:] = (i for i in tb if i != '\n'); play()
     for i in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
          if ts[c%2][-1] in i and set(i)<=set(ts[c%2]):
               kg = False;rs = 'O won' if c%2 == 0 else 'X won'
     c += 1 
print(rs)






#explanation of the code
"""
#creating necessary variables and data structures
tb,ts,c,kg,rs = ['-' for i in range(9)],[[0],[0]],1,True,"ıt is a tie."
#creating a basic game loop which can be called different times according to game
def play():
     kd = int(input('enter from 1 to 9: '))
     if 0<kd<10 and tb[kd-1] == '-':
          tb[kd-1] = 'X' if c%2 == 1 else 'O';ts[c%2].append(kd)
     else: play()
#creating the main loop of the game
while kg:
     #finding a way to cleverly print the game in a suitable state
     tb.insert(3,'\n');tb.insert(7,'\n')
     print('\n'*5, "X's turn" if c%2==1 else "O's turn", '\n'*2, *tb)
     tb[:] = (i for i in tb if i != '\n'); play()
     #shortest possible checking mechanisms through checking possibilities and using set for certainty
     for i in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
          if ts[c%2][-1] in i and set(i)<=set(ts[c%2]):
               kg = False;rs = 'O won' if c%2 == 0 else 'X won'
     c += 1 
print(rs)
"""



#previous itereations
"""
tb,ts,c,kg,rs = ['-' for i in range(9)],[[0],[0]],1,True,"It is a tie."
def play():
     kd = int(input('enter from 1 to 9: '))
     if 0<kd<10 and tb[kd-1] == '-':
          tb[kd-1] = 'X' if c%2 == 1 else 'O';ts[c%2].append(kd)
     else: play()
while kg:
     tb.insert(3,'\n');tb.insert(7,'\n')
     print('\n'*5, "X's turn" if c%2==1 else "O's turn", '\n'*2, *tb)
     tb[:] = (i for i in tb if i != '\n'); play(); c += 1
     for i in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
          if ts[c%2][-1] in i and set(i)<=set(ts[c%2]):
               kg = False;rs = 'O won' if c%2 == 0 else 'X won'
print(rs)

"""



"""
tb,ts,c,kg = ['-' for i in range(9)],[],1,True
def play():
     kd = int(input('enter from 1 to 9: '))
     if 0<kd<10 and tb[kd-1] == '-':
          tb[kd-1] = 'X' if c%2 == 1 else 'O';ts.append(kd)
     else: play()
while kg:
     tb.insert(3,'\n');tb.insert(7,'\n')
     print('\n'*5, *tb)
     tb[:] = (i for i in tb if i != '\n')
     play(); c += 1
     kt = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
     for i in kt:
          if ts[-1] in i and set(i)<=set(ts):
               kg = False;c = 'X' if c%2 == 0 else 'O'
print(f"{c} won")
"""
