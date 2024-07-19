
#include <iostream>

using namespace std;

bool voc(char)
{
	_asm {
		mov al, [ebp + 8]


		cmp al, 'a'
		je vocc

		cmp al, 'e'
		je vocc

		cmp al, 'i'
		je vocc

		cmp al, 'o'
		je vocc

		cmp al, 'u'
		je vocc

		jmp notvoc

		vocc :
		mov ecx, 1

			jmp endd

			notvoc :
		mov ecx, 0

			endd :

	}
}

int voccons(char*)
{
	_asm {
		mov ebx, [ebp + 8]
		mov esi, -1
		mov edi, 0
		mov edx, 0

		startfor:
		add esi, 1
			add edi, 1

			push[ebx + esi]

			call voc
			add esp, 4

			cmp ecx, 1
			je cond2

			cmp edi, [ebp + 12]
			je endd

			jmp startfor




		cond2:
		push[ebx + edi]
			call voc
			add esp, 4
			cmp ecx, 0
			je contor


			cmp edi, [ebp + 12]
			je endd

			jmp startfor


			contor :
		add edx, 1
			cmp edi, [ebp + 12]
			jb startfor

			mov ecx, edx

			endd :

		mov ecx, edx

	}
}

int main()
{
	char c[] = "acasa";
	int n = 4;
	int nr;

	_asm {
		push n
		lea eax, c
		push eax
		call voccons
		add esp, 8
		mov nr, ecx
	}

	cout << nr;
	return 0;

}