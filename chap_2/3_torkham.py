class TorKham:
    def __init__(self):
        self.words = []
    def restart(self):
        self.words = []
        return "game restarted"
    def play(self, word):
        if len(self.words) > 0:
            last_word = self.words[-1]
            if word.lower() == last_word.lower():
                return "game over"
            if last_word[-2:].lower() != word[:2].lower():
                return "game over"
        self.words.append(word)
        return f"'{word}' -> {self.words}"

torkham = TorKham()
print("*** TorKham HanSaa ***")
s = input("Enter Input : ").split(',')
for command in s:
    if command.startswith("P "):
        word = command[2:].strip()
        if word.isalpha():
            result = torkham.play(word)
            if result == "game over":
                print(f"'{word}' -> game over")
                break
            else:
                print(result)
        else:
            print(f"'{command}' is Invalid Input !!!")
            break
    elif command.strip() == "R":
        print(torkham.restart())
    elif command.strip() == "X":
        break
    else:
        print(f"'{command}' is Invalid Input !!!")
        break