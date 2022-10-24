from dataclasses import dataclass


@dataclass
class element:
    gate: str
    input1: float
    input2: float
    output: int

def spAND(a,b):
    return a*b
def spNOT(a):
    return 1-a
def spNOR(a,b):
    return (1-a)*(1-b)
def spOR(a,b):
    return 1-(1-a)*(1-b)
def spXOR(a,b):
    return (1-a)*b+a(1-b)
def spNAND(a,b):
    return 1-a*b
def spNXOR(a,b):
    return 1-(1-a)*b+a(1-b)

def process(E, signalsTable):
    print("The gate is: ", E.gate)
    if(E.gate=='AND'):
        signalsTable[E.output]=spAND(signalsTable[E.input1], signalsTable[E.input2])
    elif(E.gate=='NOT'):
        signalsTable[E.output]=spNOT(signalsTable[E.input1])
    elif(E.gate=='OR'):
        signalsTable[E.output]=spOR(signalsTable[E.input1], signalsTable[E.input2])
    elif(E.gate=='NOR'):
        signalsTable[E.output]=spNOR(signalsTable[E.input1], signalsTable[E.input2])
    elif(E.gate=='XOR'):
        signalsTable[E.output]=spXOR(signalsTable[E.input1], signalsTable[E.input2])
    elif(E.gate=='NXOR'):
        signalsTable[E.output]=spNXOR(signalsTable[E.input1], signalsTable[E.input2])
    elif(E.gate=='NAND'):
        signalsTable[E.output]=spNAND(signalsTable[E.input1], signalsTable[E.input2])


def circuit(E, signalsTable):
    for i in range(len(E)):
        process(E[i], signalsTable)
        # if last element
        print("The first input: ",E[i].input1," the second input: ",E[i].input2," and the index of output",E[i].output)


