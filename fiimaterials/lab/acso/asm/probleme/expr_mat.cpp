#include <iostream>
using namespace std;
//b * (a+c)/d + (a+b+c+d)%d
int main()
{
	int a, b, c, d, e = 0;
	cin >> a;
	cin >> b;
	cin >> c;
	cin >> d;
	_asm
	{
		mov eax, a
		add eax, c
		mul b
		mov edx, 0
		div d       //(a*b+b*c)/d
		mov ebx, eax
		mov eax, a
		add eax, b
		add eax, c
		add eax, d
		mov edx, 0
		div d
		add ebx, edx //(a*b+b*c)/d + (a+b+c+d)%d
		mov e, ebx
	}
	cout << e;
	return 0;
}