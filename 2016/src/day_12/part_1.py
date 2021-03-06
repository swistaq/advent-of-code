with open("data.txt") as file:
    input_data = file.read().splitlines()


class AssembunnyProcessor:
    def __init__(self, instruction_list):
        self.register = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0
        }
        self.pointer = 0
        self.instruction_list = instruction_list

    def cpy(self, x: str, y: str):
        if x.isalpha():
            self.register[y] = self.register[x]
        elif x.isdigit():
            self.register[y] = int(x)
        else:
            raise NotImplementedError
        self.pointer += 1

    def inc(self, x: str):
        self.register[x] += 1
        self.pointer += 1

    def dec(self, x: str):
        self.register[x] -= 1
        self.pointer += 1

    def jnz(self, x, y):
        if x.isalpha() and self.register[x] != 0:
            self.pointer += int(y)
        elif x.isdigit() and int(x) != 0:
            self.pointer += int(y)
        else:
            self.pointer += 1

    def exec(self, instruction: str):
        splitted = instruction.split()
        if splitted[0] == "cpy":
            self.cpy(splitted[1], splitted[2])
        elif splitted[0] == "inc":
            self.inc(splitted[1])
        elif splitted[0] == "dec":
            self.dec(splitted[1])
        elif splitted[0] == "jnz":
            self.jnz(splitted[1], splitted[2])
        else:
            raise NotImplementedError

    def begin(self):
        while self.pointer < len(self.instruction_list):
            self.exec(self.instruction_list[self.pointer])


def main():
    processor = AssembunnyProcessor(input_data)
    processor.begin()
    answer = processor.register["a"]

    print("answer:", answer)

if __name__ == "__main__":
    main()
