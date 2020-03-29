import argparse



class Subtraction:
    def get_mode():
        i=input('mode:>>>')
        l_mode=[]
        if '1' in i:
            l_mode.append('1')
        if '2' in i:
            l_mode.append('2')
        if '3' in i:
            l_mode.append('3')
        return l_mode

    def remove_char(num):
            num1,num2,num1c='','',False
            for i in range(len(num)):
                if not num[i]=='/':
                    if num1c:
                        num2+=num[i]
                    else:
                        num1+=num[i]
                else:
                    num1c=True
            return num1,num2
        
    def NWD(num,num_sec):
        l1=Subtraction.evaluation(num)
        l2=Subtraction.evaluation(num_sec)
        jl=[]
        if num>num_sec:
            for x in l2:
                if x in l1:
                    jl.append(x)
        else:
            for x in l1:
                if x in l2:
                    jl.append(x)
        c=1
        if num.endswith('0') or num_sec.endswith('0') and num.startswith('9') or num_sec.startswith('9'):
            if 9 in jl:
                jl.remove(9)
        for x in jl:
            if x>c:
                c=x
        return c
        
    def evaluation(num):
        num_list=[]
        num_list.append(1)
        for x in range(int(num)):
            if not x==0:
                num2=(int(num)/x)
                if Subtraction.len_num(num2)<=Subtraction.len_num(num):
                    if not (int(int(num)/x))in num_list:
                        num_list.append(int(int(num)/x))
        return Subtraction.sort(num_list)

    def sort(l1,reverse=False):
        l2=[]
        for y in l1:
            i=0
            if not len(l2)==0:
                for x in l2:
                    if y>x:
                        l2.insert(i,y)
                        break
                    i+=1
            else:
                l2.append(y)
        if not reverse:
            l2.reverse()
        return l2

    def len_num(num):
        lenght_num=0
        if '.' in str(num):
            counter=0
            for dig in str(num):
                if dig=='.':
                    num_dig=counter
                    break
                else:
                    counter+=1
            if list(str(num))[counter+1]=='0':
                num=int(num)
            else:
                num=list(str(num))
                num.remove('.')
                num=str(num).strip()
        for digit in str(num):
            lenght_num+=1
        return lenght_num

    def smallest(num1,num2):
        sub=Subtraction.NWD(num1,num2)
        fraction=[]
        fraction.append(int(int(num1)/sub))
        fraction.append(int(int(num2)/sub))
        return fraction

    def full(num1,num2):
        num2=int(num2)
        num1=int(num1)
        if num1%num2==0:
            return int(num1/num2),0,0
        for i in range(1,num2):
            if(num1-i)%num2==0:
                if Subtraction.len_num(num1-i/num2)==num1-1/num2:
                    return '%s %s/%s'%(num1-i/num2,i,num2)
        fraction=Subtraction.smallest(str(num1),str(num2))
        intiger=0
        if fraction[0]>fraction[1]:
            while True:
                if fraction[0]>fraction[1]:
                    intiger+=1
                    fraction[0]-=fraction[1]
                else:
                    break
        return intiger,fraction[0],fraction[1]
if __name__=='__main__':
    while True:
        num=input('>>>')
        num1,num2=Subtraction.remove_char(num)
        intiger,frc1,frc2=Subtraction.full(num1,num2)
        if intiger!=0 and frc1!=0 and frc2!=0:print('%s %s/%s'%(intiger,frc1,frc2))
        if intiger!=0 and frc1==0 and frc2==0:print(intiger)
        if intiger==0 and frc1!=0 and frc2!=0:print('%s/%s'%(frc1,frc2))
        print('\n\n\n')
