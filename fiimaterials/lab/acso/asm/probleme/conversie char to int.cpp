#include <iostream>
using namespace std;

unsigned int convert(const char*) {
    _asm {
        mov eax, 0; // rezultat
        mov esi, [ebp + 8];
        mov ecx, 0; // contor

        push 10;
    _for:
        mov ebx, 0;
        mov bl, [esi + ecx];

        cmp ebx, 0;
        jz _out;
        inc ecx;

        sub ebx, '0';
        mul[esp];
        add eax, ebx;
        jmp _for;
    _out:
        add esp, 4;
    }
}

int main() {

    cout << convert("1204");

    return 0;
}