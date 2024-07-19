

#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a = 10;
    int b = 20;
    cout << a << ' ' << b << endl;
    cout << sizeof(a) << ' ' << sizeof(b) << endl;  // 4 bytes

    float c = 10.5;
    float d = 20.5;
    cout << c << ' ' << d << endl;
    cout << sizeof(c) << ' ' << sizeof(d) << endl;  // 4 bytes

    char e = 'A';
    char f = 'B';
    cout << e << ' ' << f << endl;
    cout << sizeof(e) << ' ' << sizeof(f) << endl;  // 1 byte

    bool g = true;
    bool h = false;
    cout << g << ' ' << h << endl;
    cout << sizeof(g) << ' ' << sizeof(h) << endl;  // 1 byte

    return 0;
}



