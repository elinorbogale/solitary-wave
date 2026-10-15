

fittype(

% FIT TYPES
Y = a*exp(b*x) % exp1
Y = a*exp(b*x)+c*exp(d*x) % exp2
Y = a*x^b % power1
Y = a*x^b+c % power2


f = cell(11,1)
gof= cell(11,1)

for i = 1:11
    
    [f{i},gof{i}] = fit(X,Z1(:,i),'power2')
end

figure(6)

for i = 1:11
    hold on
    plot(f{i},X,Z1(:,i))
end
% legend typeset
leg = cell(11,1);
for i = 1:11
leg{i} = ['N=' num2str(i)]
end
xticks(X)
xlabel('$q$','Interpreter','latex')
ylabel('$K_{norm}$','Interpreter','latex')
title('$K_{norm} as a function of $q$','Interpreter','latex')
subtitle('$w$ = 0','Interpreter','latex')