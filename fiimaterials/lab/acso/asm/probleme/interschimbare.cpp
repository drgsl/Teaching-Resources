
#include <iostream>
using namespace std;


int main()
{
	int m[5];
	m[0] = 1;
	m[1] = 2;
	m[2] = 3;
	m[3] = 4;
	m[4] = 5;

	int n = 5, n1 = n - 1, jumn = n / 2; 
		_asm {
		mov eax, 0
		mov ebx, n1
		mov ecx, 0
		bucla:cmp eax, jumn
		jge afara
		mov ecx, m[eax * 4]
		mov edx, m[ebx * 4]
		mov m[eax * 4], edx
		mov m[ebx * 4], ecx
		inc eax
		dec ebx
		jmp bucla
		afara :

	}
	int i;
	for (i = 0; i < n; i++)
	{
		cout << m[i] << " ";
	}

}
