f = open("input.txt", "r")

data = f.readlines()
f.close()

print("Total number of lines:", len(data))

f = open("output.txt", "w")
f.writelines(data[:2])
f.close()

print("First two lines written to output.txt")
