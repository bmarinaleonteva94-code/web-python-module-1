# быки ккоровы
import random
generate_number = [random.randint(0,9) for _ in range(4)]
hidden_number = int("".join(map(str, generate_number)))


print(hidden_number)