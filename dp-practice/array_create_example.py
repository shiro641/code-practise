"""
Creating arrays (lists) in Python — runnable examples.

Run me:  python array_create_example.py
Each section prints its result so you can see exactly what's built.
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. Basic ways to make a 1D list")
# ---------------------------------------------------------------------------

empty = []
literal = [1, 2, 3, 4]
repeated = [0] * 5                 # [0, 0, 0, 0, 0]  (safe: ints are immutable)
from_range = list(range(5))        # [0, 1, 2, 3, 4]

print("empty     :", empty)
print("literal   :", literal)
print("repeated  :", repeated)
print("from_range:", from_range)


# ---------------------------------------------------------------------------
section("2. List comprehension: map / transform")
# ---------------------------------------------------------------------------

doubles = [x * 2 for x in range(5)]        # [0, 2, 4, 6, 8]
squares = [x ** 2 for x in range(5)]       # [0, 1, 4, 9, 16]
as_str = [str(x) for x in range(3)]        # ['0', '1', '2']
bars = ['*' * x for x in range(4)]         # ['', '*', '**', '***']

print("doubles:", doubles)
print("squares:", squares)
print("as_str :", as_str)
print("bars   :", bars)


# ---------------------------------------------------------------------------
section("3. Filter — `if` at the END drops items")
# ---------------------------------------------------------------------------

evens = [x for x in range(10) if x % 2 == 0]     # [0, 2, 4, 6, 8]
big = [x for x in range(10) if x > 5]            # [6, 7, 8, 9]

print("evens:", evens)
print("big  :", big)


# ---------------------------------------------------------------------------
section("4. Conditional value — `if/else` at the FRONT keeps all items")
# ---------------------------------------------------------------------------

labels = ['even' if x % 2 == 0 else 'odd' for x in range(4)]
# ['even', 'odd', 'even', 'odd']
clamped = [x if x % 2 == 0 else -1 for x in range(5)]
# [0, -1, 2, -1, 4]

print("labels :", labels)
print("clamped:", clamped)

# Combine both: filter out 0, then transform the rest
combo = [x * 10 if x > 2 else x for x in range(6) if x != 0]
print("combo  :", combo)                          # [1, 2, 30, 40, 50]


# ---------------------------------------------------------------------------
section("5. Multiple `for` clauses — nested loops, FLAT result")
# ---------------------------------------------------------------------------

pairs = [(r, c) for r in range(2) for c in range(3)]
# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
print("pairs:", pairs)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [val for row in matrix for val in row]     # [1, 2, 3, 4, 5, 6]
print("flat :", flat)


# ---------------------------------------------------------------------------
section("6. Nested comprehension — builds a real 2D grid")
# ---------------------------------------------------------------------------

rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]          # 3x4 of zeros
print("grid:", grid)

mult_table = [[r * c for c in range(4)] for r in range(4)]
print("mult_table:")
for row in mult_table:
    print("   ", row)


# ---------------------------------------------------------------------------
section("7. THE CLASSIC TRAP: shared inner list vs. fresh lists")
# ---------------------------------------------------------------------------

good = [[0] * 3 for _ in range(2)]   # fresh list each row
bad = [[0] * 3] * 2                  # same list referenced twice

good[0][0] = 9
bad[0][0] = 9

print("good (comprehension):", good)   # [[9, 0, 0], [0, 0, 0]]  ✅
print("bad  (* rows)       :", bad)    # [[9, 0, 0], [9, 0, 0]]  ❌
print("good rows same obj? :", id(good[0]) == id(good[1]))  # False
print("bad  rows same obj? :", id(bad[0]) == id(bad[1]))    # True


# ---------------------------------------------------------------------------
section("8. Same syntax, other collection types")
# ---------------------------------------------------------------------------

a_set = {x for x in range(5)}              # set comprehension
a_dict = {x: x * x for x in range(4)}      # dict comprehension
a_gen = (x for x in range(5))              # generator (lazy, NOT a list!)

print("set  :", a_set)
print("dict :", a_dict)
print("gen  :", a_gen, "-> list():", list(a_gen))


if __name__ == "__main__":
    print("\nDone — scroll up to compare each section.")
