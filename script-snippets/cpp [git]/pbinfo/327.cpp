#include <iostream>
using namespace std; 

// input: n
// output: primele n numere (in ord cresc)

int main()
{
    int n;
    cin>>n;

    cout << n;

    for(int i = 1; i <= n; i++){
        cout << i << " ";
    }
    /*
    i = 1
    i <= 5 (A)
    cout << i;

    i++
    i = 2
    2 <= 5 (A)
    cout << 2;

    i = 3
    3 <=5 (A)
    cout << 3;

    i = 4
    4 <= 5 (A)
    cout << 4;

    i = 5
    5 <= 5 (A)
    cout << 5;

    i = 6
    6 <= 5 (F)
    */

    /*
    pentru fiecare numar in intervalul [1, n]:
        afiseaza numarul

    for (initiere ; conditie ; evolutie){
        // cod
    }

    */
    return 0;
}