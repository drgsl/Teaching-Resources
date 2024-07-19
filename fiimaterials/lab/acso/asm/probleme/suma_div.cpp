

#include <iostream>
using namespace std;
int sumadivizori(int x)
{
	int suma;
	_asm
	{
		mov eax, 0
		mov suma, eax
		mov ecx, 1
		swhile:
		{
			cmp ecx, x
				jg fwhile

				mov edx, 0
				mov eax, x
				div ecx
				//edx:eax / ecx
				//eax - catul .. edx - restul
				cmp edx, 0
				jne aici
				mov edx, suma
				add edx, ecx
				mov suma, edx
				aici :

			inc ecx
				jmp swhile
		}
	fwhile:
	}

	return suma;
}
int main()
{
	int x;
	cin >> x;
	cout << sumadivizori(x);

	return 0;
}


