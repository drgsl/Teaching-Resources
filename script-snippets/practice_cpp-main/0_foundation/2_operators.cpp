


#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a = 10;
    int b = 20;

    // Arithmetic Operators
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    cout << "a / b = " << a / b << endl;
    cout << "a % b = " << a % b << endl;

    // Relational Operators
    cout << "a == b: " << (a == b) << endl;
    cout << "a != b: " << (a != b) << endl;
    cout << " a > b: " << (a > b)  << endl;
    cout << " a < b: " << (a < b)  << endl;
    cout << "a >= b: " << (a >= b) << endl;
    cout << "a <= b: " << (a <= b) << endl;

    // Logical Operators
    cout << "a && b: " << (a && b) << endl;
    cout << "a || b: " << (a || b) << endl;
    cout << "    !a: " <<       !a << endl;
    cout << "    !b: " <<       !b << endl;

    // Bitwise Operators
    cout << " a & b: " << (a & b) << endl;
    cout << " a | b: " << (a | b) << endl;
    cout << " a ^ b: " << (a ^ b) << endl;
    cout << "    ~a: " <<      ~a << endl;
    cout << "    ~b: " <<      ~b << endl;
    cout << "a << 1: " << (a << 1) << endl;
    cout << "b >> 1: " << (b >> 1) << endl;

    

    return 0;
}




