def is_palindrome(val):
    if str(val) == str(val)[::-1] :
        return True 
    return False

def find_pal_product():
    result = 0
    for i1 in range(100,1001):
        for i2 in range(100,1001):   
            if i2 < 100:
                continue
            prod = i1 * i2            
            if is_palindrome(prod) and prod > result:
                #Printing is just for curiousity
                print(f"{i1} * {i2} = {prod}")
                result = prod
    return result

if __name__ == "__main__":
    print(find_pal_product())
