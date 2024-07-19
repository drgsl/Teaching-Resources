


#include <iostream>
using namespace std;


int main(int argc, char const *argv[])
{
    int a = 10;
    int b = 20;

    // Conditional Statements
    if (a > b)
    {
        cout << "a is greater than b" << endl;
    }
    else if (a == b)
    {
        cout << "a is equal to b" << endl;
    }
    else
    {
        cout << "b is greater than a" << endl;
    }


    // Switch Statement
    switch (a)
    {
    case 10:
        cout << "a is 10" << endl;
        break;
    case 20:
        cout << "a is 20" << endl;
        break;
    default:
        cout << "a is neither 10 nor 20" << endl;
        break;
    }

    // Looping Statements

    //// for loop
    for (int i = 0; i < 10; i++)
    {
        cout << i << " ";
    }
    cout << endl;

    //// while loop
    int i = 0;
    while (i < 10)
    {
        cout << i << " ";
        i++;
    }
    cout << endl;

    //// do-while loop
    i = 0;
    do
    {
        cout << i << " ";
        i++;
    } while (i < 10);
    cout << endl;

    //// break statement
    for (int i = 0; i < 10; i++)
    {
        if (i == 5)
        {
            break;
        }
        cout << i << " ";
    }
    cout << endl;

    //// continue statement
    for (int i = 0; i < 10; i++)
    {
        if (i == 5)
        {
            continue;
        }
        cout << i << " ";
    }
    cout << endl;

    //// goto statement
    i = 0;
    loop:
    cout << i << " ";
    i++;
    if (i < 10)
    {
        goto loop;
    }
    cout << endl;

    //// foreach loop
    int arr[] = {1, 2, 3, 4, 5};
    for (int i : arr)
    {
        cout << i << " ";
    }

    return 0;
}


