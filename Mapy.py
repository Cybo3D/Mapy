import time

def Start():
    
    mode1 = input("Percentages: 1 \nTriangles: 2 \n> ")

    if mode1 == "1":
        mode =  input("Calculate percentage: 1 \ncalculate with percentages: 2 \nCalculate with percentage increase: 3 \nCalculate with percentage decrease: 4 \nCalculate percentage increase: 5 \nCalculate percentage decrease: 6 \nCalculate percentage degree for pie chart: 7 \n> ")

        if mode == "1":
            one =  input("how much > ")
            two =  input("total > ")
            roundNumber =  input("round > ")

            final = float(one)/float(two)
            print("answer is: " + str(round(final * 100, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()
        

        if mode == "2":
            one =  input("percent > ")
            two =  input("total > ")
            roundNumber =  input("round > ")

            oneDivided = float(one)/100
            final = oneDivided*float(two)
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

        if mode == "3":
            one = input("percent > ").replace(",", ".")
            two = input("Old number > ").replace(",", ".")
            roundNumber = input("round > ").replace(",", ".")

            oneDivided = float(one)/100
            final = float(two)+oneDivided*float(two)
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()
    
        if mode == "4":
            one = input("percent > ").replace(",", ".")
            two = input("Old number > ").replace(",", ".")
            roundNumber = input("round > ").replace(",", ".")

            oneDivided = float(one)/100
            final = float(two)-oneDivided*float(two)
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

        if mode == "5":
            one = input("increase > ").replace(",", ".")
            two = input("Old number > ").replace(",", ".")
            roundNumber = input("round > ").replace(",", ".")

            final = float(one)/float(two)*100
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

        if mode == "6":
            one = input("decrease > ").replace(",", ".")
            two = input("Old number > ").replace(",", ".")
            roundNumber = input("round > ").replace(",", ".")

            final = float(one)/float(two)*100
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

        if mode == "7":
            one = input("percentage > ").replace(",", ".")
            roundNumber = input("round > ").replace(",", ".")

            final = float(one)/100*360
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

    if mode1 == "2":

        mode =  input("triangle diagonal side: 1 \npiramid diagonal side: 2 \n> ")

        if mode == "1":
            one =  input("A > ")
            two =  input("B > ")
            roundNumber =  input("round > ")

            final = float(one)*float(one)+float(two)*float(two)
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()
        
        if mode == "2":
            one =  input("A > ")
            two =  input("B > ")
            three =  input("C > ")
            roundNumber =  input("round > ")

            final = float(one)*float(one)+float(two)*float(two)+float(three)*float(three)
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

    if mode1 == "3":
        mode =  input("gravity: 1 \npressure: 2 \n> ")

        if mode == "1":
            one =  input("mass > ")
            roundNumber =  input("round > ")

            final = float(one)*9.81
            print("answer is: " + str(round(final, int(roundNumber))) + "\n")
            time.sleep(2)
            Start()

Start()