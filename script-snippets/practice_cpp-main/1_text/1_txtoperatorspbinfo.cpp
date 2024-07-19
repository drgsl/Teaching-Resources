// În C++ există mai multe modalități de a reprezenta șirurile de caractere.
// În acest articol vom discuta despre șirurile de caractere reprezentate ca tablouri unidimensionale cu elemente de tip char, reprezentare care provine din limbajul C.

// Aceste șiruri se mai numesc null-terminated byte string (NTBS).
// În reprezentarea internă, după ultimul caracter (byte, octet) valid din șir se află caracterul '\0' – caracterul cu codul ASCII 0, numit și caracter nul.

// Astfel, pentru reprezentarea în C/C++ a cuvântului copil, care are 5 caractere, se vor folosi 6 octeți, cu valorile: 'c', 'o', 'p', 'i', 'l', '\0'.

#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

int main()
{
    // Declararea unui șir de caractere
    char s[11]; // S-a declarat un șir care poate memora maxim 11 caractere, cu indici 0 1 ... 10.

    // De asemenea, la declararea unui șir acesta poate fi inițializat.
    char s1[11] = "copil";                       // se folosesc doar 6 caractere
    char t[] = "copil";                          // se aloca automat 6 octeti pentru sirul t: cele 5 litere si caracterul nul \0
    char x[6] = {'c', 'o', 'p', 'i', 'l', '\0'}; // initializarea este similara cu cea a unui tablou oarecare
    char z[] = {'c', 'o', 'p', 'i', 'l', '\0'};  // se aloca automat 6 octeti pentru sir

    // Afișarea unui șir de caractere
    cout << s1 << endl;

    // Citirea unui șir de caractere
    cout << "Introduceti un cuvant (fara spatii): ";
    // cin >> s;
    
    strcpy(s, "Tester String");
    

    // Citirea unui șir de caractere cu spații folosind getline
    char nume1[31], nume2[31];
    cout << "Cum te cheama? (nume, prenume) ";
    // cin.ignore(); // pentru a curata buffer-ul
    // cin.getline(nume1, 31);
    cout << "Cum il cheama pe prietenul tau? ";
    // cin.getline(nume2, 31);
    cout << "Te numesti " << nume1 << endl;
    cout << "Esti prieten cu " << nume2 << endl;

    // Referirea unui caracter din șir. Parcurgerea unui șir de caractere
    char s2[] = "abac";    // sirul consta din 5 caractere: cele 4 litere si caracterul nul '\0'
    cout << s2[3] << endl; // c
    s2[1] = 'r';
    cout << s2 << endl; // arac

    // Parcurgerea unui șir de caractere
    // cout << "Introduceti un alt cuvant (fara spatii): ";
    cin >> s;
    int i = 0;
    while (s[i] != '\0')
    {
        cout << s[i] << " ";
        i++;
    }
    cout << endl;

    // sau mai condensat:
    cout << "Introduceti un alt cuvant (fara spatii): ";
    // cin >> s;
    for (int i = 0; s[i]; i++)
        cout << s[i] << " ";
    cout << endl;

    // Tipul char *. Legătura dintre pointer-i și tablouri
    char *p, s3[31] = "pbinfo";
    cout << s3 << endl; // pbinfo
    p = s3;
    cout << p << endl; // pbinfo
    p++;
    cout << p << endl; // binfo

    // Funcții pentru caractere
    char ch = 'A';
    cout << "isalnum('A'): " << isalnum(ch) << endl;
    cout << "isalpha('A'): " << isalpha(ch) << endl;
    cout << "islower('A'): " << islower(ch) << endl;
    cout << "isupper('A'): " << isupper(ch) << endl;
    cout << "isdigit('1'): " << isdigit('1') << endl;
    cout << "tolower('A'): " << (char)tolower(ch) << endl;
    cout << "toupper('a'): " << (char)toupper('a') << endl;

    // Funcții pentru șiruri de caractere
    cout << "strlen(\"pbinfo\"): " << strlen("pbinfo") << endl;
    strcpy(s, "pbinfo");
    cout << s << endl; // pbinfo
    strcpy(s, t);
    cout << s << endl; // copil
    strncpy(s, "poveste", 3);
    cout << s << endl; // poveste

    char s4[21] = "pbinfo", t2[21] = "copil";
    strcat(s4, t2);
    cout << s4 << endl; // pbinfocopil

    char *p2 = strchr(s4, 'i');
    if (p2 != nullptr)
    {
        cout << p2 << endl; // inforcopil
    }

    char *p3 = strstr(s4, "info");
    if (p3 != nullptr)
    {
        cout << p3 << endl; // infocopil
    }

    if (strcmp(s, t2) < 0)
    {
        cout << "Da" << endl;
    }
    else
    {
        cout << "Nu" << endl;
    }

    // Extrage dintr-un sir de caractere câte un subșir (cuvânt) delimitat de caractere din șirul sep
    char sep[] = " .,";
    char s5[256] = "Ana are mere, pere si prune.";
    char *p4 = strtok(s5, sep);
    while (p4 != nullptr)
    {
        cout << p4 << endl;
        p4 = strtok(nullptr, sep);
    }

    // Eliminarea unui caracter dintr-un sir
    char s6[256] = "abcdefghjkl";
    int idx = 3; // eliminam caracterul de pe pozitia 3 (d)
    strcpy(t, s6 + idx + 1);
    strcpy(s6 + idx, t);
    cout << s6 << endl; // abcefghjkl

    // Inserarea unui caracter într-un sir
    char s7[256] = "abcdefghjkl";
    idx = 3; // inseram caracterul 'A' pe pozitia 3
    strcpy(t, s7 + idx);
    strcpy(s7 + idx + 1, t);
    s7[idx] = 'A';
    cout << s7 << endl; // abcAdefghjkl

    return 0;
}
