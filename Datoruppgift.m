clc,clear
load physcon
load GivenValues
data = [theta;sigma;error]

%sigmaNy = ones(1,31)*0.0000001
%tp(3,data,sigmaNy)

x0 = [0.25,-0.25];
x = fminsearch(@objectivefcn1,x0)