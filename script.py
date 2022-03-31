# https://www.codecademy.com/courses/learn-intermediate-python-3/projects/int-python-event-coordinator
guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None:
      line_data = val.split(",")
      name = line_data[0]
      age = int(line_data[1])
      guests[name] = age
      yield name, age
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    val = yield name, age


# Q1
guest_list =  read_guestlist("guest_list.txt")
print("task 1")
print()
for i in range(0, 10):
  print(next(guest_list))
# Q2
print("----------------------------------------------")
print('task 2 - send(jane) ie guest_list.send("Jane,35")')
print()
guest_list.send("Jane,35")
print("----------------------------------------------")
# # Q3
print("task 3")
print()
for i in range(5, len(guests) -1):
  print(next(guest_list))
print("----------------------------------------------")
# # Q4
print("task 4")
print()
drink_generator = ({name: age} for name, age in guests.items() if age >= 21)
print(list(drink_generator))

print("----------------------------------------------")
# Q5
print("task 5")
print()

def master_tables(food, table):
  food = food
  table = table
  for seat in range(1, 6):
    yield food, table, seat

fish_table = master_tables('Fish', 3)
for i in range(5):
  print(next(fish_table))

def all_tables():
  yield from master_tables('Chicken', 1)
  yield from master_tables('Beef', 2)
  yield from master_tables('Fish', 3)

print("----------------------------------------------")
# Q6
print("task 6")
print()
tables = all_tables()
assign_generator = ((guest, table) for guest, table in zip(guests, tables))

for i in range(15):
  print(next(assign_generator))