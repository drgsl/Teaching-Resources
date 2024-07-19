// ASM_SUMA PRIMELOR N NUMERE PRIME.cpp : Defines the entry point for the console application.
//


#include<iostream>
using namespace std;


int main()
{
	unsigned int n, s = 0;
	cin >> n;
	_asm {
		mov ebx, n
		mov ecx, 2

		_while:
		cmp ecx, ebx
			jae _endwhile

			mov esi, 2
			mov edx, 1
			_while2 :
			cmp esi, ecx
			jae _endwhile2

			cmp edx, 0
			je _endwhile2

			mov eax, ecx
			mov edx, 0
			div esi
			inc esi
			jmp _while2

			_endwhile2 :
		cmp esi, ecx
			jb _end

			add s, ecx
			_end :
		inc ecx
			jmp _while

			_endwhile :
	}
	cout << "Suma primelor n numere prime: " << s << endl;
	return 0;
}

