import sys
import json

e = int(sys.argv[1])
W = sys.argv[2]

def calculateADPSO(e,W):

    #Experimento AD-PSO

    # print()
    # print("-------------------------------------------")
    # print("Paso 1. Contrucción de la matriz de decisión" )
    A1=[float(0.048),float(0.047),float(0.070),float(0.087),float(0.190)]
    A2=[float(0.053),float(0.052),float(0.066),float(0.081),float(0.058)]
    A3=[float(0.057),float(0.057),float(0.066),float(0.076),float(0.022)]
    A4=[float(0.062),float(0.062),float(0.063),float(0.058),float(0.007)]
    A5=[float(0.066),float(0.066),float(0.070),float(0.085),float(0.004)]
    A6=[float(0.070),float(0.071),float(0.066),float(0.058),float(0.003)]
    A7=[float(0.075),float(0.075),float(0.066),float(0.047),float(0.002)]
    A8=[float(0.079),float(0.079),float(0.066),float(0.035),float(0.002)]
    A9=[float(0.083),float(0.083),float(0.066),float(0.051),float(0.000)]
    # print( A1)
    # print( A2)
    # print( A3)
    # print( A4)
    # print( A5)
    # print( A6)
    # print( A7)
    # print( A8)
    # print( A9)

    # print()
    # print("-------------------------------------------")
    # print("Paso 2. Estimar el grado de preferencia de los criterios")
    w=[float(0.100),float(0.130),float(0.120),float(0.100),float(0.100),float(0.110),float(0.110),float(0.120),float(0.110)]
    # print("w=",w)

    # print()
    # print("-------------------------------------------")
    # print("Paso 3. Establecer la solución ideal (S)")
    P1=format(float((A1[0]+A1[1]+A1[2]+A1[3]+A1[4])/5),'.3f')
    P2=format(float((A2[0]+A2[1]+A2[2]+A2[3]+A2[4])/5),'.3f')
    P3=format(float((A3[0]+A3[1]+A3[2]+A3[3]+A3[4])/5),'.3f')
    P4=format(float((A4[0]+A4[1]+A4[2]+A4[3]+A4[4])/5),'.3f')
    P5=format(float((A5[0]+A5[1]+A5[2]+A5[3]+A5[4])/5),'.3f')
    P6=format(float((A6[0]+A6[1]+A6[2]+A6[3]+A6[4])/5),'.3f')
    P7=format(float((A7[0]+A7[1]+A7[2]+A7[3]+A7[4])/5),'.3f')
    P8=format(float((A8[0]+A8[1]+A8[2]+A8[3]+A8[4])/5),'.3f')
    P9=format(float((A9[0]+A9[1]+A9[2]+A9[3]+A9[4])/5),'.3f')

    S=[float(P1),float(P2),float(P3),float(P4),float(P5),float(P6),float(P7),float(P8),float(P9)]
    # print("S=",S)

    # print()
    # print("-------------------------------------------")
    # print("Paso 4. Determinar el índice de similitud (IS)")
    N1=[]
    N2=[]
    N3=[]
    N4=[]
    N5=[]
    N6=[]
    N7=[]
    N8=[]
    N9=[]

    #a) normalizamos (a/S)
    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A1[i]/S[0]),'.3f')
        N1.append(float(ss))
    #print("N1",N1)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A2[i]/S[1]),'.3f')
        N2.append(float(ss))
    #print("N2=",N2)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A3[i]/S[2]),'.3f')
        N3.append(float(ss))
    #print("N3=",N3)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A4[i]/S[3]),'.3f')
        N4.append(float(ss))
    #print("N4=",N4)


    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A5[i]/S[4]),'.3f')
        N5.append(float(ss))
    #print("N5=",N5)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A6[i]/S[5]),'.3f')
        N6.append(float(ss))
    #print("N6=",N6)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A7[i]/S[6]),'.3f')
        N7.append(float(ss))
    #print("N7=",N7)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A8[i]/S[7]),'.3f')
        N8.append(float(ss))
    #print("N8=",N8)

    i=0
    for i in range(5):
        ss=0   
        ss=format(float(A9[i]/S[8]),'.3f')
        N9.append(float(ss))
    #print("N9=",N9)

    #b) elevar lo normalizado al peso(w)

    NN1=[]
    NN2=[]
    NN3=[]
    NN4=[]
    NN5=[]
    NN6=[]
    NN7=[]
    NN8=[]
    NN9=[]

    for i in range(5):
        ss=0   
        xx=pow(N1[i],w[0])
        ss=format(float(xx),'.3f')
        NN1.append(float(ss))
    #print(NN1)
    for i in range(5):
        ss=0   
        xx=pow(N2[i],w[1])
        ss=format(float(xx),'.3f')
        NN2.append(float(ss))
    #print(NN2)
    for i in range(5):
        ss=0   
        xx=pow(N3[i],w[2])
        ss=format(float(xx),'.3f')
        NN3.append(float(ss))
    #print(NN3)
    for i in range(5):
        ss=0   
        xx=pow(N4[i],w[3])
        ss=format(float(xx),'.3f')
        NN4.append(float(ss))
    #print(NN4)
    for i in range(5):
        ss=0   
        xx=pow(N5[i],w[4])
        ss=format(float(xx),'.3f')
        NN5.append(float(ss))
    #print(NN5)
    for i in range(5):
        ss=0   
        xx=pow(N6[i],w[5])
        ss=format(float(xx),'.3f')
        NN6.append(float(ss))
    #print(NN6)
    for i in range(5):
        ss=0   
        xx=pow(N7[i],w[6])
        ss=format(float(xx),'.3f')
        NN7.append(float(ss))
    #print(NN7)
    for i in range(5):
        ss=0   
        xx=pow(N8[i],w[7])
        ss=format(float(xx),'.3f')
        NN8.append(float(ss))
    #print(NN8)
    for i in range(5):
        ss=0   
        xx=pow(N9[i],w[8])
        ss=format(float(xx),'.3f')
        NN9.append(float(ss))
    #print(NN9)


    #Producto sucesivo

    qq1=float(NN1[0])*float(NN1[1])*float(NN1[2])*float(NN1[3])*float(NN1[4])
    qq2=float(NN2[0])*float(NN2[1])*float(NN2[2])*float(NN2[3])*float(NN2[4])
    qq3=float(NN3[0])*float(NN3[1])*float(NN3[2])*float(NN3[3])*float(NN3[4])
    qq4=float(NN4[0])*float(NN4[1])*float(NN4[2])*float(NN4[3])*float(NN4[4])
    qq5=float(NN5[0])*float(NN5[1])*float(NN5[2])*float(NN5[3])*float(NN5[4])
    qq6=float(NN6[0])*float(NN6[1])*float(NN6[2])*float(NN6[3])*float(NN6[4])
    qq7=float(NN7[0])*float(NN7[1])*float(NN7[2])*float(NN7[3])*float(NN7[4])
    qq8=float(NN8[0])*float(NN8[1])*float(NN8[2])*float(NN8[3])*float(NN8[4])
    qq9=float(NN9[0])*float(NN9[1])*float(NN9[2])*float(NN9[3])*float(NN9[4])


    qqq1=format(float(qq1),'.3f')
    qqq2=format(float(qq2),'.3f')
    qqq3=format(float(qq3),'.3f')
    qqq4=format(float(qq4),'.3f')
    qqq5=format(float(qq5),'.3f')
    qqq6=format(float(qq6),'.3f')
    qqq7=format(float(qq7),'.3f')
    qqq8=format(float(qq8),'.3f')
    qqq9=format(float(qq9),'.3f')
    PSS=[]
    PSS= [float(qqq1),float(qqq2),float(qqq3),float(qqq4),float(qqq5),float(qqq6),float(qqq7),float(qqq8),float(qqq9)]
    # print("PSS=",PSS)


    # print()
    # print("-------------------------------------------")
    # print("Paso 5. Establecer el ranking de las alternativas, en orden descendente.")
    PS=[0,0,0,0,0,0,0,0,0]
    Alt=[0,0,0,0,0,0,0,0,0]

    # Para el número mayor
    qqmax=float(max(PSS))
    qqinx=PSS.index(qqmax)
    qqtemp=0
    qqtemp=1+qqinx
    Alt[0]=qqtemp
    PS[0]= PSS[qqinx]

    # para el número menor
    qqmin=float(min(PSS))
    qqminx=PSS.index(qqmin)
    Alt[8]=qqminx
    qqtemp=0
    qqtemp=1+qqminx
    Alt[8]=qqtemp
    PS[8]= PSS[qqminx]

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8]):
            #Si el primero es diferente a Máximo
            temp1.append(PSS[i])        
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[1]=qqtemp
    PS[1]=max(temp1)

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8] and PSS[i]!=PS[1]):
            #Si el primero es diferente a Máximo
            temp1.append(PSS[i])        
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[2]=qqtemp
    PS[2]=max(temp1)

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8] and PSS[i]!=PS[1] and PSS[i]!=PS[2]):
            #Si el primero es diferente a Máximo
            temp1.append(PSS[i])        
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[3]=qqtemp
    PS[3]=max(temp1)

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8] and PSS[i]!=PS[1] and PSS[i]!=PS[2]):
            if (PSS[i]!=PS[3]):
                #Si el primero es diferente a Máximo
                temp1.append(PSS[i])        
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[4]=qqtemp
    PS[4]=max(temp1)

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8] and PSS[i]!=PS[1] and PSS[i]!=PS[2]):
            if (PSS[i]!=PS[3] and PSS[i]!=PS[4]):
                #Si el primero es diferente a Máximo
                temp1.append(PSS[i])        
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[5]=qqtemp
    PS[5]=max(temp1)

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8] and PSS[i]!=PS[1] and PSS[i]!=PS[2]):
            if (PSS[i]!=PS[3] and PSS[i]!=PS[4] and PSS[i]!=PS[5]):
                #Si el primero es diferente a Máximo
                temp1.append(PSS[i])   
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[6]=qqtemp
    PS[6]=max(temp1)

    temp1=[]
    for i in range(9):
        if(PSS[i]!=PSS[qqinx] and PSS[i]!=PS[0] and PSS[i]!=PS[8] and PSS[i]!=PS[1] and PSS[i]!=PS[2]):
            if (PSS[i]!=PS[3] and PSS[i]!=PS[4] and PSS[i]!=PS[5] and PSS[i]!=PS[6]):
                temp1.append(PSS[i])        
    temp1max=max(temp1)
    qqtemp=0
    qqtemp=PSS.index(temp1max)
    qqtemp=1+qqtemp
    Alt[7]=qqtemp
    PS[7]=max(temp1)

    #PS=[0.999,0.985,0.984,0.956,0.000]
    # print("Producto sucesivo=   ", PS)
    # print("Ranking_alternativas=",Alt)


    # #Parámetros de control (PSO)
    # print()
    # print("-------------------------------------------")
    # print("Paso 6. Inicialización de parámetros de control.")
    n=9
    w=W
    r1=[]
    r1=S
    r2=[]
    r2=PS
    c1=0.5
    c2=0.5
    # print("Cantidad de partículas:", n)
    # print("       w=",w)
    # print("      c1=",c1)
    # print("      c2=",c2)
    # print("      r1=",r1)
    # print("      r2=",r2)
    # print("Objetive Fuction: Ri= (t^-i)/ (t^+i+t^-i) , i=1,...,m")

    # e=int(input("¿Cuántas iteraciones deseas hacer?: "))
    #e=5
    # print("     e=",e)

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
    # print("Paso 7. Inicialización de posición y velocidad de las partículas")
    # print("Iteración #1")
    # Inicialización de la velocidad
    # print("n",n)
    for i in range(n):
        r21=float(r2[i])
        V.append(format(float(r21-0.5), '.3f'))
    # print("V  =",V)

    for i in range(n):
        r11=float(r1[i])
        CP.append(format(float(10*(r11-0.5)), '.3f'))
    # print("CP =",CP)

    # print()
    # print("-------------------------------------------")
    # print("Paso 8. Evaluar la función objetivo para obtener el mejor local y global.")
    # Óptimo actual CF(1)

    for i in range(n):
        # Ri= (t^-i)/ (t^+i+t^-i) , i=1,...,m
        # vector negativo / (vector positivo + vector negarivo)
        # R2/(R2+R1)
        CForm1=float(r1[i])
        CForm2=float(r2[i])
        CForm3=(float((CForm2)/(CForm2+CForm1)))
        CForm=(format(float(CForm3), '.3f'))
        CF.append(float(CForm))
    # print("CF =",CF)

    # print()
    # print("-------------------------------------------")
    # print("Paso 9. Actualizar la velocidad y posición de cada partícula.")
    # mejor posición actual
    for i in range(n):
        # LBP[1]=CP[1]
        LBPP=format(float(CP[i]), '.3f')
        LBP.append(float(LBPP))
    # print("LBP=",LBP)

    # mejor óptimo local
    for i in range(n):
        # LBF[1]=CF[1]
        LBFF=format(float(CF[i]), '.3f')
        LBF.append(float(LBFF))
    # print("LBF=",LBF)

    # print()
    # print("-------------------------------------------")
    # print("Paso 10. Obtener la mejor posición y el mejor óptimo.")
    # MEJOR ÓPTIMO GLOBAL
    GBF.append(max(LBF))
    GBFt=max(LBF)
    # print("GBF=", GBF)

    # MEJOR POSICION GLOBAL
    GBF_index=LBF.index(GBFt)
    GBPt=float(LBP[GBF_index])
    GBP.append(LBP[GBF_index])
    # print("GBP=",GBP)
    # print()

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

        for i in range(n):
        # V(i+1)= W*V(i) +c1*r1*(LBP(i)-CP(i))+c2*r2*(GBP)i)-CP(i))
            w2t=format(float(w), '.3f')
            v2t=format(float(V[long_V1]), '.3f')
            GBP2t=format(float(GBP[long_GBP1]), '.3f')
            LBP2t=format(float(LBP[long_LBP1]), '.3f')
            CP2t=format(float(CP[long_CP1]), '.3f')
            
            c12t=format(float(c1), '.3f')
            c22t=format(float(c2), '.3f')
            
            r12t=format(float(r1[i]), '.3f')
            r22t=format(float(r2[i]), '.3f')
            
            xx1=format(float(LBP2t)-float(CP2t), '.3f')
            xx2=format(float(GBP2t)-float(CP2t), '.3f')
            Vx=format((float(w2t)*float(v2t)+float(c12t)*float(r12t)*float(xx1)+float(c22t)*float(r22t)*float(xx2)), '.3f')
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
            CPI=(format(float(CP[long_CP2])+float(V[long_V2]), '.3f'))
            CP.append(float(CPI))
            if t==2:
                #
                #
                # mejor posición actual, en el tiempo 2
                #lbp=CP
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
            CF12=format(float(CF4),'.3f')
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
        Alt2=[]
        for i in range(n):
            LBF_impT.append(float(LBF[LBF_imp]))
            Alt2.append(float(LBF[LBF_imp]))
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


    #print("Alt2",Alt2)
    qqtemp=0
    qqtemp=Alt2.index(GBF_FIN)
    #print("qqtemp",qqtemp)
    qqtemp=1+qqtemp

    cadena="A"+repr(qqtemp)
    # print("   La mejor alternativa:",cadena)
    if cadena=="A1":print(A1)
    elif cadena=="A2":print(A2)
    elif cadena=="A3":print(A3)
    elif cadena=="A4":print(A4)
    elif cadena=="A5":print(A5)
    elif cadena=="A6":print(A6)
    elif cadena=="A7":print(A7)
    elif cadena=="A8":print(A8)
    elif cadena=="A9":print(A9)




    # print("*******************")
    # print("")

    context = {
        "c1": c1,
        "c2": c2,
        "w": w,
        "n": n,
        "e": e,

        "r1": r1,
        "r2": r2,

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
        'n': n
    })
    json_dict = json.dumps(my_result)
    print(json_dict)

# # Start process
if __name__ == '__main__':
    calculateADPSO(e, W)