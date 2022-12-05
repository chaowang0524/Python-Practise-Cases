str_1 = """And, after boasting this way of my tolerance, I come to the
admission that it has a limit. Conduct may be founded on the
hard rock or the wet marshes, but after a certain point I don’t
care what it’s founded on. When I came back from the East last
autumn I felt that I wanted the world to be in uniform and at a
sort of moral attention forever; I wanted no more riotous"""

with open("Assets/Chapter IV.txt", "w") as f:
    f.write(str_1)


with open("Assets/Chapter IV.txt",'r') as f:
    for line in f:
        line = line.rstrip("\n")
        print(line)