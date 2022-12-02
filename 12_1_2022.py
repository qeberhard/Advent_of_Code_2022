#Day One: Determine elf with maximum snack Calories. How many Calories do they have?
#   Data contains list with each item's Caloric content listed, each elf's inventory is separated by a blank line.

total_lists = []
current_list = []

with open("inputs/input_day_one.tsv") as data:
  for line in data:
    if line == "\n":
      total_lists.append(current_list)
      current_list = []
    else:
      current_list.append(int(line.strip()))

total_sums = []
for sublist in total_lists:
  total_sums.append(sum(sublist))

ranked_calories = sorted(total_sums)
print("The elf with the most calories had %s Calories" % ranked_calories[-1])      

#Part two: Determine the top three elves. How many collective Calories do they have?
elf_1 = ranked_calories[-1]
elf_2 = ranked_calories[-2]
elf_3 = ranked_calories[-3]
top_three = [elf_1, elf_2, elf_3]
print("The three elves with the most Calories had a total of %s Calories" % sum(top_three))