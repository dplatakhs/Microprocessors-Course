from dataclasses import dataclass
from random import randint, choice
import random
# importing the required module
import matplotlib.pyplot as plt

@dataclass
class element:
    gate: str
    input1: float
    input2: float
    input3: float
    input4: float
    input5: float
    input6: float
    input7: float
    input8: float
    input9: float
    input10: float
    numInputs: int
    output: int

@dataclass
class individual:
    L1: list
    L2: list


def spAND(inputs,temp):
    if(len(inputs)>=2):
        inp1 = float(inputs.pop(0))
        inp2 = float(inputs.pop(0))
        temp = inp1*inp2
    for i in inputs:
        temp = temp*float(i)
    return temp
def spNOT(a):
    if((a==0 or a==1)):
        return 1-a
def spNOR(inputs,temp):
    if(len(inputs)>=2):
        inp1 = float(inputs.pop(0))
        inp2 = float(inputs.pop(0))
        temp = (1-inp1)*(1-inp2)
    for i in inputs:
        temp = (1-temp)*(1-float(i))
    return temp
def spOR(inputs,temp):
    temp=spNOR(inputs,temp)
    return 1-temp
def spXOR(inputs,temp):
    if(len(inputs)>=2):
        inp1 = float(inputs.pop(0))
        inp2 = float(inputs.pop(0))
        temp = (1-inp1)*inp2+inp1*(1-inp2)
    for i in inputs:
        temp = (1-temp)*float(i)+temp*(1-float(i))
    return temp
def spNAND(inputs,temp):
    temp=spAND(inputs,temp)
    return 1- temp
def spNXOR(inputs,temp):
    temp=spXOR(inputs,temp)
    return 1- temp

# it has as an arguement a single element. The process() is called from the circuit() where in a for-loop it passes
# every element of elementsTable to process(). There it receives the inputs and finds the output based on the gate of the element
def process(E, signalsTable,signalsSymbols):
    #print("The gate is: ", E.gate)
    out = signalsSymbols.index(E.output)
    #inp1 = signalsSymbols.index(E.input1)
    #inp2 = signalsSymbols.index(E.input2)
    # HERE WE CHANGED SOMETHING, BECAUSE OF THE MANY INPUTS PROBLEM WE 
    # ARE GOING TO PUT LISTS FOR INPUTS
    temp=0
    inputList = []
    #print("THE symbol of input1 and its INDEX OF SUMBOL INPUT1",E.input1,signalsSymbols.index(E.input1))
    indexOfinput1=signalsSymbols.index(E.input1)
    if(E.numInputs > 0):
        inputList.append(signalsTable[signalsSymbols.index(E.input1)])
    if(E.numInputs > 1):
        inputList.append(signalsTable[signalsSymbols.index(E.input2)])
    if(E.numInputs > 2):
        inputList.append(signalsTable[signalsSymbols.index(E.input3)])
    if(E.numInputs > 3):
        inputList.append(signalsTable[signalsSymbols.index(E.input4)])
    if(E.numInputs > 4):
        inputList.append(signalsTable[signalsSymbols.index(E.input5)])
    if(E.numInputs > 5):
        inputList.append(signalsTable[signalsSymbols.index(E.input6)])
    if(E.numInputs >6):
        inputList.append(signalsTable[signalsSymbols.index(E.input7)])
    if(E.numInputs > 7):
        inputList.append(signalsTable[signalsSymbols.index(E.input8)])
    if(E.numInputs > 8):
        inputList.append(signalsTable[signalsSymbols.index(E.input9)])
    if(E.numInputs > 9):
        inputList.append(signalsTable[signalsSymbols.index(E.input10)])

    #print("DA LIST of INPUTS: ",inputList)
    if(E.gate=='AND'):
        signalsTable[out]=spAND(inputList,temp)
    elif(E.gate=='NOT'):
        signalsTable[out]=spNOT(inputList)
    elif(E.gate=='OR'):
        signalsTable[out]=spOR(inputList,temp)
    elif(E.gate=='NOR'):
        signalsTable[out]=spNOR(inputList,temp)
    elif(E.gate=='XOR'):
        signalsTable[out]=spXOR(inputList,temp)
    elif(E.gate=='NXOR'):
        signalsTable[out]=spNXOR(inputList,temp)
    elif(E.gate=='NAND'):
        signalsTable[out]=spNAND(inputList,temp)

