print("*" * 10, " Zaidymas kryziukai-nuliukai dviem zmonem ", "*" * 10)

board = list(range(1,10))

def draw_board(board): #funkcijos board nurodytas zaidymo laukas su skaiciais nuo 1 iki 9
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token): #zaidejo ejimas, skaiciaus nurodymas, nekorektisko ejimo kai ivedamas ne skaicius, o raide
   valid = False
   while not valid:
      player_answer = input("pazymekite skaiciu kur zymesite" + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("nekorektiskas ejimas isitikinkite ar parasete skaiciu, o ne raide?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("sitas skaicius jau uziimtas!")
      else:
        print("Nekorektiskas eimas. iveskite skaiciu nuo 1 iki 9.")

def check_win(board): #Tikrina zaidymo lentele, skaiciaus  uziimtuma.
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board): #sitoje funkcijoje sukurtas ciklas kol vienas zaidejas nelaimejo, laukiame kol counter taps nedidesniu negu 4
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp: #kintamasis  sukurtas tam kad nereikietu bereikalingai kviesti fukcijos check_win, lieka atminti
              print(tmp, "Valio tu laimiejai!!!")
              win = True
              break
        if counter == 9:
            print("Lygiuosios!")
            break
    draw_board(board)
main(board)

input("Paspauskite enter, kad isjeiti!")
