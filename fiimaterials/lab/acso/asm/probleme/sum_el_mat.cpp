#include<iostream>
using namespace std;
int sumaElemMatrice(int*, int)
{
	_asm
	{
		mov ebx, [ebp + 8];//matricea
		mov esi, [ebp + 12];//nr linii, nr coloane
		mov ecx, 0;//i
		mov edx, 0;//j
		mov edi, 0;//suma
	for_i:
		cmp ecx, [ebp + 12];//i<n
		je stop_for_i;
		mov edx, 0;
	for_j:
		cmp edx, [ebp + 12];//j<n
		je stop_for_j;

		//elementul A[i][j] se va afla la A + i * numarul de coloane * sizeof(int) + j * sizeof(int)
		push edx;
		mov eax, ecx;
		mul esi;//eax=ecx*esi;
		pop edx;
		add eax, edx;
		add edi, [ebx + eax * 4];
		inc edx;
		jmp for_j;

	stop_for_j:
		inc ecx;
		jmp for_i;

	stop_for_i:
		mov eax, edi;
	}
}
int main()
{
	int n = 3;
	int A[3][3] = { 1,0,2,0,1,0, 1,0,1 };
	int s;
	_asm
	{
		lea eax, A;
		mov ebx, n;
		push ebx;
		push eax;
		call sumaElemMatrice;
		add esp, 8;
		mov s, eax;
	}
	cout << s;
	return 0;


}