# This function implements the circuit. It goes through all the elements of the elementsTable and calls the process()
# There -in process()- finds the output of the gate based upon the inputs of the gate.
def circuit(E, signalsTable, signalsSymbols):
    for i in range(len(E)):
        process(E[i], signalsTable, signalsSymbols)

# In this function we take the file and we initialize our elementsTable. Of course we also check the type of file
# -if it does or doesn't have topInputs-. So it returns the topInputs, the signalsSymbols(a list of all the symbols)
# a signalsTable (where it's index is associated with the signalsSymbols: signalsTable[i] has the value of the symbol of signalsSymbols[i])
# and finally the elementsTable including all the gates and their inputs/outputs.
def initializer(fname,topInputs,signalsSymbols):
    # topInputs=[0,1,2]
    # signalsTable=[1,1,0,0,0,0]
    #               a,b,c,d,e,f
    # first: gate  then we get the index from topInputs and we pick the input of "welcoming" gates
    # THEN, on output, we declare the index of the output variable, on E1 is the index of 4('e')
    
    
    flagInput = 0
    i=0
    f = open(fname, "r")
    firstNine = f.read(9)
    if(firstNine == 'topInputs'):
        line = f.readline() # read the line
        allparam = line.split() #split it
        #signalsSymbols.insert(i,firstNine) #insert it
        for i in range(len(allparam)):
            topInputs.append(allparam[i])
    else:
        # here we come in case there isnt a topInputs list. In that case we close
        # the f and we re-open it
        f.close()
        f = open(fname, "r")
        flagInput+=1
    
    #------------------------------------------------------
    #at this point we are supposed to have an topInput array if it was declared in the file
    #now it's time to start creating elements
    elementsArray = []
    num_lines = sum(1 for line in open(fname))
    for i in range(num_lines):
        # we initialize as many elements as the lines of the file as AND gates, but later we will change them
        E1 = element('AND',0,0,0,0,0,0,0,0,0,0,0,0)
        elementsArray.append(E1)
    k=0
    #print(elementsArray)
    for line in f:
        # lineArray = ['AND',2,3,7] for example
        lineArray = line.split()
        elementsArray[k].gate = lineArray[0]
        elementsArray[k].output = lineArray[1]
        elementsArray[k].input1 = lineArray[2]
        elementsArray[k].numInputs = len(lineArray)-2
        if(len(lineArray)>3):
            elementsArray[k].input2 = lineArray[3]
        if(len(lineArray)>4):
            elementsArray[k].input3 = lineArray[4]
        if(len(lineArray)>5):
            elementsArray[k].input4 = lineArray[5]
        if(len(lineArray)>6):
            elementsArray[k].input5 = lineArray[6]
        if(len(lineArray)>7):
            elementsArray[k].input6 = lineArray[7]
        if(len(lineArray)>8):
            elementsArray[k].input7 = lineArray[8]
        if(len(lineArray)>9):
            elementsArray[k].input8 = lineArray[9]
        if(len(lineArray)>10):
            elementsArray[k].input9 = lineArray[10]
        if(len(lineArray)>11):
            elementsArray[k].input10 = lineArray[11]
        k+=1


        
    
    # ----------------------------------------------------------
    # at this point we have a perfect elementsArray
    
    
    # now dont forget that in case we dont have an topInputs, we still
    # have to find them. we do topInputs = signalsSymbols-outputSignals
    outputSignals = []
    i=0
    
    # now we will create the FULL signalsSymbols list
    signalsSymbols,outputSignals = createFullSignalsSymbols(elementsArray,outputSignals,signalsSymbols)
    

    print(outputSignals)            
    #destroy duplicates
    signalsSymbols = list(dict.fromkeys(signalsSymbols))
    if(flagInput != 0):
        topInputs = list(set(signalsSymbols) - set(outputSignals)) + list(set(outputSignals) - set(signalsSymbols))
    
    # now we initialize the signalsTable
    signalsTable = []
    for i in range(len(signalsSymbols)):
        signalsTable.append(0)
    f.close()
    return topInputs,signalsSymbols,signalsTable,elementsArray

