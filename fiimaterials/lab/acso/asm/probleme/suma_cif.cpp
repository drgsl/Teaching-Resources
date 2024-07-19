#include<iostream>
using namespace std;
int main()
{ // SUMA CIFRELOR UNUI NUMAR
	int n = 34349, s = 0;
	_asm { mov eax, n
	mov ecx, 10
		WHILE:
	mov edx, 0
		cmp eax, 0
		jbe FINISH
		div ecx
		add s, edx
		jmp WHILE

		FINISH :
	}
	cout << s;
	return 0;
	}