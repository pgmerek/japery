% Justin Patterson
% reference: https://sites.google.com/a/asu.edu/s-taliro/s-taliro

clear


model = 'simple_pid';

init_cond = [];                              % n x 2 array

input_range = [0 1];                         % m x 2 array
cp_array = 1;                                % 1 x m array

% phi = '[](rise10 -> <>_[.8,.85] rise90)';
phi = '[](rise10 -> <>_[0,0.1] rise90)';     % formula to falisfy
                                             % MTL formula

i = 1;
preds(i).str = 'rise10';
preds(i).A = [-1 0.1];
preds(i).b = 0;
preds(i).loc = [];  

i = i + 1;
preds(i).str = 'rise90';
preds(i).A = [-1 0.9];
preds(i).b = 0; 
preds(i).loc = [];

time = 8;
opt = staliro_options();                    % default
opt.interpolationtype = {'const'};
% opt.optimization_solver = 'SA_Taliro';    % simulated annealing method
% opt.optimization_solver = 'CE_Taliro';    % cross entropy method
opt.optimization_solver = 'UR_Taliro';    % uniform random sampling
% opt.optimization_solver = 'GA_Taliro';    % genetic algorithim
opt.SimulinkSingleOutput = 1;
opt.optim_params.n_tests = 100;

tic
results = staliro(model,init_cond,input_range,cp_array,phi,preds,time,opt);
runtime = toc

results.run(results.optRobIndex).bestRob

% T  - vector with timestamps
% XT - state trajectory
% YT - output trajectory
% IT - has the form [t u1 u1 ... un], where t is the timestamp and the ui^th
%      vector is the i^th input
[T1,XT1,YT1,IT1] = SimSimulinkMdl(model,init_cond,input_range,cp_array,results.run(results.optRobIndex).bestSample(:,1),time,opt);

figure
subplot(2,1,1)
plot(IT1(:,1),IT1(:,2),'LineWidth',1.2)
title('Input','Interpreter','latex')
subplot(2,1,2)
plot(T1,YT1(:,1),'LineWidth',1.2)
title('Output','Interpreter','latex')   






