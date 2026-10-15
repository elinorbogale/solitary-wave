
set(groot, 'defaultAxesTickLabelInterpreter','latex'); 
set(groot, 'defaultLegendInterpreter','latex');

fs = 10000000;      % sampling frequency (Hz)
T = 1/fs;           % sampling period (seconds)
N = 20000;          % length of signal
t = (0:N-1)*T;      % time vector (seconds_
w = fs*2*pi         % angular velocity
k = 0:N/2;          % length of k here is N/2+1 (starts at 0)
freq = (k*fs/N)*1e-6;   % (from musec -> seconds)
Y = fft(ke);        % ke = kinetic energy vector

% Calculate Symbolically (not complete - must create
% anonymous function/handle for integration callback
x = syms(ke)
f = (abs(x).^2).*exp(i.*2.*pi.*w.*t)
q = integral(f,b,a);
b = -1*1e6
a = 1e6



% ONE-SIDED FFT

Y = fft(ke);
k = 0:N/2;  % length of k here is N/2+1 (starts at 0)
freq = (k*fs/N)*1e-6; % cyclces per length of signal in seconds
% abs(Y(1:(N/2)+1));  positive, non-complex half

subplot(2,1,2)
stem(freq,abs(Y(1:(N/2)+1)))
title('One Sided Absolute Value of FFT of KE');
xlabel("Frequency (MHz)");


% Power Spectrum from FFT
power = (1/N^2)*abs(fft(ke)).^2; %2-sided
power = power(1:N/2+1); %one-sided
power(2:end-1) = 2*power(2:end-1); % exclude nyquist and DC
figure
plot(freq(1:N/2+1),pow2db(power),'LineWidth',3)
title('Power Spectrum using FFT')
ylabel('Power (dB)')
xlabel('Frequency (Hz)')

periodogram(ke,rectwin(length(ke)),length(ke),fs,'power') % short form

% Power Spectral Density
density = (1/(fs*N))*abs(fft(ke)).^2; %2-sided
density = density(1:N/2+1); %one-sided
density(2:end-1) = 2*density(2:end-1); % exclude nyquist and DC
figure
plot(freq(1:N/2+1),pow2db(density),'LineWidth',3)
title('Power Density using FFT')
ylabel('Power Density (dB)/Hz')
xlabel('Frequency (Hz)')

periodogram(ke,rectwin(length(ke)),length(ke),fs,'psd')

