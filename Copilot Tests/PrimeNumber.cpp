// generate prime numbers up to 100 using the Sieve of Eratosthenes
#include <iostream>
using namespace std;
int main()
{
    int i, j;
    bool prime[100];
    for (i = 0; i < 100; i++)
        prime[i] = true;
    for (i = 2; i < 100; i++)
        if (prime[i])
            for (j = i; i*j < 100; j++)
                prime[i*j] = false;
    for (i = 2; i < 100; i++)
        if (prime[i])
            cout << i << " ";
    cout << endl;
    return 0;
}