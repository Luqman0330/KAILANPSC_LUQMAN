jenis_komponen = ["MPPF FORM 5x1000x900mm","CONTROL HORN","BRUSHLESS MOTOR","LINKAGE STOPPER","ESC (5W50A)","RECEIVER(LA10RX)","CARBON FIBER 300 mm","SERVO 9g","RC LIPO BATTERY","PROPELLER","FLYSKY-i6 REMOTE CONTROL"]
harga_komponen = [23,32,67,61,25.30,31,5.20,43,21,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10]

print("HARGA KOMPONEN=RM23,RM32,RM12,RM67,RM61,RM25.30,RM5.20,RM5.50,RM161")
a=int(input("Masukkan tempahan untuk komponen penghasilan MPPF FORM 5x1000x900mm:"))
b=int(input("Masukkan tempahan untuk komponen penghasilan CONTROL HORN"))
c=int(input("Masukkan tempahan untuk komponen penghasilan BRUSHLESS MOTOR"))
d=int(input("Masukkan tempahan untuk komponen penghasilan LINKAGE STOPPER"))
e=int(input("Masukkan tempahan untuk komponen penghasilan ESC (5W50A)"))
f=int(input("Masukkan tempahan untuk komponen penghasilan RECEIVER(LA10RX)"))
g=int(input("Masukkan tempahan untuk komponen penghasilan CARBON FIBER 300 mm"))
h=int(input("Masukkan tempahan untuk komponen penghasilan SERVO 9g"))
i=int(input("Masukkan tempahan untuk komponen penghasilanRC LIPO BATTERY"))
j=int(input("Masukkan tempahan untuk komponen penghasilan PROPELLER"))
k=int(input("Masukkan tempahan untuk komponen penghasilan FLYSKY-i6 REMOTE CONTROL"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,]

def jumlah_harga():
    for i in range (11) :
        jumlah [i] =harga_komponen[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"komponen",jenis_komponen[0])
    print(b,"komponen",jenis_komponen[1])
    print(c,"komponen",jenis_komponen[2])
    print(d,"komponen",jenis_komponen[3])
    print(e,"komponen",jenis_komponen[4])
    print(f,"komponen",jenis_komponen[5])
    print(g,"komponen",jenis_komponen[6])
    print(h,"komponen",jenis_komponen[7])
    print(i,"komponen",jenis_komponen[8])
    print(j,"komponen",jenis_komponen[9])
    print(k,"komponen",jenis_komponen[10])

    print("\n Jumlah harga untuk tempahan ialah RM",sum(jumlah))
jumlah_harga()
cetak() 
