

def solution_p2(data):
    position = 50
    count = 0
    for instruction in data:
        direction, amount = instruction
        while amount > 100:
            count += 1
            amount -= 100

        assert amount > 0
        assert amount < 100
        current_pos = position
        if direction == "L":
            position = position - amount
            if position <= 0 and not current_pos == 0:
                count += 1
            position = (position + 100) % 100
        else:
            position = position + amount
            if position >= 100 and not current_pos == 0:
                count += 1
            position = position % 100

    return count

def solution_p1(data):
    position = 50
    count = 0
    for instruction in data:
        direction, amount = instruction
        if direction == "L":
            position = (position - amount + 100) % 100
        else:
            position = (position + amount) % 100
        if position == 0:
            count += 1

    return count


def parse_input(text_file):

    directions = []
    with open(text_file, "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            value = int(line[1:])
            directions.append((direction,value))
    return directions


def main():
    data = parse_input("example.txt")
    ans = solution_p1(data)
    print(f"Answer example 1: {ans}")

    data = parse_input("input.txt")
    ans = solution_p1(data)
    print(f"Answer input 1: {ans}")


    data = parse_input("example.txt")
    ans = solution_p2(data)
    print(f"Answer example 1: {ans}")

    data = parse_input("input.txt")
    ans = solution_p2(data)
    print(f"Answer example 1: {ans}")


if __name__ == "__main__":
    main()