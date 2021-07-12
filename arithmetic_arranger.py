def arithmetic_arranger(problems, display = False):
    line1 = line2 = line3 = line4 =""
    space = "    "
    firstprob = True
    
    # test number of problems
    numop = len(problems)
    if numop > 5:
        return("Error: Too many problems.")
    
    for i in problems:
        z = i.split()
        
        # test numbers
        try:
            t1 = int(z[0])
            t2 = int(z[2])
        except:
            return("Error: Numbers must only contain digits.")
        
        l1 = len(z[0])
        l2 = len(z[2])
            
        if l1 > 4 or l2 > 4:
            return("Error: Numbers cannot be more than four digits.")
        else:
            if l1 > l2:
                l = l1
            else:
                l = l2
        
        if z[1] == "+" or z[1] == "-":
            try:
                if (z[1]) == "+":
                    e = int(z[0]) + int(z[2])
                else:
                    e = int(z[0]) - int(z[2])
            except:
                return("Error: Numbers must only contain digits.")
               
        else:
            return("Error: Operator must be '+' or '-'.")
        
        if firstprob == True:
            line1 += z[0].rjust( l + 2 )
            line2 += z[1] + z[2].rjust(l + 1)
            line3 += "-".rjust((l +2), "-")
            line4 += str(e).rjust((l + 2))
            firstprob = False
        else:
            line1 += z[0].rjust( l + 6)
            line2 += z[1].rjust(5) + " " + z[2].rjust(l)
            line3 += "    " + "-".rjust((l + 2), "-")
            line4 += "    " + str(e).rjust(l + 2)
            
    
    if display == True:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3
    return arranged_problems

