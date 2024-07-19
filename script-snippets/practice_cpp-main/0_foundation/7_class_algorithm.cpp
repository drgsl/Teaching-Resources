

#include <iostream>
using namespace std;


class Divisibility_Algorithm
{
    public:
        static bool devides(int a, int b)
        {
            return a % b == 0;
        }

        static bool isEven(int a)
        {
            return devides(a, 2);
        }

        static bool isOdd(int a)
        {
            return !isEven(a);
        }

        static int numberOfDivisors(int a)
        {
            int count = 0;
            for (int i = 1; i <= a; i++)
            {
                if (devides(a, i))
                {
                    count++;
                }
            }
            return count;
        }

        static bool isPrime(int a)
        {
            return numberOfDivisors(a) == 2;
        }
};


class Numerology_Algorithm
{
    public:

        static void swap(int &a, int &b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        static int Min(int a, int b)
        {
            return a < b ? a : b;
        }

        static int Max(int a, int b)
        {
            return a > b ? a : b;
        }

        static int Min(int a, int b, int c)
        {
            return Min(Min(a, b), c);
        }

        static int Max(int a, int b, int c)
        {
            return Max(Max(a, b), c);
        }

        static void NaiveSort(int arr[], int n)
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if(arr[i] < arr[j])
                    {
                        //this is ok, do nothing
                        continue;
                    }
                    if (arr[i] > arr[j])
                    {
                        swap(arr[i], arr[j]);
                    }
                }
            }
        }
};




int main(int argc, char const *argv[])
{

    cout << "devides(10, 1): " << Divisibility_Algorithm::devides(10, 1) << endl;
    cout << "devides(10, 2): " << Divisibility_Algorithm::devides(10, 2) << endl;

    cout << "isEven(10): " << Divisibility_Algorithm::isEven(10) << endl;
    cout << "isEven(11): " << Divisibility_Algorithm::isEven(11) << endl;

    cout << "isOdd(10): " << Divisibility_Algorithm::isOdd(10) << endl;
    cout << "isOdd(11): " << Divisibility_Algorithm::isOdd(11) << endl;

    cout << "numberOfDivisors(10): " << Divisibility_Algorithm::numberOfDivisors(10) << endl;
    cout << "numberOfDivisors(11): " << Divisibility_Algorithm::numberOfDivisors(11) << endl;

    cout << "isPrime(10): " << Divisibility_Algorithm::isPrime(10) << endl;
    cout << "isPrime(11): " << Divisibility_Algorithm::isPrime(11) << endl;

}



