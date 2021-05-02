clc,clear 
Z_t = 20
load GivenValues
 eps = 1e-6
 f = @(r) r.*(1./(1+exp((r-1)./1))).*sind(q(1).*r./hbar)
 Int = integral(f, 0, inf)
 %Condition = ((Z_t - 4 * pi * Int / eps) / eps)^2
    
