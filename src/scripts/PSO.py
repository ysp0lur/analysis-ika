import sys
import random
import json

n = int(sys.argv[1])
e = int(sys.argv[2])
w = sys.argv[3]
c1 = sys.argv[4]
c2 = sys.argv[5]
c3 = sys.argv[6]
c4 = sys.argv[7]
c5 = sys.argv[8]
c6 = sys.argv[9]
c7 = sys.argv[10]
c8 = sys.argv[11]
c9 = sys.argv[12]
CC = int(sys.argv[13])
RR = sys.argv[14]

def calculateRandom(n,e,w,c1,c2,c3,c4,c5,c6,c7,c8,c9,CC,RR):
    #Parámetros de control (ingresan)
    # print()
    # print("###########################################")
    # print("Control parameters")
    # print("###########################################")
    # print()

    # print("Cantidad de partículas:")
    # print("     n=",n)

    # print("     e=",e)
    # print("     w=",w)
    # print("Cantidad de c y r:", CC)
    r1=[]
    r2=[]
    r3=[]
    r4=[]
    r5=[]
    r6=[]
    r7=[]
    r8=[]
    r9=[]
    if CC==2:
       
        # c1=0.2
        # c2=0.6
        c3=0
        c4=0
        c5=0
        c6=0
        c7=0
        c8=0
        c9=0

        # print("      c1=",c1)
        # print("      c2=",c2)
    # elif CC==9:
        
        # c1=0.1
        # c2=0.13
        # c3=0.1
        # c4=0.1
        # c5=0.18
        # c6=0.08
        # c7=0.15
        # c8=0.05
        # c9=0.11

        # print("      c1=",c1)
        # print("      c2=",c2)
        # print("      c3=",c3)
        # print("      c4=",c4)
        # print("      c5=",c5)
        # print("      c6=",c6)
        # print("      c7=",c7)
        # print("      c8=",c8)
        # print("      c9=",c9)
    # print("      RR=",RR)

    if (RR=="a"):
        # print("Son datos aleatorios")
        for i in range(n):
            aleatorio1=random.random()
            aleatorio3=random.random()

            if aleatorio1>1:
                aleatorio1=aleatorio1-0.2
            aleatorio2=f'{aleatorio1:.4f}'
                    
            if aleatorio3>1:
                aleatorio3=aleatorio3-0.2
            aleatorio4=f'{aleatorio3:.4f}'

            r1.append(float(aleatorio2))
            r2.append(float(aleatorio4))

            if(CC==9):
                aleatorio5=random.random()
                aleatorio7=random.random()
                aleatorio9=random.random()
                aleatorio11=random.random()
                aleatorio13=random.random()
                aleatorio15=random.random()
                aleatorio17=random.random()

                if aleatorio5>1:
                    aleatorio5=aleatorio5-0.2
                aleatorio6=f'{aleatorio5:.4f}'
                            
                if aleatorio7>1:
                    aleatorio7=aleatorio7-0.2
                aleatorio8=f'{aleatorio7:.4f}'       
                
                if aleatorio9>1:
                    aleatorio9=aleatorio9-0.2
                aleatorio10=f'{aleatorio9:.4f}'         
                
                if aleatorio11>1:
                    aleatorio11=aleatorio11-0.2
                aleatorio12=f'{aleatorio11:.4f}'

                if aleatorio13>1:
                    aleatorio13=aleatorio13-0.2
                aleatorio14=f'{aleatorio13:.4f}'

                if aleatorio15>1:
                    aleatorio15=aleatorio15-0.2
                aleatorio16=f'{aleatorio15:.4f}'
                
                if aleatorio17>1:
                    aleatorio17=aleatorio17-0.2
                aleatorio18=f'{aleatorio17:.4f}'

                r3.append(float(aleatorio6))
                r4.append(float(aleatorio8))
                r5.append(float(aleatorio10))
                r6.append(float(aleatorio12))
                r7.append(float(aleatorio14))
                r8.append(float(aleatorio16))
                r9.append(float(aleatorio18))

        # print("      r1",r1)
        # print("      r2",r2)
        # if(CC==9):
            # print("      r3",r3)
            # print("      r4",r4)
            # print("      r5",r5)
            # print("      r6",r6)
            # print("      r7",r7)
            # print("      r8",r8)
            # print("      r9",r9)

    if (RR=="b"):
        # print("Son datos fijos")
        if CC==2:
            if n==5:
                r1=[0.0479, 0.0467,0.0629, 0.0355, 0.0000]
                r2=[0.0827, 0.0830,0.0700, 0.0867, 0.1900]
            elif n==9:
                r1=[0.1969, 0.0741, 0.0489, 0.0311, 0.0570, 0.0400, 0.0407, 0.0448, 0.0526]
                r2=[0.0503, 0.1392, 0.1718, 0.1881, 0.1877, 0.1905, 0.1927, 0.1952, 0.1934]
            # print("      r1",r1)
            # print("      r2",r2)

        if CC==9:
            if n==5:
                r1=[0.0478, 0.0466, 0.0697, 0.0867, 0.1900]
                r2=[0.0526, 0.0521, 0.0663, 0.0812, 0.0577]  
                r3=[0.0572, 0.0571, 0.0663, 0.0765, 0.0224]
                r4=[0.0617, 0.0616, 0.0629, 0.0580, 0.0066]
                r5=[0.0660, 0.0661, 0.0697, 0.0853, 0.0038]
                r6=[0.0703, 0.0705, 0.0663, 0.0580, 0.0025]
                r7=[0.0745, 0.0748, 0.0663, 0.0471, 0.0018]
                r8=[0.0786, 0.0790, 0.0663, 0.0355, 0.0017]
                r9=[0.0826, 0.0829, 0.0663, 0.0505, 0.0000]
            elif n==9:
                # estos no me los proporcionarion:
                #Positivos
                r1=[0.1969, 0.0741, 0.0489, 0.0311, 0.0570, 0.0400, 0.0407, 0.0448, 0.0526]
                r2=[0.1561, 0.0941, 0.0606, 0.0362, 0.0338, 0.0841, 0.0384, 0.0154, 0.0364]
                r3=[0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0403, 0.0403, 0.0342, 0.0342]
                r4=[0.0347, 0.0358, 0.0525, 0.1730, 0.0766, 0.0414, 0.0538, 0.0556, 0.1027]
                
                #Negativos
                r5=[0.0503, 0.1392, 0.1718, 0.1881, 0.1877, 0.1905, 0.1927, 0.1952, 0.1934]
                r6=[0.0050, 0.0657, 0.1023, 0.1330, 0.1430, 0.0741, 0.1487, 0.1558, 0.1521]
                r7=[0.1969, 0.0741, 0.0489, 0.0311, 0.0570, 0.0400, 0.0407, 0.0448, 0.0526]
                r8=[0.0404, 0.0404, 0.0404, 0.0404, 0.0404, 0.0034, 0.0034, 0.0063, 0.0063]
                r9=[0.0347, 0.0358, 0.0525, 0.1730, 0.0766, 0.0414, 0.0538, 0.0556, 0.1027]
            # print("      r1",r1)
            # print("      r2",r2)
            # print("      r3",r3)
            # print("      r4",r4)
            # print("      r5",r5)
            # print("      r6",r6)
            # print("      r7",r7)
            # print("      r8",r8)
            # print("      r9",r9)

    # print("")
    # print("----")
    # print("Objetive Fuction: Ri= (t^-i)/ (t^+i+t^-i) , i=1,...,m")
    # ----------
    #inicialización del enjambre
    CP=[]
    V=[]
    CF=[]
    LBP=[]
    LBF=[]
    GBP=[]
    GBF=[]
    temp=[]
    temporal=[]

    # ----------
    # Inicialización de la partícula del enjambre
    # Iniciando cálculo de las iteraciones
    # ----------
    #Iteración #1
    # ----------

    # print()
    # print("-------------------------------------------")
    # print("Iteración # 1")
    # Inicialización de la velocidad
    for i in range(n):
        r21=float(r2[i])
        V.append(format(float(r21-0.5), '.4f'))
    #print("V  =",V)

    for i in range(n):
        r11=float(r1[i])
        CP.append(format(float(10*(r11-0.5)), '.4f'))
    #print("CP =",CP)


    # Óptimo actual CF(1)

    for i in range(n):
        # Ri= (t^-i)/ (t^+i+t^-i) , i=1,...,m
        # vector negativo / (vector positivo + vector negarivo)
        # R2/(R2+R1)
        CForm1=float(r1[i])
        CForm2=float(r2[i])
        CForm3=(float((CForm2)/(CForm2+CForm1)))
        CForm=(format(float(CForm3), '.4f'))
        CF.append(float(CForm))
    #print("CF =",CF)

    # mejor posición actual
    for i in range(n):
        # LBP[1]=CP[1]
        LBPP=format(float(CP[i]), '.4f')
        LBP.append(float(LBPP))
    #print("LBP=",LBP)

    # mejor óptimo local
    for i in range(n):
        # LBF[1]=CF[1]
        LBFF=format(float(CF[i]), '.4f')
        LBF.append(float(LBFF))
    #print("LBF=",LBF)

    # MEJOR ÓPTIMO GLOBAL
    GBF.append(max(LBF))
    GBFt=max(LBF)
    #print("GBF=", GBF)

    # MEJOR POSICION GLOBAL
    GBF_index=LBF.index(GBFt)
    GBPt=float(LBP[GBF_index])
    GBP.append(LBP[GBF_index])
    #print("GBP=",GBP)
    #print()

    ###########################################
    #  Iteráción 2 a la n
    ##########################################
    it=2
    e=e-2
    t=2
    tt=1

    while (e>=0):
        # print("--------")
        # print("Iteración #", it)
        long_V1=len(V)-n
        long_LBP1=len(LBP)-n
        long_CP1=len(CP)-n
        long_GBP1=len(GBP)-1

        if CC==2:
            for i in range(n):
            # V(i+1)= W*V(i) +c1*r1*(LBP(i)-CP(i))+c2*r2*(GBP)i)-CP(i))
                w2t=format(float(w), '.4f')
                v2t=format(float(V[long_V1]), '.4f')
                GBP2t=format(float(GBP[long_GBP1]), '.4f')
                LBP2t=format(float(LBP[long_LBP1]), '.4f')
                CP2t=format(float(CP[long_CP1]), '.4f')
                
                c12t=format(float(c1), '.4f')
                c22t=format(float(c2), '.4f')
                
                r12t=format(float(r1[i]), '.4f')
                r22t=format(float(r2[i]), '.4f')
                
                xx1=format(float(LBP2t)-float(CP2t), '.4f')
                xx2=format(float(GBP2t)-float(CP2t), '.4f')
                Vx=format((float(w2t)*float(v2t)+float(c12t)*float(r12t)*float(xx1)+float(c22t)*float(r22t)*float(xx2)), '.4f')
                V.append(Vx)
                #print("V",V)

                long_V1=long_V1+1
                long_LBP1=long_LBP1+1
                long_CP1=long_CP1+1

        elif CC==9:
            for i in range(n):
            # V(i+1)= W*V(i) +c1*r1*(LBP(i)-CP(i))+c2*r2*(GBP)i)-CP(i))++c3*r3*(GBP)i)-CP(i))
            #         +c4*r4*(GBP)i)-CP(i))+c5*r5*(GBP)i)-CP(i))+c6*r6*(GBP)i)-CP(i))
            #         +c7*r7*(GBP)i)-CP(i))+c8*r8*(GBP)i)-CP(i))+c9*r9*(GBP)i)-CP(i))
                w2t2=format(float(w), '.4f')
                v2t2=format(float(V[long_V1]), '.4f')
                LBP2t2=format(float(LBP[long_LBP1]), '.4f')
                CP2t2=format(float(CP[long_CP1]), '.4f')
                GBP2t2=format(float(GBP[long_GBP1]), '.4f')

                c12t2=format(float(c1), '.4f')
                c22t2=format(float(c2), '.4f')
                c32t2=format(float(c3), '.4f')
                c42t2=format(float(c4), '.4f')
                c52t2=format(float(c5), '.4f')
                c62t2=format(float(c6), '.4f')
                c72t2=format(float(c7), '.4f')
                c82t2=format(float(c8), '.4f')
                c92t2=format(float(c9), '.4f')
                
                r12t2=format(float(r1[i]), '.4f')
                r22t2=format(float(r2[i]), '.4f')
                r32t2=format(float(r3[i]), '.4f')
                r42t2=format(float(r4[i]), '.4f')
                r52t2=format(float(r5[i]), '.4f')
                r62t2=format(float(r6[i]), '.4f')
                r72t2=format(float(r7[i]), '.4f')
                r82t2=format(float(r8[i]), '.4f')
                r92t2=format(float(r9[i]), '.4f')
                
                xx02=format(float(w2t2)*float(v2t2), '.4f')
                xx12=format(float(LBP2t2)-float(CP2t2), '.4f')
                xx22=format(float(GBP2t2)-float(CP2t2), '.4f')

                xx32=format(float(c12t2)*float(r12t2), '.4f')
                xx42=format(float(c22t2)*float(r22t2), '.4f')
                xx52=format(float(c32t2)*float(r32t2), '.4f')
                xx62=format(float(c42t2)*float(r42t2), '.4f')
                xx72=format(float(c52t2)*float(r52t2), '.4f')
                xx82=format(float(c62t2)*float(r62t2), '.4f')
                xx92=format(float(c72t2)*float(r72t2), '.4f')
                xx102=format(float(c82t2)*float(r82t2), '.4f')
                xx112=format(float(c92t2)*float(r92t2), '.4f')

                xy12=format(float(xx32)*float(xx12), '.4f')
                xy22=format(float(xx42)*float(xx22), '.4f')
                xy32=format(float(xx52)*float(xx22), '.4f')
                xy42=format(float(xx62)*float(xx22), '.4f')
                xy52=format(float(xx72)*float(xx22), '.4f')
                xy62=format(float(xx82)*float(xx22), '.4f')
                xy72=format(float(xx92)*float(xx22), '.4f')
                xy82=format(float(xx102)*float(xx22), '.4f')
                xy92=format(float(xx112)*float(xx22), '.4f')  

                yy1=format(float(xx02)+float(xy12)+float(xy22), '.4f')  
                yy2=format(float(xy32)+float(xy42)+float(xy52), '.4f')  
                yy3=format(float(xy62)+float(xy72)+float(xy82)+float(xy92), '.4f')  

                Vxx=format(float(yy1)+float(yy2)+float(yy3), '.4f')

                Vx=format(float(Vxx), '.4f')
                V.append(Vx)
                #print("V",V)
                long_V1=long_V1+1
                long_LBP1=long_LBP1+1
                long_CP1=long_CP1+1
        long_V2=len(V)-n
        long_VV=len(V)
        long_CP2=len(CP)-n

        #CP=CP(i)+V(i)
        for i in range(n):
            CPI=(format(float(CP[long_CP2])+float(V[long_V2]), '.4f'))
            CP.append(float(CPI))
            if t==2:
                #mejor posición actual,en e tiempo 2
                LBP.append(float(CPI))
            #print("CP", CP)
            
            long_V2=long_V2+1
            long_CP2=long_CP2+1

        #óptimo actual CF
        long_CP1=len(CP)-(2*n)
        long_CP2=len(CP)-n

        for i in range(n):
            #CP2/(CP2+CP1)
            CF1=float(CP[long_CP1])
            CF2=float(CP[long_CP2])
            
            CF3=float(CF2+CF1)
            CF4=float(CF2/CF3)
            CF12=format(float(CF4),'.4f')
            CF.append(CF12)
            long_CP1=long_CP1+1
            long_CP2=long_CP2+1   
        #print("CF", CF)

        # mejor óptimo local
        long_CF2=len(CF)-n
        long_LBF1=len(LBF)-(n)
        for i in range(n):
            #Max( CF[i],LBF[i-1])
            CFt=float(CF[long_CF2])      
            LBFt=float(LBF[long_LBF1])

            if CFt>LBFt:
                LBF.append(CFt)
            else:
                LBF.append(LBFt)
            long_CF2=long_CF2+1
            long_LBF1=long_LBF1+1
        #print("LBF", LBF)


        # MEJOR ÓPTIMO GLOBAL
        long_LBF=len(CP)-n   # para sacar posición
        
        for i in range(n):
            temporal.append(float(LBF[long_LBF]))
            long_LBF=long_LBF+1
        GBF.append(max(temporal))
        GBFt=max(temporal)
        #print("GBF", GBF)

        # MEJOR POSICION GLOBAL
        long_CP2=len(CP)-n   # para sacar posición
        for i in range(n):
            #temporal.append(float(LBF[long_CP2]))
            tempora2=(float(LBF[long_CP2]))
            if GBFt==tempora2:
                #temporal3.append(float(CP[long_CP2]))
                GBP.append((float(CP[long_CP2])))
                GBPt=(float(CP[long_CP2]))
            else:
                long_CP2=long_CP2+1
        #GBP.append(max(temporal))
        #GBPt=max(temporal)

        # mejor posición actual  
        #print(GBPt)
        for l in range(n):
            column = []
            if t>2:
                for i in range(l, len(CP), n):
                    #print("CP",CP[i])
                    #print("i",i)
                    d=[]
                                    
                    if float(CP[i]) == float(GBPt):
                        #print("entre al primer IF")
                        d = float(CP[i])
                    elif float(GBPt)<0:
                        #print("entre al elif")
                        if float(CP[i])>float(GBPt):
                            #print("CP[i]>GBPt=")
                            d = float(CP[i])
                        else:
                            if i==0:
                                #print("CE[i]")
                                d = float(CP[i])
                                #print("[i]",i)
                            else:
                                ii=i-n
                                if float(CP[ii])>float(GBPt):
                                    #print("CP[ii]>GBPt")
                                    d = float(CP[ii])
                                    #print("[i]",ii)
                                else:
                                    #print("LBP")
                                    d = float(LBP[ii])
                                    #print("i",ii)
                    #print("d",d)    
                    column.append(d)
                    #print("colum", column)
                #print("CP_t",column)
                LBPMM=min(column)
                #print("LBPMM", LBPMM)
                LBP.append(LBPMM)
                temp.append(column)
                #print("GBPt",GBPt)
                #print("LBP",LBP)
                #print()
        t=t+1

    # impresión de datos por iteración
        V_imp = len(V)-n
        CP_imp = len(CP)-n
        CF_imp = len(CF)-n
        LBF_imp = len(LBF)-n
        LBP_imp = len(LBP)-n
        GBF_imp = len(GBF)-1
        GBP_imp = len(GBP)-1

        V_impT = []
        for i in range(n):
            V_impT.append(float(V[V_imp]))
            V_imp = V_imp+1
        # print("   V  =",V_impT)

        CP_impT = []
        for i in range(n):
            CP_impT.append(float(CP[CP_imp]))
            CP_imp = CP_imp+1
        # print("   CP =",CP_impT)

        CF_impT = []
        for i in range(n):
            CF_impT.append(float(CF[CF_imp]))
            CF_imp = CF_imp+1
        # print("   CF =",CF_impT)

        LBF_impT = []
        for i in range(n):
            LBF_impT.append(float(LBF[LBF_imp]))
            LBF_imp = LBF_imp+1
        # print("   LBF=",LBF_impT)

        LBP_impT = []
        for i in range(n):
            LBP_impT.append(float(LBP[LBP_imp]))
            LBP_imp = LBP_imp+1
        # print("   LBP=",LBP_impT)

        for i in range(n):
            GBF_impT = (float(GBF[GBF_imp]))
        # print("   GBF =",GBF_impT)

        for i in range(n):
            GBP_impT = (float(GBP[GBP_imp]))
        # print("   GBP =",GBP_impT)

        e = e-1
        it = it+1
        # print("")

    # print("*******************")
    GBF_SF = len(GBF)-1
    GBP_SF = len(GBP)-1

    GBF_FIN = (float(GBF[GBF_SF]))
    # print("   Mejor posición=",GBF_FIN)

    GBP_FIN = (float(GBP[GBP_SF]))
    # print("   Mejor óptimo=",GBP_FIN)
    # print("*******************")
    # print("")


    context = {
    "c1": c1,
    "c2": c2,
    "c3": c3,
    "c4": c4,
    "c5": c5,
    "c6": c6,
    "c7": c7,
    "c8": c8,
    "c9": c9,
    "w": w,
    "n": n,
    "e": e,

    "r1": r1,
    "r2": r2,
    "r3": r3,
    "r4": r4,
    "r5": r5,
    "r6": r6,
    "r7": r7,
    "r8": r8,
    "r9": r9,

    "V_impT": V_impT,
    "CP_impT": CP_impT,
    "CF_impT": CF_impT,
    "LBF_impT": LBF_impT,
    "LBP_impT": LBP_impT,
    "GBF_impT": GBF_impT,
    "GBP_impT": GBP_impT,

    "GBF_FIN": GBF_FIN,
    "GBP_FIN": GBP_FIN,
}

    # Retornamos lo que sea que necesite el front
    # return (GBF, GBP)
    # return (V_impT,CP_impT,CP,CF_impT, LBF_impT, LBP_impT,GBF, GBP, GBF_impT, GBP_impT, r1, r2, r3, r4, r5, r6, r7, r8, r9)
    my_result = ({
        'V': V_impT,
        'CP': CP_impT,
        'CP_A': CP,
        'CF': CF_impT,
        'LBF': LBF_impT,
        'LBP': LBP_impT,
        'GBF': GBF,
        'GBP': GBP,
        'bestPosition': GBF_impT,
        'bestOptimal': GBP_impT,
        'r1': r1,
        'r2': r2,
        'r3': r3,
        'r4': r4,
        'r5': r5,
        'r6': r6,
        'r7': r7,
        'r8': r8,
        'r9': r9,
    })
    json_dict = json.dumps(my_result)
    print(json_dict)

# # Start process
if __name__ == '__main__':
    calculateRandom(n,e,w,c1,c2,c3,c4,c5,c6,c7,c8,c9,CC,RR)
