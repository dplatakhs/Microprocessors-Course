%%%
%%%
%%% τρέχετε το πρόγραμμα ως:
%%% signalprobs(input1sp,input2sp)
%%%
%%% Παραδείγματα:
%%% >> signalprobs(0.5,0.5)
%%% AND Gate for input probabilities (0.500000 0.500000):
%%% ans =  0.25000
%%% OR Gate for input probabilities (0.500000 0.500000):
%%% ans =  0.75000
%%% XOR Gate for input probabilities (0.500000 0.500000):
%%% NAND Gate for input probabilities (0.500000 0.500000):
%%% NOR Gate for input probabilities (0.500000 0.500000):
%%%
%%%
%%% >> signalprobs(0,0)
%%% AND Gate for input probabilities (0.00000 0.00000):
%%% ans =  0
%%% OR Gate for input probabilities (0.00000 0.00000):
%%% ans =  0
%%% XOR Gate for input probabilities (0.00000 0.00000):
%%% NAND Gate for input probabilities (0.00000 0.00000):
%%% NOR Gate for input probabilities (0.00000 0.00000):
%%%
%%% >> signalprobs(1,1)
%%% AND Gate for input probabilities (1.00000 1.00000):
%%% ans =  1
%%% OR Gate for input probabilities (1.00000 1.00000):
%%% ans =  1
%%% XOR Gate for input probabilities (1.00000 1.00000):
%%% NAND Gate for input probabilities (1.00000 1.00000):
%%% NOR Gate for input probabilities (1.00000 1.00000):
%%%
%%%
%%%
%%% Οι συναρτήσεις που υπολογίζουν τα signal probabilities 
%%% AND και OR πυλών δύο εισόδων έχουν ήδη υλοποιηθεί παρακάτω.
%%% Οι συναρτήσεις που υπολογίζουν τα signal probabilities 
%%% XOR, NAND και NOR πυλών δύο εισόδων είναι ημιτελής.
%%% (α) Σας ζητείτε να συμπληρώσετε τις υπόλοιπες ημιτελής συναρτήσεις για τον υπολογισμό
%%% των signal probabilities XOR,NAND και NOR 2 εισόδων πυλών.
%%% (β) γράψτε συναρτήσεις για τον υπολογισμό των signal probabilities 
%%% AND, OR, XOR, NAND, NOR πυλών 3 εισόδων
%%% (γ) γράψτε συναρτήσεις για τον υπολογισμό των signal probabilities 
%%% AND, OR, XOR, NAND, NOR πυλών Ν εισόδων


function s=signalprobs(varargin)
  argum=[];
  for i = 1:length (varargin)
    argum=[argum,varargin{i}];
  endfor

  if(length(varargin)==2)
    input1sp=varargin{1};
    input2sp=varargin{2};
    sp2AND(input1sp, input2sp)
    sp2OR(input1sp, input2sp)
    sp2XOR(input1sp, input2sp);
    sp2NAND(input1sp, input2sp);
    sp2NOR(input1sp, input2sp);
  elseif(length(varargin)==3)
    input1sp=varargin{1};
    input2sp=varargin{2};
    input3sp=varargin{3};
    sp3AND(input1sp, input2sp, input3sp);
    sp3OR(input1sp, input2sp, input3sp);
    sp3XOR(input1sp, input2sp, input3sp);
    sp3NAND(input1sp, input2sp, input3sp);
    sp3NOR(input1sp, input2sp, input3sp);
  elseif(length(varargin)>=4)
    AND(argum)
    NAND(argum)
    NOR(argum)
    OR(argum)
    XOR(argum)
  else
    printf("Not enough inputs!\n")
  endif    
end
function s=sp2AND(input1sp, input2sp)
  printf("AND Gate for input probabilities (%f %f):\n",input1sp,input2sp)
  s = input1sp*input2sp;
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
  endfunction
