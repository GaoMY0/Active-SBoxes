from pysat.formula import CNF
from pysat.solvers import Cadical153
from C_constrain import *
from D_function import *
from SAT import *

def F(rounds,M):
    #创建模型
    m = CNF();start=[];num=1
    #创建变量

    X=[];Y=[];D=[]
    num=cre_v(X,Y,D,rounds,num)

    #差分传播
    L,S=f2(X,Y,rounds)

    f3(m, X, L,rounds)   # 线性传播
    f1(m, Y, S, rounds)  # 非线性传播

    # #标记活跃S盒子
    active(m,Y,S,D,rounds)
    #
    # # #统计活跃S盒子
    t=[]
    for r in range(rounds):
        for x in range(4):
            for z in range(32):
                t.append(D[r][x][z])
    num=less_count(m,num,start,t,M,1)

    # #保证一个活跃
    start.append(D[0][0][0])
    print("模型大小：",num)
    # #模型求解
    count=0
    while(1):
        with Cadical153(bootstrap_with=m.clauses) as l:
            if l.solve(assumptions=start) == True:

                result=l.get_model()
                result=[0]+result
                if len(result)<num:
                    for i in range(len(result),num+1):
                        result.append(i)
                printresult(result,X,L,Y,S,rounds,M)

                #排除已知的起点
                remove_start(m,result,S[0])
                count+=1
                print(count)
            else:
                print("模型无解")
                break