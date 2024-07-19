



#include <iostream>
using namespace std;

int a = 128; // even number
int b = 13; // prime number


int main(int argc, char const *argv[])
{
    // Parity Check
    if (a % 2 == 0)
    {
        cout << "a is even" << endl;
    }
    else
    {
        cout << "a is odd" << endl;
    }

    // Check all divisors of a
    for (int i = 1; i <= a; i++)
    {
        if (a % i == 0)
        {
            cout << i << " is a divisor of " << a << endl;
        }
    }

    // Check if a is prime
    int numberOfDivisors = 0;
    for (int i = 1; i <= a; i++)
    {
        if (a % i == 0)
        {
            numberOfDivisors++;
        }
    }
    if (numberOfDivisors == 2)
    {
        cout << a << " is a prime number" << endl;
    }
    else
    {
        cout << a << " is not a prime number" << endl;
    }

    // Check all divisors of b
    for (int i = 1; i <= b; i++)
    {
        if (b % i == 0)
        {
            cout << i << " is a divisor of " << b << endl;
        }
    }

    // Check if b is prime
    numberOfDivisors = 0;
    for (int i = 1; i <= b; i++)
    {
        if (b % i == 0)
        {
            numberOfDivisors++;
        }
    }
    if (numberOfDivisors == 2)
    {
        cout << b << " is a prime number" << endl;
    }
    else
    {
        cout << b << " is not a prime number" << endl;
    }


    return 0;
}





