clear; close all;

%% Script details for dummies (that's you!)
% This script takes calibration data and burn data from excel files and
% creates a thrust curve for use in OpenRocket/RockSim.

% Pre-Processing:
  % 1. Sift through calibration data file and find 5 or more data points with
  %    known loads and create a small table off to the side with these
  %    points. Edit the calibration xlsread line to pull the table's
  %    coordinates.
  % 2. Sift through burn data and remove unnecessary "0 load" data on
  %    either side of burn. Each data point is recorded a set time apart from
  %    each other (For our purposes, this was 1000Hz or 1 data point per ms).
  %  Input 0.001 next to the first data point you will use, 0.002 for the
  %    second, 0.003 for the third and then drag the bottom right corner of
  %    these cells to continue this trend to the end of your data.
  %  Edit the burn xlsread line to pull this set of points.
  % 3. You may need to edit the DryLoad to zero out the beginning of burn
  %    when no load is applied so as to not create erroneous total impulse,
  %    and mV_Range to porperly encapsulate your data.

%% Load Data From Calibration and Burn

    C = xlsread('5-07-22_Test_Fire_Calibration_2.csv','E5:F9');
        %Allocate mV reading to column 1 and calibration weight to column 2
        mV = C(:,1);
        N = C(:,2)*4.4482216153; %Multiplying by 4.448... to convert needed known weights from lbs to newtons
        
    Burn = xlsread('05-07-22_Test_Fire_Data.csv','A107500:B111500');
        %Burn = table2array(Burn_Table);
        %Allocate time to column 1 and thrust to column 2
        t = Burn(:,2);
        T_mV = Burn(:,1);
        %Remove Dry Mass
                    % For 98 load cell this drymass value is despicable and
                    % sent from hell
        %DryMass = T_mV(1);
        %T_mV = T_mV - DryMass;
        
%% Using Calibration data, create linear relationship between mV and N

F = polyfit(mV,N,1);
m = F(1);
b = F(2);
mV_Range = [0:10000];

figure(1)
scatter(mV,N)
hold on
fplot(@(mV_Range) mV_Range*m+b, [0,10000]);
title('Calibration Results')
xlabel('Load Cell Reading (mV)')
ylabel('Calibration Weight (N)')
hold off

%% Convert Burn data from mV to N
T_N = T_mV*m+b;

T_N = T_N - T_N(1);

figure(2)
plot(t,T_N);
grid on
title('Thrust vs Time');
xlabel('Time (s)');
ylabel('Thrust (N)');

eng = [t,T_N];

%% Calculate and plot Impulse
I = cumtrapz(t,T_N);

figure(3)
plot(t,I);
grid on
title('Total Impulse vs Time');
xlabel('Time (s)');
ylabel('Total Impulse (N*s)');

%% Calculate Specific Impulse
ueq = I(length(I),1)/0.18643;
Isp = ueq/9.81;

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
        fprintf(fileID,'%6.3f %4.8f\r\n',eng');
        fclose(fileID);
        
        p = 0;
    else
        if resp == 'n'
            p = 0;
        end
    end
end