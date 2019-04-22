

clc
clear


m1 = xlsread('data.xlsx',1);
m2 = xlsread('data.xlsx',2);
m3 = xlsread('data.xlsx',3);
m4 = xlsread('data.xlsx',4);

m = struct('torque' , {m1(:,1),m2(:,1),m3(:,1),m4(:,1)}, ...
           'rpm'    , {m1(:,2),m2(:,2),m3(:,2),m4(:,2)}, ...
           'current', {m1(:,3),m2(:,3),m3(:,3),m4(:,3)});

% [torque_and_rpm, torque_and_current] 
corr_mat1 = corrcoef([m(1).torque m(1).rpm m(1).current]);
corr_mat2 = corrcoef([m(2).torque m(2).rpm m(2).current]);
corr_mat3 = corrcoef([m(3).torque m(3).rpm m(3).current]);
corr_mat4 = corrcoef([m(4).torque m(4).rpm m(4).current]);

fprintf('correlation coefficients\n');
fprintf('------------------------\n');
fprintf('m1: [%.4f  %.4f]\n', corr_mat1(1,2), corr_mat1(1,3));
fprintf('m2: [%.4f  %.4f]\n', corr_mat2(1,2), corr_mat2(1,3));
fprintf('m3: [%.4f  %.4f]\n', corr_mat3(1,2), corr_mat3(1,3));
fprintf('m4: [%.4f  %.4f]\n', corr_mat4(1,2), corr_mat4(1,3));
fprintf('\n');

scatter(m(1).torque,m(1).rpm,'filled','r','HandleVisibility','off');
hold on
scatter(m(2).torque,m(2).rpm,'filled','b','HandleVisibility','off');
scatter(m(3).torque,m(3).rpm,'filled','g','HandleVisibility','off');
scatter(m(4).torque,m(4).rpm,'filled','c','HandleVisibility','off');

oz_force_in_2_newton_mm = 7.061552;
% from Polulu datasheet
no_load_speed = 560;
no_load_current = 100;
stall_current = 1100;
stall_torque = 15 * oz_force_in_2_newton_mm;

motor_num = 4;
torque_fit = linspace(0,stall_torque,100);
no_load_speed_fit = zeros(1,motor_num);
speed_torque_slope_fit = zeros(1,motor_num);
speed_fit = zeros(length(torque_fit),motor_num);
for i = 1:motor_num
    model = fitlm(m(i).torque, m(i).rpm);

    if table2array(model.Coefficients('x1','pValue')) < 0.05
        no_load_speed_fit(i) = table2array(model.Coefficients('(Intercept)','Estimate'));
        speed_torque_slope_fit(i) = table2array(model.Coefficients('x1','Estimate'));
        speed_fit(:,i) = no_load_speed_fit(i) + speed_torque_slope_fit(i) * torque_fit;
    end
end
plot(torque_fit,speed_fit(:,1),'r','LineWidth',1.2)
hold on
plot(torque_fit,speed_fit(:,2),'b','LineWidth',1.2)
plot(torque_fit,speed_fit(:,3),'g','LineWidth',1.2)
plot(torque_fit,speed_fit(:,4),'c','LineWidth',1.2)
plot([0 stall_torque],[no_load_speed 0],'k--','LineWidth',1.2)
xlim([0 inf])
ylim([0 inf])
xlabel('torque (N.mm)','Interpreter','latex')
ylabel('rpm','Interpreter','latex')
legend({'motor1','motor2','motor3','motor4','theoretical'},'Interpreter','latex')


figure
scatter(m(1).torque,m(1).current,'filled','r','HandleVisibility','off');
hold on
scatter(m(2).torque,m(2).current,'filled','b','HandleVisibility','off');
scatter(m(3).torque,m(3).current,'filled','g','HandleVisibility','off');
scatter(m(4).torque,m(4).current,'filled','c','HandleVisibility','off');

no_load_current_fit = zeros(1,motor_num);
current_torque_slope_fit = zeros(1,motor_num);
current_fit = zeros(length(torque_fit),motor_num);
for i = 1:motor_num
    model = fitlm(m(i).torque, m(i).current);

    if table2array(model.Coefficients('x1','pValue')) < 0.05
        no_load_current_fit(i) = table2array(model.Coefficients('(Intercept)','Estimate'));
        current_torque_slope_fit(i) = table2array(model.Coefficients('x1','Estimate'));
        current_fit(:,i) = no_load_current_fit(i) + current_torque_slope_fit(i) * torque_fit;
    end
end
plot(torque_fit,current_fit(:,1),'r','LineWidth',1.2)
hold on
plot(torque_fit,current_fit(:,2),'b','LineWidth',1.2)
plot(torque_fit,current_fit(:,3),'g','LineWidth',1.2)
plot(torque_fit,current_fit(:,4),'c','LineWidth',1.2)
plot([0 stall_torque],[no_load_current stall_current],'k--','LineWidth',1.2)
xlim([0 inf])
ylim([0 inf])
xlabel('torque (N.mm)','Interpreter','latex')
ylabel('current (mA)','Interpreter','latex')
legend({'motor1','motor2','motor3','motor4','theoretical'},'Interpreter','latex')

Km = 1./current_torque_slope_fit;
Km_avg = sum(Km) / length(Km);
fprintf('Torque Coefficient (Km = km * Phi)\n');
fprintf('----------------------------------\n');
fprintf('m1: %.4f V.s\n',Km(1));
fprintf('m2: %.4f V.s\n',Km(2));
fprintf('m3: %.4f V.s\n',Km(3));
fprintf('m4: %.4f V.s\n',Km(4));
fprintf('avg: %.4f V.s  (%.2f%% error)\n', Km_avg, abs(Km_avg-.1059)/.1059 * 100);



