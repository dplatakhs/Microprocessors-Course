function model(a,b,c,N,flag)
  %if flag==1 we use random workload
  
  clc
  printf("We initialized the output of the gates = 0\n")
  
  % parameters of AND model
  global saAND = 0;
  global lastAND = 0;
  % parameters of NOT model
  global saNOT = 0;
  global lastNOT = 0;
  % parameters of final model
  global sa = 0;
  global lastRES = 0;

  Workload=[];

  MonteCarloSize=N;
  for i = 1:MonteCarloSize
    Workload=[Workload; round(mod(rand(),2)), round(mod(rand(),2)), round(mod(rand(),2))];
  end
  
  % Remove " ; " if you want to see the workload
  Workload;
  if(flag == 1)
    for i = 1:MonteCarloSize
      circuit(Workload(i,1),Workload(i,2),Workload(i,3));
    endfor
    printf("----------------------------\n")
    printf("Switching activity of NOT gate:%d\n",saNOT)
    printf("Switching activity of AND gate:%d\n",saAND)
    printf("Switching activity of LAST gate:%d\n",sa)
    printf("The ratio is: %d\n",sa/N)
  else
    d=circuit(a,b,c);
    % Compute switching activity of AND GATE
    s1 = a*b;
    Esw1 = 2*s1*(1-s1);
    % Compute switching activity of NOT GATE
    s2=1-c;
    Esw2 = 2*s2*(1-s2);
    % Compute switching activity of LAST GATE
    s3 = a*b*(1-c);
    Esw3 = 2*s3*(1-s3);
    
    printf("Result of the Circuit: %d\n",d)
    printf("Switching activity of AND Gate: %d\n",Esw1)
    printf("Switching activity of NOT: %d\n",Esw2)
    printf("Switching activity of CIRCUIT: %d\n",Esw3)
  endif
  clear all;
endfunction

function d=circuit(a,b,c)
  % we initialize d=0 so it doesnt get printed
  d=0;
  % parameters of AND model
  global saAND;
  global lastAND;
  % parameters of NOT model
  global saNOT;
  global lastNOT;
  % parameters of final model
  global sa;
  global lastRES;
  % calling AND model 
  e = sp2AND(a,b);
  % calling NOT model
  f = sp1NOT(c);
  % end of the model
  d = sp2AND(e,f);

  % compute switching activity    
  if(e != lastAND)
    saAND=saAND+1;
  endif
  lastAND=e;
  if(f != lastNOT)
    saNOT=saNOT+1;
  endif
  lastNOT=f;
  if(d != lastRES)
    sa=sa+1;
    %printf("I changed from %d, to %d\n",lastRES,d);
  endif
  lastRES=d;
endfunction

function s=sp2AND(input1sp, input2sp)
  s = input1sp*input2sp;
  %Esw = 2*s*(1-s);
  %printf("Switching activity of AND: %d\n",Esw)
endfunction

function s=sp1NOT(input1sp)
  s=1-input1sp;
  %Esw = 2*s*(1-s);
  %printf("Switching activity of NOT: %d\n",Esw)
endfunction