def initializer(fname,topInputs,signalsSymbols):
    # topInputs=[0,1,2]
    # signalsTable=[1,1,0,0,0,0]
    #               a,b,c,d,e,f
    # first: gate  then we get the index from topInputs and we pick the input of "welcoming" gates
    # THEN, on output, we declare the index of the output variable, on E1 is the index of 4('e')
    
    # we add the 'z' in order to compare and move on the list. If it was empty, there would be nothing
    # to compare to.
    signalsSymbols.append('z')
    flagInput = 0
    i=0
    f = open(fname, "r")
    firstNine = f.read(9)
    if(firstNine == 'topInputs'):
        f.read(1) # read the space
        firstNine = f.read(1) #read first Symbol
        #signalsSymbols.insert(i,firstNine) #insert it
        while(firstNine != '\n'):
            # now we will insert the symbol to its proper index
            #print(firstNine)
            for i in range(len(signalsSymbols)):
                if(ord(firstNine)>ord(signalsSymbols[i])):
                    continue
                else:
                    signalsSymbols.insert(i,firstNine)
            firstNine = f.read(1) #read the next space between symbols
            if(firstNine == '\n'):
                break
            firstNine = f.read(1) #read next Symbol
    else:
        # here we come in case there isnt a topInputs list. In that case we close
        # the f and we re-open it
        f.close()
        f = open(fname, "r")
        flagInput+=1
    
    # now we will create the topInputs list, but first we remove the 'z' we added.
    # if there was no topInputs in the file, this for-loop would be ignored.
    signalsSymbols.remove('z')
    for i in range(len(signalsSymbols)):
        ind = ord(signalsSymbols[i]) - ord('a')
        topInputs.append(ind)
    
    
    #------------------------------------------------------
    #at this point we are supposed to have an topInput array if it was declared in the file
    #now it's time to start creating elements
    elementsArray = []
    num_lines = sum(1 for line in open(fname))
    for i in range(num_lines):
        # we initialize as many elements as the lines of the file as AND gates, but later we will change them
        E1 = element('AND',0,0,0)
        elementsArray.append(E1)
    k=0
    #print(elementsArray)
    for line in f:
        # lineArray = ['AND',2,3,7] for example
        lineArray = line.split()
        elementsArray[k].gate = lineArray[0]
        elementsArray[k].output = ord(lineArray[1]) - ord('a')
        elementsArray[k].input1 = ord(lineArray[2]) - ord('a')
        #print(k,len(lineArray))
        if(len(lineArray)>3):
            elementsArray[k].input2 = ord(lineArray[3]) - ord('a')
        k+=1
        
    
    # ----------------------------------------------------------
    # at this point we have a perfect elementsArray
    
    
    # now dont forget that in case we dont have an topInputs, we still
    # have to find them. we do topInputs = signalsSymbols-outputSignals
    outputSignals = []
    i=0
    
    # now we will create the FULL signalsSymbols list
    for i in range(len(elementsArray)):
        # check if parameter exists already
        newSymbol = elementsArray[i].output
        exist_output = signalsSymbols.count(chr(newSymbol+97))
        #append the output to the output array
        outputSignals.append(chr(newSymbol+97))
        
        if(exist_output == 0):
            #print("GOT IN with symbol: ",chr(newSymbol+97))
            for j in range(len(signalsSymbols)+1):
                #check if parameter exists already
                if(j==len(signalsSymbols)):
                    signalsSymbols.append(chr(newSymbol+97))
                elif((newSymbol+97)>ord(signalsSymbols[j])):
                    continue
                else:
                    #print("new element: ",chr(newSymbol+97))
                    signalsSymbols.insert(j,chr(newSymbol+97))
                    
        #checking input1
        newSymbol = elementsArray[i].input1
        exist_input1 = signalsSymbols.count(chr(newSymbol+97))
        if(exist_input1 == 0):
            for j in range(len(signalsSymbols)):
                #check if parameter exists already
                if((newSymbol+97)>ord(signalsSymbols[j])):
                    continue
                else:
                    # add the char in correct place
                    signalsSymbols.insert(j,chr(newSymbol+97))
                    
        # check if there is an input2, because if it's not gate, there isn't
        if(elementsArray[i].gate != 'NOT'):
            newSymbol = elementsArray[i].input2
            exist_input2 = signalsSymbols.count(chr(newSymbol+97))
            for j in range(len(signalsSymbols)):
                #check if parameter exists already
                if((newSymbol+97)>ord(signalsSymbols[j])):
                    continue
                else:
                    # add the char in correct place
                    signalsSymbols.insert(j,chr(newSymbol+97))
                    
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



def testbench(topInputs, signalsTable, elementsTable):
    #EDWWW print("signalsTable from testbench: ",signalsTable)
    circuit(elementsTable, signalsTable)
    print("This is the signals table ", signalsTable)
    print("The result of the circuit: ",signalsTable[elementsTable[len(elementsTable)-1].output],"\n")


# ---------------------!!!!!!!!!!!!!!!!!!!------------------------------------------
# HERE THE PROGRAM STARTS, IN ORDER TO CHANGE THE GATES AND THE INPUT TABLE, GO TO DEMOFILE.TXT AND EDIT!!!
signalsSymbols = []
topInputs = []
topInputs,signalsSymbols,signalsTable,elementsTable=initializer("noinputs.txt",topInputs,signalsSymbols)
print("These are the signals SYMBOLS: ",signalsSymbols)
print("The input symbols have indexes: ",topInputs)
print("And our signals table: ", signalsTable)

# And our signals table:  [0, 0, 0, 0, 0, 0]
print("OUR ELEMENTS TABLE",elementsTable)
# We have: topInputs=[0,1,2]
# BE CAREFUL, in order to change signalsTable, check the LENGTH OF IT
#signalsTable=[1,1,0,1,0,1,0]
testbench(topInputs,signalsTable,elementsTable)
print("-----------------")
