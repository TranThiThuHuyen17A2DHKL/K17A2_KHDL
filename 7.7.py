#cac loai tien:500000,200000,100000,50000
tien_muon_doi=1375000
so_to_1=tien_muon_doi//500000
tien_con_lai=tien_muon_doi%500000
so_to_2=tien_con_lai//200000
tien_con_lai=tien_muon_doi%200000
so_to_3=tien_con_lai//100000
tien_con_lai=tien_con_lai%100000
so_to_4=tien_con_lai//50000
tien_con_lai=tien_muon_doi%50000
print("so to 1: ",so_to_1)
print("so to 2:",so_to_2)
print("so to 3:",so_to_3)
print("so to 4:",so_to_4)
print("so tien con lai la: ",tien_con_lai)