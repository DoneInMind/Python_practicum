class Maze:
    def __init__(self, n):
        self.cells = [["█"] * (2 * n + 1) for _ in range(2 * n + 1)]
        for y in range(n):
            for x in range(n):
                self.cells[2 * y + 1][2 * x + 1] = "·"

    def __setitem__(self, key, value):
        x0, s, y1 = key
        y0, x1 = s.start, s.stop
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1)):
                self.cells[2 * y + 2][2 * x0 + 1] = value
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1)):
                self.cells[2 * y0 + 1][2 * x + 2] = value

    def __getitem__(self, key):
        x0, s, y1 = key
        y0, x1 = s.start, s.stop
        seen, stack = {(x0, y0)}, [(x0, y0)]
        while stack:
            x, y = stack.pop()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                if self.cells[2 * y + 1 + dy][2 * x + 1 + dx] == "·" and (x + dx, y + dy) not in seen:
                    seen.add((x + dx, y + dy))
                    stack.append((x + dx, y + dy))
        return (x1, y1) in seen

    def __str__(self):
        return "\n".join(map("".join, self.cells))

import sys
exec(sys.stdin.read())
