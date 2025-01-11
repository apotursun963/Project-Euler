
int is_prime(int num)
{
    int i = 2;

    if (num <= 1)
        return (0);
    while (i * i <= num)
    {
        if (num % i == 0)
            return (0);
        i++;
    }
    return (1);
}

int Largest_Prime_Factor(void)
{
    int number = 13195;
    int max_prime = 0;

    for (int i=1; i < number; i++)
    {
        if (number % i == 0 && is_prime(i))
        {
            if (max_prime < i)
                max_prime = i;
        }
    }
    return (max_prime);
}
