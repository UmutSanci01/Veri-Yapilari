import random

def guess_opposit_side(n):
    return 7 - n

if __name__ == "__main__":
    for i in range(10):
        side = random.randint(1, 6)
        print(f"side {side} opposit side {guess_opposit_side(side)}")