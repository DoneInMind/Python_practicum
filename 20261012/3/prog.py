w = len(input()) - 2
h, gas_h = 0, 0
while (line := input())[1] != "#":
    h += 1
    if (line[1] == "."): gas_h += 1

gas, liq, total = gas_h * w, (h - gas_h) * w, h * w
liq_rows = (liq + h - 1) // h
print("#" * (h + 2))
for i in range(w):
    print("#" + ("." if i < w - liq_rows else "~") * h + "#")
print("#" * (h + 2))

big = max(gas, liq)
gas_fr, liq_fr = f"{gas}/{total}", f"{liq}/{total}"
fw = max(len(gas_fr), len(liq_fr))
print(f"{'.' * round(20 * gas / big):<20} {gas_fr:>{fw}}")
print(f"{'~' * round(20 * liq / big):<20} {liq_fr:>{fw}}")
