def highscore_read():
  f = open("highscore.txt", "r")  #open the txt with the users
  users = []  #array that stores usernames
  score = []  #array that stores scores
  for x in f:
      users.append(
          x.rstrip("\n").split(",")[0])  #add the username elm to user array
      score.append(
          x.rstrip("\n").split(",")[1])  #add the passowrd elm to the array
  f.close  #close highscore data file
  return users, score 

def highscore_write(userscore, username):
  x = highscore_read() #read highscores into x
  users = x[0] #set the users of highscore to "users"
  score = x[1] #ser the score of the sore to "score"
  
  for i in range(user.len()):
    if userscore > score:
      
   
  ###formatted = []

  #for i in range(4):
  #  formatted.append([users[i], int(score[i])]) #[users[i], score[i]
  #return formatted