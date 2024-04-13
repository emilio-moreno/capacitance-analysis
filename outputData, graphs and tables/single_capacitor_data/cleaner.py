import csv

with open("./datos_137nF_44Mohm_f2.txt", "r") as f:
    data = csv.reader(f)
    data = list(data)

print(data)
data_seconds = []
for n in data:
    data_seconds.append([float(n[0]), float(n[1])])

with open("./datos_137nF_44Mohm_f2_cleaned.txt", "w", newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerows(data_seconds)
