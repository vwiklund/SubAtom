clc,clear 
load GivenValues
E = 250e6*eV;
X = [0.000029875143678   0.529502469776266   0.046627573536436]
X = [0.000078293344768  -3.306180400910931   0.119456969368932]

for i = 1:length(theta)
sigmaNy(i) = Spr(E,theta(i),X);
end

tp(data,sigmaNy) %plottar
Xi2(X)
%%
x0 = [0.000029874610150,0.529504016706228,0.046630692085208];
x = fminsearch(@Xi2,x0)




