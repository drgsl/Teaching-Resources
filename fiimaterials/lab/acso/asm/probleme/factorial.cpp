#include <iostream>
#include <stdio.h>
#include <malloc.h>
#include <string.h>

using namespace std;

unsigned int factorial(unsigned int n)
{
	if (n == 0)
		return 1;
	return n * factorial(n - 1);
}

unsigned int fact(unsigned int)
{
	_asm
	{
		mov ebx, [ebp + 8]
		cmp ebx, 0
		jne continuare
		mov eax, 1
		jmp fine
		continuare :
		dec ebx
			push ebx
			call fact
			add	esp, 4
			mul dword ptr[ebp + 8]
			fine :


	}
}

int main()
{
	int n;
	cin >> n;
	cout << fact(n);

}