import csv
from math import sqrt


def calcuateAverageList(list):
    return sum(list) / len(list)


def calculatePercentError(x, y):
    return abs(x - y) / ((x + y) / 2) * 100


def calculateStandardDeviation(list_values):
    mean = calcuateAverageList(list_values)
    total = sum(list(map(lambda x: (x - mean)**2, list_values)))
    total = sqrt(total / len(list_values))
    return total


def calculateUncertaintyOfAverage(list_values):
    return calculateStandardDeviation(list_values) / sqrt(len(list_values))


datarows = []
with open("./outputData/EnParalelo/Descarga/EnParalelo_Descarga_OutputData.csv", "r") as data:
    dataCSV = csv.reader(data)

    for row in dataCSV:
        datarows.append(row)

print("Percent error for decay times (%) - Arduino vs Model")
for n in range(1, 6):
    model_decay_time = float(datarows[n][3])
    arduino_decay_time = float(datarows[n][4])
    percent_error = calculatePercentError(model_decay_time, arduino_decay_time)
    print(round(percent_error, 2))

print("\nPercent error for starting voltage (%) - Arduino vs Model")
for n in range(1, 6):
    model_starting_voltage = float(datarows[n][1])
    arduino_starting_voltage = float(datarows[n][2])
    percent_error = calculatePercentError(
        model_starting_voltage, arduino_starting_voltage)
    print(round(percent_error, 2))

capacitances = [float(datarows[n][-1]) for n in range(1, 6)]
avg_capacitance = calcuateAverageList(capacitances)

print("\nCapacitances (nF)")
for c in capacitances:
    print(c)
print("\nAverage capacitance (nF)")
print(round(avg_capacitance, 1))
print("\nUncertainty (nF)")
print(round(calculateUncertaintyOfAverage(capacitances), 1))
