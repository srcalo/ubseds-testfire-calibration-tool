clear
% Load data from csv file, 1st column time, second column mV data
V = xlsread('05-07-22_Test_Fire_Data.csv','A107500:B111500');

% Use calibration data to create force v mV line 
%C = [966.796875-659.179788 1655.273438 2412.1-659.179688 3125-659.179688 3344.726562-659.179688; 4.214*9.81 (4.214+5.114)*9.81 (4.214+5.114+5.128)*9.81 (4.214+5.114+5.128+5.096)*9.81 (4.2114+5.114+5.128+5.096+1.222+1.172)*9.81]';
%[m,b] = calibrationLine(C);
m = 0.5177;
b = -310.9233;

% Convert data in mV to thrust in N
T(:,1) = V(:,2);
T(:,2) = (V(:,1).*m+b);%.*9.81;%+100 for ~6600Ns motor
T = downsample(T,100);
T(length(T),2) = 0;

figure
plot(T(:,1),T(:,2));
grid on
title('Thrust vs Time');
xlabel('Time (s)');
ylabel('Thrust (N)');

%% Calculate and plot Impulse
I = cumtrapz(T(:,1),T(:,2));

figure
plot(T(:,1),I);
grid on
title('Total Impulse vs Time');
xlabel('Time (s)');
ylabel('Total Impulse (N*s)');

%% Generate .eng file
p = 1;
while p == 1
    resp = input('Create .eng file? (y/n): ','s');
    if resp == 'y'
        fileName = [input('Input file name: ','s') ' '];
        motorCode = [input('Motor code: ','s') ' '];
        diam = [input('Casing diameter (mm): ','s') ' '];
        length = [input('Motor length (mm); ','s') ' '];
        delay = 'P ';
        propMass = [input('Propellant mass (kg): ','s') ' '];
        inWeight = [input('Total prop+casing weight (kg): ','s') ' '];
        manufacturer  = 'UBSEDS';
        
        header = [motorCode diam length delay propMass inWeight manufacturer];
        
        fileID = fopen(strcat(fileName,'.eng'),'w');
        fprintf(fileID,'%6s %12s\r\n',header);
        fprintf(fileID,'\r\n');
        fprintf(fileID,'%6.3f %4.8f\r\n',T');
        fclose(fileID);
        
        p = 0;
    else
        if resp == 'n'
            p = 0;
        end
    end
end