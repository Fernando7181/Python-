file_size = float(input("Whats the size of the file in MB: "))
internet_speed = float(input("And what could it be the speed in Mbps: "))
print("The time that will take to download the file will be in seconds: "+ str((file_size / internet_speed) * 60) )
