with open("data.txt") as file:
    input_data = str(file.readlines()[0]).split(", ")

test_input_1 = ["R2", "L3"]  # result: 5 (2E, 3N)
test_input_2 = ["R2", "R2", "R2"]  # result: 2 (2S)
test_input_3 = ["R5", "L5", "R5", "R3"]  # result: 12


class Direction(tuple):
    """ Direction wrapper """
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    current_direction = 0

    def turn_right(self):
        self.current_direction = (self.current_direction + 1) % 4
        return self.directions[self.current_direction]

    def turn_left(self):
        self.current_direction = (self.current_direction - 1) % 4
        return self.directions[self.current_direction]

    def get_current(self):
        return self.directions[self.current_direction]


def find_distance(instructions):
    current_direction = Direction()
    current_position = (0, 0)

    for move in instructions:
        move_direction = move[:1]
        move_distance = int(move[1:])

        if move_direction == "R":
            current_direction.turn_right()
        else:
            current_direction.turn_left()

        new_x = current_position[0] + current_direction.get_current()[0] * move_distance
        new_y = current_position[1] + current_direction.get_current()[1] * move_distance
        current_position = new_x, new_y

    return abs(current_position[0]) + abs(current_position[1])


def main():
    test_1 = find_distance(test_input_1)
    test_2 = find_distance(test_input_2)
    test_3 = find_distance(test_input_3)
    answer = find_distance(input_data)

    print("test_1:", test_1)
    print("test_2:", test_2)
    print("test_3:", test_3)
    print("answer:", answer)

if __name__ == "__main__":
    main()
