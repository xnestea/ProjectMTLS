### accuracy of final prediction based on model ###
### use DB with states in it to check real life accuracy
testDB = "../datasets/oldtestDB/1prottest.txt"
output = "../results/predictedPSSM.txt"
truestates = []
for i, line in enumerate(open(testDB, "r")):
    if i % 3 == 2:
        truestates.append(line.strip("\n"))
predstates = []
for i, line in enumerate(open(output, "r")):
    if i % 3 == 2:
        predstates.append(line.strip("\n"))

### measure true accuracy
totalscore = 0
correctpred = 0
for i in range(len(truestates)):
    for state in range(len(truestates[i])):
        totalscore += 1
        if truestates[i][state] == predstates[i][state]:
            correctpred += 1

print (correctpred / totalscore)