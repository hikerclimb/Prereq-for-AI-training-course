with open('Hands-On-Excercises-1_Module2.txt', "r") as file:
    for line in file:
        if line.strip() == "ERROR":
            print(line.strip())
