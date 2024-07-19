#include <iostream>

using namespace std;
/*
Problema 1:
Creati o functie in ASM care este capabila sa faca suna a N parametri si s-o returneze.

Problema 2:
Creati o functie in ASM care este capabila sa faca suna a N parametri si s-o returneze.
Suma se va face dupa urmatorul algoritm:
	Fie x indicele parametrului curent
	Suma += p, daca x%2 == 0
	Suma -= p, daca x%2 == 1

	Unde p este parametrul curent (Px)
*/

int main()
{
	int a;

	_asm
	{
		push 3      // parametrul 5
		push 5      // parametrul 4
		push 7      // parametrul 3
		push 9      // parametrul 2
		push 4      // parametrul 1 - reprezinta nr de parametri la care trebuie sa facem suma
		call suma   // int suma(nr_parametri, param1, param2, param3 ...)
		add esp, 20 // 20 - 5 parametri * 4 bytes fiecare pe stiva

		jmp endall


		suma :
		push ebp
			mov ebp, esp // creez contexul curent de functie

			mov ecx, 0   // registru de indice, i
			mov eax, 0   // registru de suma
			mov edx, ebp // registru pt adresa parametrilor functiei
			add edx, 8   // facem registrul de adresa sa pointeze la primul parametru

			startfor:            // for(i=0, suma=0, edx=pointer la primul parametru; i<n; i++)
		mov ebx, [ebp + 8] // ebp+8 - nr. de variabile
			cmp ecx, ebx     // comparam i-ul cu nr total de variabile, n
			jae endfor       // daca i >= n, sarim la finalul functiei

			add edx, 4       // trecem la urmatoarea adresa de parametru
			mov ebx, [edx]   // luam parametrul curent de pe stiva
			add eax, ebx     // suma cu parametrul

			inc ecx          // i++
			jmp startfor     // salt la inceputul for-ului

			endfor :
		pop ebp          // incheiem socotelile cu functia - restabilim contextul vechi de functie
			ret              // sarim inapoi unde am facut call-ul

			endall :
		mov a, eax
	}
	cout << "Suma prob.1: " << a<<endl;


	_asm
	{
		push 9 // p5
		push 7 // p4
		push 5 // p3
		push 3 // p2
		push 4 // p1
		call suma2 // void suma(nr_var, v1, v2, v3, ...)
		add esp, 20
		mov a, eax

		jmp theend
		suma2 :
		push ebp
			mov ebp, esp

			mov eax, 0 // suma
			mov ebx, ebp
			add ebx, 8 // la adresa asta incep parametrii
			mov ecx, 0 // i = 0
			mov esi, 0

			startfor2:
		mov edx, [ebp + 8]
			cmp ecx, edx
			jae finfunc

			add ebx, 4
			mov edx, [ebx]

			xor esi, 1
			cmp esi, 1
			je myminus
			add eax, edx
			jmp dupaop
			myminus :
		sub eax, edx
			dupaop :
		inc ecx
			jmp startfor2

			finfunc :
		pop ebp
			ret

			theend :
	}

	cout << "Suma prob.2: " << a;

	return 0;
}
