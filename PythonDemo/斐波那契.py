def lib(n):
    if n==0 or n==1:
        return n
    else:
        return lib(n-1)+lib(n-2)
                    
