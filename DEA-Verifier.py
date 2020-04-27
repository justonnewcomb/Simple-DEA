#Verifying a DEA is time consuming math, but this program can do it lickity split! 

dea = input("What is the DEA in question? ").upper()
name = input("What is the perscribers last name? ").upper()

def verify(dea, name):

    #DEA's are verified by:
    #Second letter must be the first letter of the last name 
    if name[0] != dea[1]: 
        print("INVALID: initials incorrect")
        return
    
    else:
        nums = [] 
        for i in dea[2:]:
            nums.append(int(i)) 

        #add the 1st, 3rd, and 5th digits 
        first = nums[0] + nums[2] + nums[4]

        #add the 2nd, 4th, and 6th digits then multiply by two
        second = (nums[1]+nums[3]+nums[5])*2
        #add the two results, the last digit of the outcome should match the last digit of the DEA
        result = str(first+second)

        if int(result[-1]) == nums[6]:
            print("VALID")
            return 
        else:
            print("INVALID: numbers incorrect")
            return
            
verify(dea, name)

