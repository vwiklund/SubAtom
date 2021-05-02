function kvadratmetod = Xi2(X,data)
    theta=data(1,:)
    sigma = data(2,:)
    error = data(3,:)
    Sum = 0
    Intervall = [0, 50, 100]

    Z_t = 20
    eps = 1e-6
    f = @(r) r^2*(X(0) / (1 + exp((r - X(1)) / X(2))))
    Int = integral(f, Intervall(0), Intervall(1))
    Condition = ((Z_t - 4 * pi * Int / eps) / eps)^2

    for i = 1:(length(theta))
        Sum = Sum + ((spread(E,theta(x),X)-sigma(x))/error(x))^2
    end
       kvadratmetod = Sum+Condition
    
end