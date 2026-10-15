
%pre-allocate
ja = [1,11];
re = [6,11];
max = zeros(ja);
     halfmax = zeros(ja);
     halfwidth = zeros(ja);
     time = zeros(ja);
     MAX = zeros(re);
     HALFMAX = zeros(re);
     HALFWIDTH = zeros(re);
     TIME = zeros(re);

for k = [5,7,9,11,13,15]
   bb = num2str(k,'%02d');
    myfolder = fullfile(['/Users/derickbogale/Documents/MARCH-APRIL ELI/q' bb,'/w00_q' bb],'KE*.dat');
    list = dir(myfolder);
 
for i = 1:length(list)
    fileName = fullfile(list(i).folder,list(i).name);
    matrix = readtable(fileName);
    data = table2array(matrix);
    t = 1e-3*data(:,1);
    first = data(:,2);
    final = data(:,end);
     [pks,x,w,pr] = findpeaks(final,t,'NPeaks',1);
     max(i) = pks;
     halfmax(i) = 0.5*pks;
     halfwidth(i) = w;
     time(i) = x;
end
    m = (k-3)/2;
    MAX(m,:) = max;
    HALFMAX(m,:) = halfmax;
    HALFWIDTH(m,:) = halfwidth;
    TIME(m,:) = time;
end

k0 = 0.0011571533; % initial energy
X = [5;7;9;11;13;15];
Y = 10:1:20;
Z1 = MAX./k0;
Z2 = HALFWIDTH;
Z3 = HALFMAX/k0;
Z = Z3.';
zfitq2 =  Z1(:,2);
zfitn = Z1(1,:);

% curve-fitting



figure(2)
surf(X,Y,Z)
 xlabel('$q$','Interpreter','latex')
        ylabel('$N$','Interpreter','latex')
        %zlabel('$t$ (ms)','Interpreter','latex')
        zlabel('$K_{norm}$ ','Interpreter','latex')
        title('Half-Height as a function of $q$ and $N$','Interpreter','latex')
        subtitle('At w=0','Interpreter','latex','FontSize',8)
       xticks([5 7 9 11 13 15])


    % i ~ every grain N
    % k ~ every tapering q