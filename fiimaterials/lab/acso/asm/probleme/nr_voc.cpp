#include<iostream>
using namespace std;
int nrVocale(char*, int)
{
	_asm
	{
		mov ebx, [ebp + 8];
		mov edi, [ebp + 12];
		mov ecx, 0;//i;
		mov esi, 0;//nr vocale
	for_:
		cmp ecx, edi;
		jge sfarsit;
		movzx eax, [ebx + ecx];
		mov edx, 'a';
		cmp eax, edx;
		je adev;

		mov edx, 'e';
		cmp eax, edx;
		je adev;

		mov edx, 'i';
		cmp eax, edx;
		je adev;

		mov edx, 'o';
		cmp eax, edx;
		je adev;

		mov edx, 'u';
		cmp eax, edx;
		je adev;

		inc ecx;
		jmp for_;

	adev:
		inc esi;
		inc ecx;
		jmp for_;
	sfarsit:
		mov eax, esi;
	}

}

int main()
{
	char c[] = "ana are mere";
	int nr = 12;
	int n;
	_asm
	{
		lea eax, c;
		mov ebx, nr;
		push ebx;
		push eax;
		call nrVocale;
		add esp, 8;
		mov n, eax;
	}
	cout << n;
	return 0;
}