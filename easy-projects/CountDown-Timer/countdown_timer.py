import time

#Function to that countdown to zero from given input

def countdown(t):
    says = input('Enter something to say after timer ends-->  20').upper()
    while t:
        mins, secs = divmod(t,60)
        timer =  "{:02d} : {:02d}".format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1


    print(f'{says}')

t = int(input("Enter time in seconds: "))

#Countdown timer-Function call
countdown(t)