# This function runs through our file to collect all the symbols of the signals. It's called from the initializer() when
# it's time to make the FULL signalsSymbols
def createFullSignalsSymbols(elementsArray,outputSignals,signalsSymbols):
    for i in range(len(elementsArray)):
        # check if parameter exists already
        newSymbol = elementsArray[i].output
        exist_output = signalsSymbols.count(newSymbol)
        #append the output to the output array
        outputSignals.append(newSymbol)
        
        if(exist_output == 0):
            #print("GOT IN with symbol: ",chr(newSymbol+97))
            signalsSymbols.append(newSymbol)

                    
        #checking input1
        newSymbol = elementsArray[i].input1
        exist_input1 = signalsSymbols.count(newSymbol)
        if(exist_input1 == 0):
            signalsSymbols.append(newSymbol)
            
                    
        # check if there is an input2, because if it's NOT gate, there isn't
        if(elementsArray[i].gate != 'NOT'):
            newSymbol = elementsArray[i].input2
            exist_input2 = signalsSymbols.count(newSymbol)
            if(exist_input2 == 0):
                signalsSymbols.append(newSymbol)

            newSymbol = elementsArray[i].input3
            exist_input3 = signalsSymbols.count(newSymbol)
            if(exist_input3 == 0):
                signalsSymbols.append(newSymbol)
            

            newSymbol = elementsArray[i].input4
            exist_input4 = signalsSymbols.count(newSymbol)
            if(exist_input4 == 0):
                signalsSymbols.append(newSymbol)
            
            newSymbol = elementsArray[i].input5
            exist_input5 = signalsSymbols.count(newSymbol)
            if(exist_input5 == 0):
                signalsSymbols.append(newSymbol)
            
            newSymbol = elementsArray[i].input6
            exist_input6 = signalsSymbols.count(newSymbol)
            if(exist_input6 == 0):
                signalsSymbols.append(newSymbol)
            
            newSymbol = elementsArray[i].input7
            exist_input7 = signalsSymbols.count(newSymbol)
            if(exist_input7 == 0):
                signalsSymbols.append(newSymbol)
            
            newSymbol = elementsArray[i].input8
            exist_input8 = signalsSymbols.count(newSymbol)
            if(exist_input8 == 0):
                signalsSymbols.append(newSymbol)
            
            newSymbol = elementsArray[i].input9
            exist_input9 = signalsSymbols.count(newSymbol)
            if(exist_input9 == 0):
                signalsSymbols.append(newSymbol)
            
            newSymbol = elementsArray[i].input10
            exist_input10 = signalsSymbols.count(newSymbol)
            if(exist_input10 == 0):
                signalsSymbols.append(newSymbol)
    return signalsSymbols,outputSignals



def testbench(topInputs, signalsTable, elementsTable, signalsSymbols):
    #EDWWW print("signalsTable from testbench: ",signalsTable)
    circuit(elementsTable, signalsTable,signalsSymbols)
    #print("This is the signals table ", signalsTable)
    #print("topInputs ARE THE FOLLOWING: ", topInputs)
    #print("The result of the circuit: ",signalsTable[elementsTable[len(elementsTable)-1].output],"\n")
    return signalsTable

def countSwitchesofIndividual(topInputs, signalsTable, elementsTable, signalsSymbols,L1,L2):
    # first we have to create an individual of L=2 (that means to signalsTables/topInputs)
    # and after that we have to count the differences
    countSwitch=0
    #print("L1 and L2: ",L1,L2)
    s1=testbench(L1,signalsTable,elementsTable,signalsSymbols)
    s2=testbench(L2,signalsTable,elementsTable,signalsSymbols)
    #print("s1 and s2: ",s1,s2)
    for i in range(len(s1)):
        #check if the signalsSymbols[i]-->the signal, it's in topInputs
        newSymbol = s1[i]
        exist = topInputs.count(newSymbol)
        # if it exists continue
        if(exist != 0):
            continue
        if(s1[i] != s2[i]):
            print("found a different")
            countSwitch+=1
    #return the topInputs!!! not the signalsTable
    return countSwitch, L1, L2

def findBiggestScore(topInputs,signalsTable,elementsTable,signalsSymbols,workbench):
    score=[]
    # L=2 (so L1,L2) and N=2000
    for i in range(len(workbench)):
        #print("L1 and L2: ",workbench[i].L1, workbench[i].L2)
        count, workbench[i].L1, workbench[i].L2 = countSwitchesofIndividual(topInputs,signalsTable,elementsTable,signalsSymbols,workbench[i].L1, workbench[i].L2)
        score.append(count)
        #workbench.append(individual(L1,L2))
    #find the index of the most changed invdividuals
    scoreG1=0
    indexG1=0
    scoreG2=0
    indexG2=0
    for i in range(len(workbench)):
        if(scoreG1<score[i]):
            scoreG1=score[i]
            indexG1=i
    for i in range(len(workbench)):
        #ignore the biggest score
        if(i==indexG1):
            continue
        if(scoreG2<score[i]):
            scoreG2=score[i]
            indexG2=i
    scoreG=scoreG1
    #print(scoreG)
    return workbench[indexG1],workbench[indexG2],scoreG  

