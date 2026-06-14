text = input("Write your diary: ")

with open("diary.txt", "w") as file:

    file.write(text)

print("Diary saved!")