function s=sp2OR(input1sp, input2sp)
  printf("OR Gate for input probabilities (%f %f):\n",input1sp,input2sp)
  s = 1-(1-input1sp)*(1-input2sp); #OR = 1- NOR
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction
function s=sp2XOR(input1sp, input2sp)
  printf("XOR Gate for input probabilities (%f %f):\n",input1sp,input2sp)
  s = (1-input1sp)*input2sp + input1sp*(1-input2sp)
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp2NAND(input1sp, input2sp)
  printf("NAND Gate for input probabilities (%f %f):\n",input1sp,input2sp)
  s = 1-input1sp*input2sp #NAND = 1 - AND
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction
function s=sp2NOR(input1sp, input2sp)
  printf("NOR Gate for input probabilities (%f %f):\n",input1sp,input2sp)
  s = (1-input1sp)*(1-input2sp)
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp3AND(input1sp, input2sp, input3sp)
  printf("AND Gate for input probabilities (%f %f %f) :\n", input1sp, input2sp, input3sp)
  s = input1sp*input2sp*input3sp
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp3NAND(input1sp, input2sp, input3sp)
  printf("NAND Gate for input probabilities (%f %f %f) :\n", input1sp, input2sp, input3sp)
  s = 1 - input1sp*input2sp*input3sp #NAND = 1 - AND
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp3OR(input1sp, input2sp, input3sp)
  printf("OR Gate for input probabilities (%f %f %f) :\n", input1sp, input2sp, input3sp)
  s = 1 - (1-input1sp)*(1-input2sp)*(1-input3sp) #OR = 1 - NOR
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp3NOR(input1sp, input2sp, input3sp)
  printf("NOR Gate for input probabilities (%f %f %f) :\n", input1sp, input2sp, input3sp)
  s = (1-input1sp)*(1-input2sp)*(1-input3sp)
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp3XOR(input1sp, input2sp, input3sp)
  printf("XOR Gate for input probabilities (%f %f %f) :\n", input1sp, input2sp, input3sp)
  s = (1-input1sp)*(1-input2sp)*input3sp+(1-input1sp)*input2sp*(1-input3sp)+input1sp*(1-input2sp)*(1-input3sp)+ input1sp*input2sp*input3sp
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function AND(varargin)
  resAND=1;
  argumAND=[];
  for i = 1:length (varargin)
    argumAND=[argumAND,varargin{i}];
  endfor
  argumAND;
  for i = 1:length(argumAND)
    resAND*=argumAND(i);
  endfor
  printf("We have a AND gate with %d input probabilities: %d\n", length(argumAND),resAND);
  s=resAND;
  Esw = 2*s*(1-s);
  printf("Switching activity of AND: %d\n",Esw)
endfunction

function NAND(varargin)
  resAND=1;
  argumAND=[];
  for i = 1:length (varargin)
    argumAND=[argumAND,varargin{i}];
  endfor
  argumAND;
  for i = 1:length(argumAND)
    resAND*=argumAND(i);
  endfor
  resNAND=1-resAND;
  printf("We have a NAND gate with %d input probabilities: %d\n", length(argumAND),resNAND);
  s=resNAND;
  Esw = 2*s*(1-s);
  printf("Switching activity of NAND: %d\n",Esw)
endfunction

function NOR(varargin)
  resNOR=1;
  argumNOR=[];
  for i = 1:length (varargin)
    argumNOR=[argumNOR,varargin{i}];
  endfor
  for i = 1:length(argumNOR)
    resNOR*=1-argumNOR(i);
  endfor
  printf("We have a NOR gate with %d input probabilities: %d\n", length(argumNOR),resNOR);
  s=resNOR;
  Esw = 2*s*(1-s);
  printf("Switching activity of NOR: %d\n",Esw)
endfunction

function OR(varargin)
  resNOR=1;
  argumNOR=[];
  for i = 1:length (varargin)
    argumNOR=[argumNOR,varargin{i}];
  endfor
  for i = 1:length(argumNOR)
    resNOR*=1-argumNOR(i);
  endfor
  resOR=1-resNOR;
  printf("We have a OR gate with %d input probabilities: %d\n", length(argumNOR),resOR);
  s=resOR;
  Esw = 2*s*(1-s);
  printf("Switching activity of OR: %d\n",Esw)
endfunction

function XOR(varargin)
  res=0;
  resNOR=0;
  argumNOR=[];
  for i = 1:length (varargin)
    argumNOR=[argumNOR,varargin{i}];
  endfor
  resNOR=(1-argumNOR(1))*argumNOR(2)+(1-argumNOR(2))*argumNOR(1); #XOR ta prwta 2
  for i = 3:length(argumNOR)
    temp=resNOR;
    resNOR=temp*(1-argumNOR(i))+(1-temp)*argumNOR(i);    #h eksodos tou XOR 
  endfor                                                      #me to epomeno inp    
  resXOR=resNOR;
  printf("We have a XOR gate with %d input probabilities: %d\n", length(argumNOR),resXOR);
  s=resXOR;
  Esw = 2*s*(1-s);
  printf("Switching activity of XOR: %d\n",Esw)
endfunction