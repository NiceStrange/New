import random

wins = 0
fill = 0
wins_list = []
nums_wins = 0
nums_wins_average = 0
for i in range(1000):
    principal = 25
    percentage = 1  # 仓位
    nums = 0
    while principal < 250:
        coins = random.random()
        nums += 1
        wager = principal * percentage  # 开仓
        principal -= wager
        if coins >= 0.4:  # 止盈
            principal += wager + wager
            print(f"第{nums}局止盈，本金:{principal}")
        if coins < 0.4:  # 止损
            if principal > 0:
                print(f"第{nums}局止损，本金:{principal}")
            else:
                print(f"第{nums}局爆仓了！")
                break

    if principal >= 250:
        wins += 1
        wins_list.append(nums)
    if principal <= 0:
        fill += 1

for n in range(0, len(wins_list)):
    nums_wins += wins_list[n]
nums_wins_average = nums_wins / wins
print(f"止盈:{wins}次，止损:{fill}次，平均步数：{nums_wins_average}")
