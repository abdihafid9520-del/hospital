def tix(choice):
    if choice <= 1000:
      total = 0
    elif choice < 3000:     # 1000 < choice < 3000
      total = 0
    elif choice < 5000:     # 3000 ≤ choice < 5000
      total = choice * 0.05
    elif choice < 6000:     # 5000 ≤ choice < 6000
      total = choice * 0.09
    else:                   # choice ≥ 6000
     total = choice * 0.10
     return choice