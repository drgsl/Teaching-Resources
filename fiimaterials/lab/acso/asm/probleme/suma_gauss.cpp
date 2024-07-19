

#include <iostream>


using namespace std;

int main()
{
    int n, suma;
    cin >> n;
    _asm {
        mov eax, 0;
        mov ecx, 1;
        mov ebx, n;
    bucla:
        cmp ecx, ebx;
        ja finali;
        add eax, ecx;
        inc ecx;
        jmp bucla;

    finali:
        mov suma, eax;
    }

    cout << suma;
    return 0;
}

