#James Draney Project 8
#yerrrrr

def main():
    temperature=input("Enter Average Temperature Per Day Separated By Commas: ")
    temperature=temperature.split(",")
    heating=0
    cooling=0
    
    for i in temperature:
        if float(i)<60 or float(i)>80:
            heating+=(60-(float(i)))
        else:
            cooling+=((float(i))-80)

    print("The Number of Cooling Days is ", cooling, "The Number of Heating Days is", heating)

main()
        
    
