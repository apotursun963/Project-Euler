
int Smallest_Multiple(void)
{
    int num = 0;
    int ctr = 0;

    while (1)
    {
        num++;
        for (int i=1; i <= 20; i++)
        {
            if (num % i == 0)
                ctr++;
            else
                ctr = 0;
        }
        if (ctr == 20)
            return (num); 
    }
}
