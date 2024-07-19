#define _CRT_SECURE_NO_WARNINGS

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <float.h>

#include "glut.h"

// dimensiunea ferestrei in pixeli
#define dim 300
#define PI  3.14159

using namespace std;
unsigned char prevKey;

int pixel = 0;
double raza_cerc = 1;
int numarLinii = 15, numarColoane = 15;
int global_w, global_h;
int grosime = 1;

class GrilaCarteziana
{
    double nr_Linii, nr_Coloane;
public:
    void writePixel(int i, int j) {
        double radius = nr_Linii / 5;
        double centru_x = i * nr_Linii - 1;
        double centru_y = j * nr_Coloane - 1;
        int max_triangle = 20;

        glColor3f(0, 0, 0);
        glBegin(GL_TRIANGLE_FAN);

        glVertex2f(centru_x, centru_y);
        for (double i = 0; i <= max_triangle; i += 0.1f) {
            double x = centru_x + (radius * cos(i * 2 * PI / max_triangle));
            double y = centru_y + (radius * sin(i * 2 * PI / max_triangle));
            glVertex2f(x, y);
        }
        glEnd();
    }
    void init(double numarLinii, double numarColoane)
    {
        this->nr_Linii = 2 / numarLinii;
        this->nr_Coloane = 2 / numarColoane;

        glColor3f(0.5, 0.5, 0.5); //gri
        glBegin(GL_LINES);

        for (double i = -1; i <= 1; i = i + nr_Linii)
        {
            glVertex2d(i, 1);
            glVertex2d(i, -1);
        }
        for (double i = -1; i <= 1; i = i + nr_Coloane)
        {
            glVertex2d(-1, i);
            glVertex2d(1, i);
        }
        glEnd();

        if (pixel == 0) {
            writePixel(1, 1);
        }
    }
};
GrilaCarteziana gc;

void Init(void) {
    // specifica culoarea unui buffer dupa ce acesta
    // a fost sters utilizand functia glClear. Ultimul
    // argument reprezinta transparenta (1 - opacitate
    // completa, 0 - transparenta totala)
    glClearColor(1.0, 1.0, 1.0, 1.0);

    // grosimea liniilor
    glLineWidth(3);

    // dimensiunea punctelor
    glPointSize(4);

    // functia void glPolygonMode (GLenum face, GLenum mode)
    // controleaza modul de desenare al unui poligon
    // mode : GL_POINT (numai vf. primitivei) GL_LINE (numai
    //        muchiile) GL_FILL (poligonul plin)
    // face : tipul primitivei geometrice dpdv. al orientarii
    //        GL_FRONT - primitive orientate direct
    //        GL_BACK  - primitive orientate invers
    //        GL_FRONT_AND_BACK  - ambele tipuri
    glPolygonMode(GL_FRONT, GL_LINE);
}

void DisplayGrila() {
    glClear(GL_COLOR_BUFFER_BIT);
    gc.init(numarLinii, numarColoane);
    glFlush();
}

void printAbove(double x0, double y0, double x1, double y1, int buline) {
    int dy = y1 - y0;
    int dx = x1 - x0;
    int d = 2 * dy - dx;
    int dE = 2 * dy;
    int dNE = 2 * (dy - dx);
    int x = x0, y = y0;

    gc.writePixel(x, y);
    for (int i = 1; i <= buline/2; i++) {
        gc.writePixel(x, y - i);
        gc.writePixel(x, y + i);
    }

    while (x < x1)
    {
        if (d <= 0)
        {
            d += dE;
            x++;
        }
        else
        {
            d += dNE;
            x++;
            y++;
        }

        gc.writePixel(x, y);
        for (int i = 1; i <= buline/2; i++) {
            gc.writePixel(x, y - i);
            gc.writePixel(x, y + i);
        }
    }
}

