import random

def alivePerYear(ymin,ymax,lyst):
    count = {}  # setting up a dictionary to count the number of people alive in each year.
    for i in range(ymin, ymax+1):
        count[i] = 0  # initializing dictionary
    for item in lyst:
        for i in range(lyst.get(item)[0],lyst.get(item)[1]):
            count[i] += 1 #add up the number of people alive for a given year

    return count


def bestYear(count):      #after we have a list with all the years and the number of people alive during those
    (year, most) = count.popitem()   # years we find the year with the most people

    for i in range(len(count)):
        (temp_year, temp_most) = count.popitem()
        if temp_most > most:
            (year, most) = (temp_year, temp_most)


    return (year,most)



def main():
    ymin = 1900;
    ymax = 2000; #initializing year bounds

    lyst = {}
    for i in "abcdefghijklmnopqrstuvwxyz":   #creates random people named after the letters if the alphebet
        a = random.randint(1900, 2001)      #and the years they were born and died in
        b = random.randint(1900, 2001)
        if (a>b):                          # Choosing lesser of the years as birth year and greater as death year
            birthy = b
            deathy = a
        else:
            birthy = a
            deathy = b

        lyst[i] = (birthy,deathy) #adds name (i) and years lived to list


    count = alivePerYear(ymin,ymax,lyst)
    print(count)



    (year, most) = bestYear(count)
    print("The Most number of people lived in a year :") 
    print(most)
    
    print("The year when the most number of people lived :")
    print(year)

main()