def mutation(ind1,ind2):
    # Right now the individual(ind1,ind2) has two topInputs(L1,L2)
    # from each we will pick either L1 or L2 to form a new individual
    C=1
    workbench=[]
    #Take a hold of the L1/L2 of each individual and later pick randomly from each individual
    Lind1 = [ind1.L1,ind1.L2]
    Lind2 = [ind2.L2,ind2.L1]
    childOriginal = individual(Lind1[random.randint(0, 1)],Lind2[random.randint(0, 1)])
    # R=1 from workbench: one from L1 and one from L2 
    m=5 #5% chance of mutation
    # time to make a new population/workload
    childFake = childOriginal
    changed=[]
    for j in range(30):
        # time for mutation of ONE! ONLY ONE INDIVIDUAL!
        # FIRST the L1
        childOriginal = childFake 
        for i in range(len(childOriginal.L1)):
            pos = random.randint(0, 100)
            if(pos<5):
                #if it falls under the m=5 then change its bit from 0->1 or 1->0
                #print("something changed at L1!!")
                #print("BEFORE: ",childOriginal)
                childOriginal.L1[i] = 1 - childOriginal.L1[i]
                #print("after: ",childOriginal)
        changedL1=childOriginal.L1
        # THEN the L2
        for k in range(len(childOriginal.L2)):
            pos = random.randint(0, 100)
            if(pos<5):
                #if it falls under the m=5 then change its bit from 0->1 or 1->0
                childOriginal.L2[k] = 1 - childOriginal.L2[k]
        changedL2=childOriginal.L2
        childMutated = individual(changedL1,changedL2)
        workbench.append(childMutated)
        changed.append(j)
        #print("Mutated and original",childFake,childOriginal)
    #print(changed)
    #print(workbench)
    return workbench


signalsSymbols = []
topInputs = []
topInputs,signalsSymbols,signalsTable,elementsTable=initializer("big.txt",topInputs,signalsSymbols)
#for i in range(len(elementsTable)):
#    print("And the element: ",elementsTable[i])
print("These are the signals SYMBOLS: ",signalsSymbols)
print("The input symbols are: ",topInputs)
print("And our signals table: ", signalsTable)
#print("And the top Inputs are: ", topInputs)
print("-----------------------------------TESTBENCH BELOW---------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("length of signalsTable and signalsSymbols: ",len(signalsSymbols),len(signalsSymbols))
signalsTable=testbench(topInputs,signalsTable,elementsTable,signalsSymbols)
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------COUNT SWITCHES----------------------------------------")
print("-----------------------------------------------------------------------------------------")
print("We have this many signals(topInputs NOT included): ",len(signalsTable)-len(topInputs))
#first we initialize the workbench randomly
workbench=[]
scoreList=[]
# L=2 (so L1,L2) and N=30, create a population for the firstTime
for i in range(30):
    # now we create the two random arrays
    L1=[] # initialize L1 and L2
    L2=[]
    # and now we create L1 and L2. This only happens on generation1
    for i in range(len(topInputs)):
        L1.append(random.randint(0, 1))
        L2.append(random.randint(0, 1))
        workbench.append(individual(L1,L2))
# at this point we have an initial workbench and now in every generation we will create a new workbench
#----------------------------------------------Generation 1-----------------------------------
# w1/w2 are the individuals with the biggest scores.
w1,w2,score = findBiggestScore(topInputs,signalsTable,elementsTable,signalsSymbols,workbench)
for i in range(10):    
    scoreList.append(score)
    # now we mutitate and we generate a new population of 30 individuals so, generation 1
    workbench=mutation(w1,w2)
    #print("This is the i and workbench: \n",i,workbench[0])
    # w1/w2 are the individuals with the biggest scores.
    w1,w2,score = findBiggestScore(topInputs,signalsTable,elementsTable,signalsSymbols,workbench)
    #-----------------------IN NEXT LOOP NEW GENERATION IS ABOUT TO COME.-----------------------

print("the scores of each generation: ",scoreList)
#print("the legth of our workbench: ",len(workbench))
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")