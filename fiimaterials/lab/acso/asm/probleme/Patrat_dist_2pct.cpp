#include<iostream>
using namespace std;
struct punct
{
	int x;
	int y;
};
int distanta(punct*, punct*)
{
	_asm
	{
		mov esi, [ebp + 8];//A
		mov edi, [ebp + 12];//B

		mov ebx, [edi];//B.x
		sub ebx, [esi];//B.x-=A.x;
		mov eax, ebx;
		mul eax;
		mov ebx, eax;//ebx=(B.x-A.x)^2

		mov ecx, [edi + 4];//B.y;
		sub ecx, [esi + 4];//B.y-=A.y;
		mov eax, ecx;
		mul eax;
		mov ecx, eax;//ecx=(B.y-A.y)^2;

		mov eax, ebx;
		add eax, ecx;

	}
}
int main()
{
	punct A;
	punct B;
	A.x = 3; A.y = 4;
	B.x = 5; B.y = 20;
	int rezultat;
	_asm
	{
		lea eax, A;
		lea ebx, B;
		push ebx;
		push eax;
		call distanta;
		add esp, 8;
		mov rezultat, eax;
	}
	cout << rezultat;
	return 0;

}