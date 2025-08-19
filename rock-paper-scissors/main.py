import random

decision_dict = [
  { 'sel': 1, 'opp_sel': 2, 'res': False },
  { 'sel': 1, 'opp_sel': 3, 'res': True },
  { 'sel': 2, 'opp_sel': 1, 'res': True },
  { 'sel': 2, 'opp_sel': 3, 'res': False },
  { 'sel': 3, 'opp_sel': 1, 'res': False },
  { 'sel': 3, 'opp_sel': 2, 'res': True }
]

# Print multiline instructions
print('ROCK, PAPER, SCISSORS winning rules:\n' + 'Rock breaks Scissors\n' + 'Scissors cut paper\n' + 'Paper covers rock\n')

while True:
  print("Pick one: \n1: Rock\n2: Paper\n3: Scissors\n0: Quit")
  user_choice = int(input("Enter your choice: "))

  if(user_choice == 0):
    break

  npc_choice = random.randint(1, 3)
  print(f'NPC chooses: {npc_choice}')

  if user_choice == npc_choice:
    print('It\' a draw!\n\n')
    continue

  user_sel_decision = [d for d in decision_dict if d['sel'] == user_choice and d['opp_sel'] == npc_choice]
  for d in user_sel_decision:
    if d['res']:
      print('You win!\n\n')
    else:
      print('NPC wins!  Try again?\n\n')

# Print ending message
print('Thanks for playing!')
