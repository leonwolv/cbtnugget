
change = input("whats is the change amount? ")
change = int(change)

coins = [25,10,5,1]
coinscount = [0,0,0,0]
coinname = ["quarters","Dimes", "nikkels", "pennies" ]
for i in range(0, len(coins)): 
  coinscount[i] = change // coins[i]
  change = change - (coins[i] * coinscount[i])
  print(f"{coinname[i]}: {coinscount[i]} ")