void printBellow(double x0, double y0, double x1, double y1, int buline) {
    int dy = y1 - y0;
    int dx = x1 - x0;
    int d = 2 * dy - dx;
    int dE = 2 * dy;
    int dSE = 2 * (dy + dx);
    int x = x0, y = y0;

    gc.writePixel(x, y);
    for (int i = 1; i <= buline/2; i++) {
        gc.writePixel(x, y - i);
        gc.writePixel(x, y + i);
    }

    while (x < x1)
    {
        if (d >= 0)
        {
            d += dE;
            x++;
        }
        else
        {
            d += dSE;
            x++;
            y--;
        }

        gc.writePixel(x, y);
        for (int i = 1; i <= buline/2; i++) {
            gc.writePixel(x, y - i);
            gc.writePixel(x, y + i);
        }
    }
}

void AfisareSegmentDreapta3(double x0, double y0, double x1, double y1, int buline) {
    double m = (y1 - y0) / (x1 - x0);

    if (m > 0) {
        if (x0 > x1) {
            printAbove(x1, y1, x0, y0, buline);
        }
        else {
            printAbove(x0, y0, x1, y1, buline);
        }
    }
    else {
        if (x0 > x1) {
            printBellow(x1, y1, x0, y0, buline);
        }
        else {
            printBellow(x0, y0, x1, y1, buline);
        }
    }
}

void DisplayPixel() {
    int casuta1 = numarLinii + 1 - round(0.66 * numarLinii / 2);
    int casuta2 = numarLinii - round(numarLinii / 2);
    printf("casute: %d %d\n", casuta1, casuta2);

    AfisareSegmentDreapta3(0, numarLinii, numarLinii, casuta1, 3);
    AfisareSegmentDreapta3(0, 0, numarColoane, casuta2, 1);
}

void DisplayLines() {
    glColor3f(1, 0.1, 0.1); // rosu

    glBegin(GL_LINES);
    glVertex2f(-1, 1);
    glVertex2f(1, 0.33);
    glEnd();

    glBegin(GL_LINES);
    glVertex2f(-1, -1);
    glVertex2f(1, 0);
    glEnd();
}



void Display(void)
{
    switch (prevKey)
    {
    case '0':
        glClear(GL_COLOR_BUFFER_BIT);
        pixel = 1 - pixel;
        break;
    case '1':
        if (numarLinii > 1) {
            numarLinii--;
            numarColoane--;
        }
        DisplayGrila();
        break;
    case '2':
        numarLinii++;
        numarColoane++;
        DisplayGrila();
        break;
    case '3':
        glClear(GL_COLOR_BUFFER_BIT);
        pixel = 1;
        DisplayGrila();
        DisplayLines();
        DisplayPixel();
        break;
    default:
        break;
    }

    glFlush();
}

/*
   Parametrii w(latime) si h(inaltime) reprezinta noile
   dimensiuni ale ferestrei
*/
void Reshape(int w, int h) {
    printf("Call Reshape : latime = %d, inaltime = %d\n", w, h);

    // functia void glViewport (GLint x, GLint y,
    //                          GLsizei width, GLsizei height)
    // defineste poarta de afisare : acea suprafata dreptunghiulara
    // din fereastra de afisare folosita pentru vizualizare.
    // x, y sunt coordonatele pct. din stg. jos iar 
    // width si height sunt latimea si inaltimea in pixeli.
    // In cazul de mai jos poarta de afisare si fereastra coincid
    glViewport(0, 0, (GLsizei)w, (GLsizei)h);
}

/*
   Parametrul key indica codul tastei iar x, y pozitia
   cursorului de mouse
*/
void KeyboardFunc(unsigned char key, int x, int y) {
    printf("Ati tastat <%c>. Mouse-ul este in pozitia %d, %d.\n",
        key, x, y);
    // tasta apasata va fi utilizata in Display ptr.
    // afisarea unor imagini
    prevKey = key;
    if (key == 27) // escape
        exit(0);
    glutPostRedisplay();
}

/*
   Codul butonului poate fi :
   GLUT_LEFT_BUTTON, GLUT_MIDDLE_BUTTON, GLUT_RIGHT_BUTTON
   Parametrul state indica starea: "apasat" GLUT_DOWN sau
   "eliberat" GLUT_UP
   Parametrii x, y : coordonatele cursorului de mouse
*/
void MouseFunc(int button, int state, int x, int y) {
    printf("Call MouseFunc : ati %s butonul %s in pozitia %d %d\n",
        (state == GLUT_DOWN) ? "apasat" : "eliberat",
        (button == GLUT_LEFT_BUTTON) ?
        "stang" :
        ((button == GLUT_RIGHT_BUTTON) ? "drept" : "mijlociu"),
        x, y);
}

