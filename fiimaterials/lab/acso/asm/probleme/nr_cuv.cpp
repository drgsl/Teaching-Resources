/*1. Sa se scrie în limbaj de asamblare o functie definita astfel:
int countCuvinte(char *sir);
Parametrul sir este un pointer catre un sir de caractere terminat prin '\0', care contine doar litere si spatii, iar între doua cuvinte consecutive exista exact un spatiu.
Functia va returna numarul de cuvinte din sirul de caractere indicat prin parametrul sir.
Exemplu:
-Apelul countCuvinte("Ana are mere") va returna 3.
- Apelul countCuvinte(" Am plecat la examen ") va returna 4.*/




#include <iostream>
#include <fstream>

int countCuvinte(char sir)
{
	char FinalPropozitie = '\0';
	char c = ' ';
	_asm
	{mov  ebx, [ebp + 8]
		mov edx, 0
		movzx ecx, c
		mov eax, 0
		_for:
	movzx esi, dword ptr[ebx + edx]
		cmp esi, '\0'
		je _final_for
		cmp esi, ecx
		jne _nu_numara
		inc eax
		inc edx
		jmp _for
		_nu_numara :
	inc edx
		jmp _for
		_final_for :


	}

}
using namespace std;
int main()
{
	char sir[50] = "Mihai merge la mare si Sorin la munte";
	int rezultat;
	_asm
	{lea ebx, sir
		push ebx
		call countCuvinte
		add esp, 4 * 1
		inc eax
		mov rezultat, eax
	}
	cout << rezultat;
}