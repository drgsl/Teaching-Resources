



#include <iostream>
using namespace std;

int fibo(int n)
{
    return n == 0 || n == 1 ? n : fibo(n-1) + fibo(n-2);
}

// int fibo(int n)
// {
//     if (n == 0 || n == 1)
//     {
//        return n;
//     } 
//     return fibo(n-1) + fibo(n-2);
// }



int main(int argc, char const *argv[])
{

    cout << fibo(8) << endl;

    return 0;
}






