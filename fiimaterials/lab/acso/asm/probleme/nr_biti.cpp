
#include <iostream>
using namespace std;

int numberOfBits(int)
{
	_asm
	{
		mov eax, 0
		mov ebx, [ebp + 8]
		while1:
		cmp ebx, 0
			je stop_while
			inc eax
			shr ebx, 1
			jmp while1
			stop_While :
	}
}

int main()
{
	int x;
	cin >> x;
	int nrBits = numberOfBits(x);
	cout << nrBits;
	return 0;
}
