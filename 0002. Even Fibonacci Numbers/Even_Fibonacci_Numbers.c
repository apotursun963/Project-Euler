
int Even_Fibonacci_Numbers(void)
{
    int a = 1;
    int b = 2;
    int total = 0;

    while (a < 4000000)
    {
        if (a % 2 == 0)
            total += a;
        int tmp = b;
        b = a + b; 
        a = tmp;
    }
    return (total);
}
