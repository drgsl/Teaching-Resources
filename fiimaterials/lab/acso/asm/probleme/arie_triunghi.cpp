
#include <iostream>
#include <cmath>
using namespace std;
struct triunghi {
	unsigned long a;
	unsigned long b;
	unsigned long c;
};
unsigned radical(unsigned long x)
{
	return unsigned(sqrt(x));
}
unsigned aria(triunghi *t)
{
	_asm {
		mov ebx, [ebp + 8]
		mov eax, [ebx]
		mov ecx, [ebx + 4]
		add eax, ecx
		mov ecx, [ebx + 8]
		add eax, ecx
		mov edi, 2
		mov edx,0
		div edi
		mov ecx, eax
		sub ecx, [ebx]
		mul ecx
		add ecx, [ebx]
		sub ecx, [ebx + 4]
		mul ecx
		add ecx, [ebx + 4]
		sub ecx, [ebx + 8]
		mul ecx
		push eax
		call radical
		pop ebx
	}
}
int main()
{
	triunghi t;
	unsigned long S;
	_asm {
		mov eax, 5
		mov ebx, 4
		mov ecx, 3
		lea edi,t
		mov [edi],eax
		mov [edi+4],ebx
		mov [edi+8],ecx
		push edi
		call aria
		add esp, 4
		mov S, eax
	}
	cout << S;
	return 0;
}