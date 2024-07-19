


#include <iostream>
#include <cstring>
using namespace std;



int main(int argc, char const *argv[])
{
    // Declararea unui șir de caractere
    char s[255] = "Tester String"; // S-a declarat un șir care poate memora maxim 11 caractere, cu indici 0 1 ... 10.
    
    cout << s << endl;
    cout << s[0] << endl;
    cout << s[5] << endl;
    cout << s[12] << endl;
    cout << s[13] << endl;
    cout << s[14] << endl;
    cout << s[300] << endl;

    // Operations on strings

    // strlen
    cout << "Lungimea sirului s este: " << strlen(s) << endl; 
    // 13

    // strcpy
    char s1[10];
    strcpy(s1, s);
    // char s1 = { 'T', 'e', 's', 't', 'e', 'r', '\0' };
    // s1 = "Tester";
    // s1 = s;
    cout << s1 << endl;

    // strcat
    char s2[255] = "String 2";
    strcat(s, s2);
    cout << s << endl;
    // Tester StringString 2

    // strcmp
    if (strcmp(s, s1) == 0)
        cout << "Sirurile sunt egale" << endl;
    else if (strcmp(s, s1) < 0)
        cout << "Sirul s este mai mic lexicografic" << endl;
    else
        cout << "Sirul s este mai mare lexicografic" << endl;

    // strchr
    if(strchr(s, 'S') != NULL)
        cout << "Caracterul a fost gasit" << endl;

    char *p = strchr(s, 'S');
    cout << p << endl;
    // String 2
    if (p != NULL)
        cout << "Caracterul a fost gasit" << endl;

    // strstr
    if(strstr(s, "String") != NULL)
        cout << "Substringul a fost gasit" << endl;

    p = strstr(s, "String");
    cout << p << endl;
    // StringString 2
    if (p != NULL)
        cout << "Substringul a fost gasit" << endl;

    // strrev
    cout << strrev(s) << endl;
    // 2 gnirtSgnirtseT

    // strupr
    cout << strupr(s) << endl;
    // 2 GNIRTSGNIRTSET

    // strlwr
    cout << strlwr(s) << endl;
    // 2 gnirtsgnirtset

    // strtok
    char s3[] = "A sentance with multiple words to be tokenized by strtok by spaces";
    char *token = strtok(s3, " ");
    while (token != NULL)
    {
        cout << token << endl;
        token = strtok(NULL, " ");
    }

    // strtok
    char s4[] = "A,sentance,with,multiple,words,to,be,tokenized,by,strtok,by,commas";
    token = strtok(s4, ",");
    while (token != NULL)
    {
        cout << token << endl;
        token = strtok(NULL, ",");
    } 

}


