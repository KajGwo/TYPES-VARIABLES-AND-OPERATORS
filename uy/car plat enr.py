car_number = input('Enter car registration number: ')
if car_number[0:2] == "KR":
    iskr = True
elif car_number[0:2] == "KK":
    iskr = True
else:
    iskr = False


print('Car is from Krakow: ', iskr)