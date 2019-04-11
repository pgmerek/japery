

clc
clear


m1 = xlsread('additional_data.xlsx',1);
m2 = xlsread('additional_data.xlsx',2);
m3 = xlsread('additional_data.xlsx',3);
m4 = xlsread('additional_data.xlsx',4);

% armature resistance and inductance
r = [m1(1,1) m2(1,1) m3(1,1) m4(1,1)];
l = [m1(1,2) m2(1,2) m3(1,2) m4(1,2)];

m = struct('rpm', {m1(:,4), m2(:,4), m3(:,4), m4(:,4)}, ...
           'emf', {m1(:,7), m2(:,7), m3(:,7), m4(:,7)});

scatter(m(1).rpm, m(1).emf,'filled','r','HandleVisibility','off');
hold on
scatter(m(2).rpm, m(2).emf,'filled','b','HandleVisibility','off');
scatter(m(3).rpm, m(3).emf,'filled','g','HandleVisibility','off');
scatter(m(4).rpm, m(4).emf,'filled','c','HandleVisibility','off');

%from Polulu datasheet
no_load_speed = 560;

motor_num = 4;
speed_fit = linspace(0,no_load_speed,100);
max_emf_fit = zeros(1,motor_num);
emf_speed_slope_fit = zeros(1,motor_num);
emf_fit = zeros(length(speed_fit),motor_num);
for i = 1:motor_num
    model = fitlm(m(i).rpm, m(i).emf);

    if table2array(model.Coefficients('x1','pValue')) < 0.05
        max_emf_fit(i) = table2array(model.Coefficients('(Intercept)','Estimate'));
        emf_speed_slope_fit(i) = table2array(model.Coefficients('x1','Estimate'));
        emf_fit(:,i) = max_emf_fit(i) + emf_speed_slope_fit(i) * speed_fit;
    end
end
plot(speed_fit,emf_fit(:,1),'r','LineWidth',1.5)
plot(speed_fit,emf_fit(:,2),'b','LineWidth',1.5)
plot(speed_fit,emf_fit(:,3),'g','LineWidth',1.5)
plot(speed_fit,emf_fit(:,4),'c','LineWidth',1.5)
xlabel('rpm','Interpreter','latex')
ylabel('back emf (V)','Interpreter','latex')
legend({'motor1','motor2','motor3','motor4'},'Interpreter','latex')

rpm_2_rad_per_sec = 2*pi/60;
Ke = emf_speed_slope_fit / rpm_2_rad_per_sec;
Ke_avg = sum(Ke) / length(Ke);
fprintf('EMF Coefficient (Ke = ke * Phi)\n');
fprintf('-------------------------------\n');
fprintf('m1: %.4f V.s/rad\n',Ke(1));
fprintf('m2: %.4f V.s/rad\n',Ke(2));
fprintf('m3: %.4f V.s/rad\n',Ke(3));
fprintf('m4: %.4f V.s/rad\n',Ke(4));
fprintf('avg: %.4f V.s/rad  (%.2f%% error)\n\n', Ke_avg, abs(Ke_avg-.2046)/.2046 * 100);

r_avg = sum(r) / length(r);
fprintf('Armature Resistance (Ra)\n');
fprintf('------------------------\n');
fprintf('m1: %.2f Ohms\n',r(1));
fprintf('m2: %.2f Ohms\n',r(2));
fprintf('m3: %.2f Ohms\n',r(3));
fprintf('m4: %.2f Ohms\n',r(4));
fprintf('avg: %.2f Ohms  (%.2f%% error)\n\n', r_avg, abs(r_avg-10.91)/10.91 * 100);

l_avg = sum(l) / length(l);
fprintf('Armature Inductance (La)\n');
fprintf('------------------------\n');
fprintf('m1: %.2f mH\n',l(1));
fprintf('m2: %.2f mH\n',l(2));
fprintf('m3: %.2f mH\n',l(3));
fprintf('m4: %.2f mH\n',l(4));
fprintf('avg: %.2f mH\n', l_avg);




