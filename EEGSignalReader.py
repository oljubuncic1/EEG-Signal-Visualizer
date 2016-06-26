import csv
import matplotlib.pyplot as plt

def signalParser(electrodeIndex):

# the file contains 14980 instances of EEG measurements
#first 14 columns are the signal values from different electrodes
# the last column is the eye state: 1-closed, 0-open
#time of the measurement is 117 seconds

    interval = 117. / 14980
    val = 0
    time = []
    eegValue = []

    # eeg value = csv value - avg(all_values)

    sum = 0.

    with open('EEGSignal.csv', 'rb') as signalFile:
        signalReader = csv.reader(signalFile)
        for row in signalReader:
            time.append(val)
            val += interval
            eegValue.append(float(row[electrodeIndex]))
            sum += float(row[electrodeIndex])

    avg = sum / 14980.

    if(electrodeIndex != 14):
        for i in range(0, 14980):
            eegValue[i] -= avg

    return time, eegValue


#main


#x,y = signalParser(4)
#plt.plot(x,y)
#plt.show()