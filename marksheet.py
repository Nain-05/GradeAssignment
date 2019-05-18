Std_Name=input('Student Name: ')
Fthr_Name=input('Father Name: ')
Std_Rollnum=int(input('Roll Number: '))
Group=input('Group: ')
Class_Name=input('Standard: ')
print('\n\t\t\tSUBJECT\t\t\tMARKS')
print('\t\t\t---------------------------------\n')
English_mrk=int(input('\t\t\tENGLISH\t\t|\t'))
Sindhi_mrk=int(input('\t\t\tSINDHI\t\t|\t'))
PakStd_mrk=int(input('\t\t\tPAKISTAN STUDIES|\t'))
Chem_mrk=int(input('\t\t\tCHEMISTRY\t|\t'))
Bio_mrk=int(input('\t\t\tBIOLOGY\t\t|\t'))
print('\t\t\t---------------------------------\n')
Total_Marks=English_mrk + Sindhi_mrk + PakStd_mrk + Chem_mrk + Bio_mrk;
Average=float(Total_Marks/425)*100
print('Total Marks ', Total_Marks)
print('Average  %.2f'%Average)
if Average >= 80:
    print("Grade 'A+'")
elif Average >=70 and Average <80:
    print("Grade 'A'")
elif Average >=60 and Average <70:
    print("Grade 'B'")
elif Average >=50 and Average <60:
    print("Grade 'C'")
elif Average >=40 and Average <40:
    print("Grade 'D'")
else:
    print("Grade 'Fail'")