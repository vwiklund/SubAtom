function spread = Spr(E,theta,X)
    load physcon c hbar alpha m eV
    format long
    rho_ch0 = X(1);
    a = X(2);
    b = X(3);

    Zp=1;
    Zt=20;
    v=sqrt(c^2-(m/E)^2*c^6)
    beta=v/c
    gamma = 1/(sqrt(1-v^2/c^2))
    p=m*v*gamma;
    q=2*p*sind(theta/2)
    f= @(r) r.*(rho_ch0./(1+exp((r-a)/b))).*sind(q.*r./hbar);
    Int= integral(f,0,inf);
    F = 4*pi*hbar/(Zt*eV*q)*Int;
    spread = (Zp^2*Zt^2*alpha^2*(hbar*c)^2)/(4*beta^4*E^2*sind(theta/2)^4)*(1-beta^2*sind(theta/2)^2)*abs(F)^2;
end