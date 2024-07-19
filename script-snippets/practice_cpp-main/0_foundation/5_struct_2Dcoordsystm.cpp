
#include <iostream>
using namespace std;

struct Point
{
    int x;
    int y;
};

struct Line
{
    Point start;
    Point end;
};

struct Rectangle
{
    Line top;
    Line right;
    Line bottom;
    Line left;
};

int main(int argc, char const *argv[])
{

    Point A = { 1,  1};
    Point B = {-1,  1};
    Point C = {-1, -1};
    Point D = { 1, -1};

    cout << "A: " << A.x << ", " << A.y << endl;
    cout << "B: " << B.x << ", " << B.y << endl;
    cout << "C: " << C.x << ", " << C.y << endl;
    cout << "D: " << D.x << ", " << D.y << endl;


    Line AB = {A, B};
    Line BC = {B, C};
    Line CD = {C, D};
    Line DA = {D, A};

    cout << "AB: " << AB.start.x << ", " << AB.start.y << " -> " << AB.end.x << ", " << AB.end.y << endl;


    Rectangle rect;
    rect.top = AB;
    rect.right = BC;
    rect.bottom = CD;
    rect.left = DA;

    cout << "Top: " << rect.top.start.x << ", " << rect.top.start.y << " -> " << rect.top.end.x << ", " << rect.top.end.y << endl;

    return 0;
}




