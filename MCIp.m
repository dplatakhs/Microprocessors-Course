function MCIp(C)
  clc
  a = 1;
  counterIn = 0;
  counterOut = 0;
  %Ecyc = pi*0.25;
  %randi([-500 500])
  for i=1:C
    x1 = randi([-500 500]);
    x2 = randi([-500 500]);
    x1 = x1/1000;
    x2 = x2/1000;
    dis = sqrt(x1^2 + x2^2);
    if(dis<0.5)
      counterIn=counterIn+1;
    end
    counterOut=counterOut+1;
  end
  ratio = 4*(counterIn/counterOut);
  printf("This is the ratio of 4*(in/out): %d. If we increase C the ratio will get closer to pi\n",ratio)  
endfunction
