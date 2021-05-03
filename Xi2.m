function kvadratmetod = Xi2(X)
    load GivenValues theta sigma error eV
    Sum = 0;
    Intervall = [0, 50, 100];

    Z_t = 20;
    eps = 1e-6;
    f = @(r) r.^2.*(X(1)./(1 + exp((r - X(2))./ X(3))));
    Int = integral(f,0,inf);
    Condition = ((Z_t - 4 * pi * Int / eV) / eps)^2;
    E = 250e6*eV;
    for i = 1:(length(theta))
        Sum = Sum + ((Spr(E,theta(i),X)-sigma(i))/error(i))^2;
    end
       kvadratmetod = Sum+Condition
       X
end