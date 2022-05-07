n = int(input())
div = int(input())

def FindSumOfRemainders(n, div):
    if  for(int i = 1; i <= n; ++i):
    {// Find all divisors of i and add them
        for(int j = 1; j * j <= i; ++j)
        {
            if (i % j == 0)
            {
                if (i / j == j)
                    sum += j;
                else
                    sum += j + i / j;
            }
        }
    }
    return sum;

 
# // Driver code
# int main()
# {
#     int n = 4;
#     cout << " " << divisorSum(n) << endl;
     
#     n = 5;
#     cout << " " << divisorSum(n);
     
#     return 0;
# }
    

result = FindSumOfRemainders(n, div)
print(result)