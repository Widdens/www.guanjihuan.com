clc;clear all;clf;
s=100000;  %ȡ����Ʒ��
f=[1,2,3,3,3,3,6,5,4,3,2,1];  %�����õ���Ʒ�ķֲ�����
d=zeros(1,s);  %��ʼ״̬
x=1;
for i=1:s
     y=unidrnd(12);  %1��12�������
     alpha=min(1,f(y)/f(x)); %������
     u=rand;  
     if u<alpha   %��alpha�ĸ��ʽ���ת��
         x=y;
     end
     d(i)=x;
end
hist(d,1:1:12);