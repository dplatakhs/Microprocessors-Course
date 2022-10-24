from dataclasses import dataclass
@dataclass
class element:
    gate: str
    input1: float
    input2: float
    output: int

print("-----------------")

def spAND(a,b):
    return a*b

def spNOT(a):
    return 1-a

def process(E, signalsTable):
    print("The gate is: ", E.gate)
    if(E.gate=='AND'):
        signalsTable[E.output]=spAND(signalsTable[E.input1], signalsTable[E.input2])
    else:
        signalsTable[E.output]=spNOT(signalsTable[E.input1])

def circuit(E, signalsTable):
    for i in range(len(E)):
        process(E[i], signalsTable)
        print("The first input: ",E[i].input1," the second input: ",E[i].input2," and the index of output",E[i].output)

def initializer(topInputs):
    # topInputs=[0,1,2]
    # signalsTable=[1,1,0,0,0,0]
    #               a,b,c,d,e,f
    # first: gate  then we get the index from topInputs and we pick the input of "welcoming" gates
    # THEN, on output, we declare the index of the output variable, on E1 is the index of 4('e')
    E1 = element('AND',0,0,0)
    E2 = element('AND',0,0,0)
    E3 = element('AND',0,0,0)
    
    #print("TOPINPUTS AND SIGNALSTABLE",topInputs,signalsTable,"\n")
    E1.gate='AND'
    E1.input1=topInputs[0]#signalsTable[topInputs[0]]
    E1.input2=topInputs[1]#signalsTable[topInputs[1]]

    # edw pera gia output exoyme INDEX, dhladh h thesh 4 tou signalsTable DEN KSEROUME ti timh exei
    # kai gia na mathoume tha prepei na perasoume to element(E1) apo thn process
    E1.output=4;

    # here the input of NOT Gate is at the index of 2, singalsTable[2] = 'c'
    # output of NOT Gate is at the index of 5, signalsTable[5] = 'f'
    E2.gate='ΝΟΤ'
    E2.input1=topInputs[2]#signalsTable[topInputs[2]]
    E2.output=5;

    # here the input of AND Gate is at the index of 4,5: singalsTable[4,5] = 'e','f'
    # output of AND Gate is at the index of 3, signalsTable[3] = 'd'
    E3.gate='AND'
    E3.input1=4#signalsTable[4]
    E3.input2=5#signalsTable[5]
    E3.output=3;
    ElementsTable=[E1,E2,E3]

    return topInputs,ElementsTable

def testbench(topInputs, signalsTable, elementsTable):
    #EDWWW print("signalsTable from testbench: ",signalsTable)
    circuit(elementsTable, signalsTable)
    print("This is the signals table ", signalsTable)
    print("The result of the circuit: ",signalsTable[elementsTable[len(elementsTable)-1].output],"\n")

# ---------------------!!!!!!!!!!!!!!!!!!!------------------------------------------
# HERE THE PROGRAM STARTS, IN ORDER TO CHANGE THE GATES AND THE INPUT TABLE, GO TO DEMOFILE.TXT AND EDIT!!!
#signalsSymbols = []
topInputs = [0,1,2]
topInputs,elementsTable=initializer(topInputs)
#print("These are the signals SYMBOLS: ",signalsSymbols)
signalsTable = [0, 0, 0, 0, 0, 0]
print("And the elements table: ",elementsTable)
print("And our signals table: ", signalsTable)

# And our signals table:  [0, 0, 0, 0, 0, 0]
print("OUR ELEMENTS TABLE",elementsTable)
# HERE WE PLAY WITH OUR SINGALS TABLE. CHANGE THE NEXT LINE 
signalsTable=[1,1,0,1,0,1]
testbench(topInputs,signalsTable,elementsTable)
signalsTable=[1,0,0,1,0,1]
testbench(topInputs,signalsTable,elementsTable)

print("-----------------")