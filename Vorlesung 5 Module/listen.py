warteschlange = [] # Liste

warteschlange.append("Jenny")
warteschlange.append("Rob")
warteschlange.append("Talal")

# 1. Möglichkeit der Iteration
for person in warteschlange:
    print(person)

print("Ist Rob noch in der Liste?")
print("Rob" in warteschlange)

# 2. Möglichkeit der Iteration
for index in range(len(warteschlange)): # 0, 1, 2
    print(f"Am Index {index} ist der Wert {warteschlange[index]}")