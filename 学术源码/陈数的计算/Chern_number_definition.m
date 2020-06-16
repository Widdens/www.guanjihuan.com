%�������巨
clear;clc;
n=100;%�����ܶ�
delta=1e-9;%�󵼵�ƫ����
C=0; 
for kx=-pi:(1/n):pi
    for ky=-pi:(1/n):pi
        VV=get_vector(HH(kx,ky));
        Vkx=get_vector(HH(kx+delta,ky));%��ƫ��kx�Ĳ�����
        Vky=get_vector(HH(kx,ky+delta));%��ƫ��ky�Ĳ�����
        Vkxky=get_vector(HH(kx+delta,ky+delta));%��ƫ��kx��ky�Ĳ�����
        if  sum((abs(Vkx-VV)))>0.01   %Ϊ�˲������������ԣ�����Ĳ�����ֻ�����������⣬���Կ���ֱ����ô����
            Vkx=-Vkx;
        end
        
        if  sum((abs(Vky-VV)))>0.01
            Vky=-Vky;
        end
        
        if  sum(abs(Vkxky-VV))>0.01
            Vkxky=-Vkxky;
        end
        %�۴��Ĳ�������berry connection���󵼺��ڻ�
        Ax=VV'*(Vkx-VV)/delta;%Berry connection Ax
        Ay=VV'*(Vky-VV)/delta;%Berry connection Ay
        Ax_delta_ky=Vky'*(Vkxky-Vky)/delta;%��ƫ��ky��berry connection Ax
        Ay_delta_kx=Vkx'*(Vkxky-Vkx)/delta;%��ƫ��kx��berry connection Ay
        %berry curvature
        F=((Ay_delta_kx-Ay)-(Ax_delta_ky-Ax))/delta;
        %chern number
        C=C+F*(1/n)^2;  
    end
end
C=C/(2*pi*1i)

function vector_new = get_vector(H)
[vector,eigenvalue] = eig(H);
[eigenvalue, index]=sort(diag(eigenvalue), 'descend');
vector_new = vector(:, index(2));
end

function H=HH(kx,ky)
H(1,2)=2*cos(kx)-1i*2*cos(ky);
H(2,1)=2*cos(kx)+1i*2*cos(ky);
H(1,1)=-1+2*0.5*sin(kx)+2*0.5*sin(ky)+2*cos(kx+ky);
H(2,2)=-(-1+2*0.5*sin(kx)+2*0.5*sin(ky)+2*cos(kx+ky));
end