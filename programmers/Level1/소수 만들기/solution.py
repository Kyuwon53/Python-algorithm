def solution(nums):
    answer = 0
    primes = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                primes.append(nums[i]+nums[j]+nums[k])
    for prime in primes:
        if is_prime(prime):
            answer += 1
    return  answer

def is_prime(num):
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return False
    return True



print(solution([1,2,3,4]))
