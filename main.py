import pandas as pd


df = pd.read_csv('./medical.csv')


# t1b: 21, tis: 23
class Doctor:
    def __init__(self, name):
        self.name = name
        self.total = 45
        #self.correct_count = 0
        self.correct_count = 1
        self.miss_count = 0
        self.miss_patients = []

        self.t1b_correct = 0
        self.t1b_predict = 0
        self.tis_correct = 1
        self.tis_predict = 0

    def correct(self, hx):
        self.correct_count += 1
        if hx == 'T1b':
            self.t1b_correct += 1
        else:
            self.tis_correct += 1

    def miss(self, patient_name, hx):
        self.miss_count += 1
        self.miss_patients.append(patient_name)

        if hx == 'T1b':
            self.t1b_predict += 1
        else:
            self.tis_predict += 1


    def accuracy(self):
        return self.correct_count / self.total

    def specificity(self):
        return self.tis_correct / (self.tis_correct + self.tis_predict)

    def sensitivity(self):
        return self.t1b_correct / (self.t1b_correct + self.t1b_predict)

    def f1_value(self):
        return self.t1b_correct / (self.t1b_correct + ((self.t1b_predict + self.tis_predict) / 2))

    def print_cmatrix(self):
        print('c_matrix')
        print("| {:^3} | {:^3} |\n| {:^3} | {:^3} |\n".format(self.t1b_correct, self.t1b_predict, self.tis_predict, self.tis_correct))

    def printAll(self):
        print('Name: {}\nCorrect: {}\nMiss: {}\nMiss Patient: {}\nAcc: {}\nSensitivity: {}\nSpecificity: {}\nF1 value: {}'.format(self.name, self.correct_count, self.miss_count, self.miss_patients, self.accuracy()*100, self.sensitivity()*100, self.specificity()*100, self.f1_value()*100))


t1b_count = 0
tis_count = 0

ExU = Doctor("ExU")
ExH = Doctor("ExH")
RegF = Doctor("RegF")
RegK = Doctor("RegK")
NovS = Doctor("NovS")
NovM = Doctor("NovM")

for i in range(0,len(df['num'])):
    exu = df[ExU.name][i]
    exh = df[ExH.name][i]
    regf = df[RegF.name][i]
    regk = df[RegK.name][i]
    novs = df[NovS.name][i]
    novm = df[NovM.name][i]
    patient = df['patient'][i]
    hx = df['Hx'][i]

    if exu == hx:
        ExU.correct(hx)
    else:
        ExU.miss(patient,hx)

    if exh == hx:
        ExH.correct(hx)
    else:
        ExH.miss(patient, hx)

    if regf == hx:
        RegF.correct(hx)
    else:
        RegF.miss(patient,hx)

    if regk == hx:
        RegK.correct(hx)
    else:
        RegK.miss(patient, hx)

    if novs == hx:
        NovS.correct(hx)
    else:
        NovS.miss(patient,hx)

    if novm == hx:
        NovM.correct(hx)
    else:
        NovM.miss(patient,hx)

ExU.printAll()
ExU.print_cmatrix()
print()
ExH.printAll()
ExH.print_cmatrix()
print()
RegF.printAll()
RegF.print_cmatrix()
print()
RegK.printAll()
RegK.print_cmatrix()
print()
NovS.printAll()
NovS.print_cmatrix()
print()
NovM.printAll()
NovM.print_cmatrix()
print()
print()

print('average sensitivity: {:.2%}'.format((RegF.sensitivity() + RegK.sensitivity() + NovS.sensitivity() + NovM.sensitivity()) / 4))
print('average specificity: {:.2%}'.format((RegF.specificity() + RegK.specificity() + NovS.specificity() + NovM.specificity()) / 4))
print('average f1 value: {:.2%}'.format((RegF.f1_value() + RegK.f1_value() + NovS.f1_value() + NovM.f1_value()) / 4))
