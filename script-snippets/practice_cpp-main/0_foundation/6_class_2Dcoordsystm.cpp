

#include <iostream>
using namespace std;

class Point
{
public:
    int x;
    int y;

    // void print()
    // {
    //     cout << "x: " << x << ", y: " << y << endl;
    // }
private:
    int z;

    // void print()
    // {
    //     cout << "x: " << x << ", y: " << y << ", z: " << z << endl;
    // }    
};

class Line
{
public:
    Point start;
    Point end;
};

class Rectangle
{
public:
    Line top;
    Line right;
    Line bottom;
    Line left;
};

int main(int argc, char const *argv[])
{
    Point test;
    test.x = 1;
    test.y = 2;
    // test.z = 3; // error: 'int Point::z' is private within this context

    Point A;
    A.x = 1;
    A.y = 1;

    Point B;
    B.x = -1;
    B.y = 1;

    Point C;
    C.x = -1;
    C.y = -1;

    Point D;
    D.x = 1;
    D.y = -1;

    cout << "A: " << A.x << ", " << A.y << endl;
    cout << "B: " << B.x << ", " << B.y << endl;
    cout << "C: " << C.x << ", " << C.y << endl;
    cout << "D: " << D.x << ", " << D.y << endl;

}
