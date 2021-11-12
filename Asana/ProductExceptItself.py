 
# prefix and postfix
 
def productExceptSelf(nums):
    product = []
    prefix = [0] * len(nums)
    postfix = [0] *len(nums)
    prefixVal, postfixVal = 1,1
    for i in range(len(nums)):
        prefixVal *= nums[i] 
        prefix[i] = prefixVal
    for j in reversed(range(len(nums))):
        postfixVal *= nums[j]
        postfix[j] = postfixVal
        
    for k in range(len(nums)):
        if k == 0:
            pre = 1
            post = postfix[k+1]
        elif k == len(nums) - 1:
            pre = prefix[k-1]
            post = 1
        else:
            pre = prefix[k-1]
            post = postfix[k+1]
            
        product.append(pre*post)
        
    return product


def productExceptSelf2(nums):
    product = [1] * len(nums)
    pre = 1
    post = 1
    l = 0
    r = len(nums) - 1
    while l <= len(nums)-1 and r >= 0:
        product[l] *= pre
        product[r] *= post
        pre *= nums[l]
        post *= nums[r]

        l += 1
        r -= 1
    return product



print(productExceptSelf2([-1,1,0,-3,3]))



                