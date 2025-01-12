
int count_digits(int num)
{
    int counter = 0;

    while (num != 0)
    {
        counter++;
        num /= 10;
    }
    return (counter);
}

int ten_thousandth_fibo_number_index(void)
{
    int a = 1;
    int b = 1;
    int idx = 2;

    while (1)
    {
        int tmp = b;
        b = a + b;
        a = tmp;
        idx++;

        if (count_digits(b) == 1000)
            return (idx);
    }
}
