n = 5


while n != 0:
  if n == 1:
    print("En liten apekatt sitter i ett tre")
    print("Den erter krokodillen: 'Du kan ikke ta meg ned'")
  else:
    print(str(n) + " små apekatter sitter i ett tre")
    print("De erter krokodillen: 'Du kan ikke ta oss ned'")
  print("Sa kom krokodillen, så diger og så svær og slurp!")
  n = n - 1
  if n == 0:
    print("Da var det ingen apekatter der")
  else:
    print("Så var de bare " + str(n) + " apekatter der")
  print("\n")
