function test = tp(data,sigmaNy)
clf
load GivenValues
theta=data(1,:);
sigma = data(2,:);
error = data(3,:);

semilogy(theta,sigma,"x")
hold on

semilogy(theta,sigmaNy,"x")
end