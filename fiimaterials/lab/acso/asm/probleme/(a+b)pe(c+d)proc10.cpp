#include <iostream>

using namespace std;
//((a+b)/(c+d))%10
int main()
{
	int a, b, c, d, v, x = 10;
	cin >> a;
	cin >> b;
	cin >> c;
	cin >> d;

	_asm
	{
		mov eax, a
		add eax, b
		mov ecx, eax
		mov eax, c
		add eax, d
		mov v, eax
		mov eax, ecx
		mov edx, 0
		div v
		mov edx, 0
		div x
		mov v, edx
	}
	cout << v;

	return 0;
}