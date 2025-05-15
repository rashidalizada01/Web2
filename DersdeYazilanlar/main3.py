# Satır ve sütun sayısını tanımlayalım
rows = 4
cols = 4

# Matrisi oluşturma
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        if i == 0:
            # İlk satırda "*" ve sayılar
            row.append(f"{j} ") if j > 0 else row.append("* ")
        else:
            # Diğer satırlarda harfler ve "x" karakteri
            row.append("x " if j > 0 else chr(97 + i - 1) + " ")  # chr(97) 'a' harfini verir
    matrix.append(row)

# Matrisi yazdırma
for row in matrix:
    print(''.join(row))