int main(int argc, char** argv) {
    // Initializarea bibliotecii GLUT. Argumentele argc
    // si argv sunt argumentele din linia de comanda si nu 
    // trebuie modificate inainte de apelul functiei 
    // void glutInit(int *argcp, char **argv)
    // Se recomanda ca apelul oricarei functii din biblioteca
    // GLUT sa se faca dupa apelul acestei functii.
    glutInit(&argc, argv);

    // Argumentele functiei
    // void glutInitWindowSize (int latime, int latime)
    // reprezinta latimea, respectiv inaltimea ferestrei
    // exprimate in pixeli. Valorile predefinite sunt 300, 300.
    glutInitWindowSize(dim, dim);

    // Argumentele functiei
    // void glutInitWindowPosition (int x, int y)
    // reprezinta coordonatele varfului din stanga sus
    // al ferestrei, exprimate in pixeli. 
    // Valorile predefinite sunt -1, -1.
    glutInitWindowPosition(100, 100);

    // Functia void glutInitDisplayMode (unsigned int mode)
    // seteaza modul initial de afisare. Acesta se obtine
    // printr-un SAU pe biti intre diverse masti de display
    // (constante ale bibliotecii GLUT) :
    // 1. GLUT_SINGLE : un singur buffer de imagine. Reprezinta
    //    optiunea implicita ptr. nr. de buffere de
    //    de imagine.
    // 2. GLUT_DOUBLE : 2 buffere de imagine.
    // 3. GLUT_RGB sau GLUT_RGBA : culorile vor fi afisate in
    //    modul RGB.
    // 4. GLUT_INDEX : modul indexat de selectare al culorii.
    // etc. (vezi specificatia bibliotecii GLUT)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    // Functia int glutCreateWindow (char *name)
    // creeaza o fereastra cu denumirea data de argumentul
    // name si intoarce un identificator de fereastra.
    glutCreateWindow(argv[0]);

    Init();

    // Functii callback : functii definite in program si 
    // inregistrate in sistem prin intermediul unor functii
    // GLUT. Ele sunt apelate de catre sistemul de operare
    // in functie de evenimentul aparut

    // Functia 
    // void glutReshapeFunc (void (*Reshape)(int width, int height))
    // inregistreaza functia callback Reshape care este apelata
    // oridecate ori fereastra de afisare isi modifica forma.
    glutReshapeFunc(Reshape);

    // Functia 
    // void glutKeyboardFunc (void (*KeyboardFunc)(unsigned char,int,int))
    // inregistreaza functia callback KeyboardFunc care este apelata
    // la actionarea unei taste.
    glutKeyboardFunc(KeyboardFunc);

    // Functia 
    // void glutMouseFunc (void (*MouseFunc)(int,int,int,int))
    // inregistreaza functia callback MouseFunc care este apelata
    // la apasarea sau la eliberarea unui buton al mouse-ului.
    glutMouseFunc(MouseFunc);

    // Functia 
    // void glutDisplayFunc (void (*Display)(void))
    // inregistreaza functia callback Display care este apelata
    // oridecate ori este necesara desenarea ferestrei: la 
    // initializare, la modificarea dimensiunilor ferestrei
    // sau la apelul functiei
    // void glutPostRedisplay (void).
    glutDisplayFunc(Display);

    // Functia void glutMainLoop() lanseaza bucla de procesare
    // a evenimentelor GLUT. Din bucla se poate iesi doar prin
    // inchiderea ferestrei aplicatiei. Aceasta functie trebuie
    // apelata cel mult o singura data in program. Functiile
    // callback trebuie inregistrate inainte de apelul acestei
    // functii.
    // Cand coada de evenimente este vida atunci este executata
    // functia callback IdleFunc inregistrata prin apelul functiei
    // void glutIdleFunc (void (*IdleFunc) (void))
    glutMainLoop();

    return 0;
}