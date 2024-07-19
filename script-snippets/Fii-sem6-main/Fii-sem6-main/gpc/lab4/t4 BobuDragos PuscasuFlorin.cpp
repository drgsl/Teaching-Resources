// Daca se doreste utilizarea bibliotecii GLUT trebuie
// inclus fisierul header GL/glut.h (acesta va include
// la GL/gl.h si GL/glu.h, fisierele header pentru
// utilizarea bibliotecii OpenGL). Functiile din biblioteca
// OpenGL sunt prefixate cu gl, cele din GLU cu glu si
// cele din GLUT cu glut.

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <GL/glut.h>
#include <vector>

using namespace std;

unsigned char prevKey;


/*
Design and implement a class CartesianGrid that draws a square 2D
Cartesian grid having the following features:
*/
class CartesianGrid{

public:
    int rows, cols;

    /*
    1.1 The number of rows/columns are parameters of the grid
    */
    CartesianGrid(int rows, int cols){
        this->rows = rows;
        this->cols = cols;
    }
    
    void draw(){
        // draw the grid
        glColor3f(0.0, 0.0, 0.0);
        glBegin(GL_LINES);
        for(int i = 0; i <= rows; i++){
            glVertex2f(-1.0, -1.0 + 2.0 * i / rows);
            glVertex2f(1.0, -1.0 + 2.0 * i / rows);
        }
        for(int i = 0; i <= cols; i++){
            glVertex2f(-1.0 + 2.0 * i / cols, -1.0);
            glVertex2f(-1.0 + 2.0 * i / cols, 1.0);
        }
        glEnd();
    }
    /*
    1.2. Pixels, having a circular shape (or other shapes - e.g.,
squared, should be painted at the grid vertices (a grid vertex is the
intersection between a row and a column),
    */
   void drawCircle(float cx, float cy, float r, int num_segments, bool isFilled = true) 
    { 
        if(isFilled)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        else
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

        glBegin(GL_POLYGON); 
        for(int ii = 0; ii < num_segments; ii++) 
        { 
            float theta = 2.0f * 3.1415926f * float(ii) / float(num_segments);//get the current angle 
        
            float x = r * cosf(theta);//calculate the x component 
            float y = r * sinf(theta);//calculate the y component 
        
            glVertex2f(x + cx, y + cy);//output vertex 
        
        } 
        glEnd(); 
    }

    /*
    1.4. An (i,j) pixel should be displayed by calling a method writePixel
    having at least 2 integer arguments: the column i and the row j.
    */
    void drawPixel(int i, int j){
        // draw a pixel
        glColor3f(0, 0, 1);
        /*
        1.3. Pixels should not intersect,
        */
        double ratio = std::min(abs((2.0 * 1 / rows)-(2.0 * 2 / rows)),
                             abs((2.0 * 1 / cols)-(2.0 * 2 / cols)))/5;
        drawCircle(-1.0 + 2.0 * i / cols, -1.0 + 2.0 * j / rows, ratio, 10);
        // printf("%f \n", ratio);
    }

    void drawAllPixels(){
        for(int i = 0; i <= rows; i++){
            for(int j = 0; j <= cols; j++){
                drawPixel(i, j);
            }
        }
    }

    /*
    2. Implement one of the course algorithms for displaying a line segment
whose endpoints have integer coordinates (see the image).
Those solutions that implement the algorithm ScanConvertSegments3
(by providing suitable changes to it, so the computation of the pixel
coordinates does not use the pixel coordinates computed by the
algorithm of the course) will be graded to the fullest.
    */

void drawLinePixels(int x0, int y0, int xn, int yn){
    if (x0 > xn) {
			swap(x0, xn);
			swap(y0, yn);
		}

    drawLine(x0, y0, xn, yn);
    if (yn >= y0 && abs(xn - x0) >= abs(yn - y0)) {
        int dx = xn - x0;
        int dy = abs(yn - y0);
        int d = 2 * dy - dx;
        int dE = 2 * dy;
        int dNE = 2 * (dy - dx);
        
        int x = x0, y = y0;
        drawPixel(x, y);
        while (x < xn)
        {
            if (d <= 0) {
                // alegem E 
                d += dE; x++; }
            else { //alegem NE 
                d += dNE; x++; y++; }
            drawPixel(x, y);
        }
    }
    // dy/dx > 1 si yn>=y0
		else if (yn >= y0 && abs(xn - x0) < abs(yn - y0)) {
			int dx = xn - x0;
			int dy = yn - y0;
			//int d = 2 * dx - dy;
			int d = dy - 2 * dx;
			int dN = -2 * dx;
			int dNE = 2 * (dy - dx);
			int x = x0;
			int y = y0;
            drawPixel(x, y);
			while (y < yn) {
				if (d > 0) {
					d += dN;
					y++;
				}
				else {
					d += dNE;
					x++; y++;
				}
                drawPixel(x, y);
			}
		}
		// dy/dx <= 1 si yn<=y0
		else if (yn <= y0 && abs(xn - x0) >= abs(yn - y0)) {
			int dx = xn - x0;
			int dy = yn - y0;
			int d = 2 * dy + dx;
			int dE = 2 * dy;
			int dSE = 2 * (dy + dx);
			int x = x0;
			int y = y0;
            drawPixel(x, y);
			while (x < xn) {
				if (d > 0) {
					d += dE;
					x++;
				}
				else {
					d += dSE;
					x++; y--;
				}
                drawPixel(x, y);

			}
		}
		// dy/dx > 1 si yn < y0 
		else if (y0 > yn && abs(xn - x0) < abs(yn - y0)) {
			int dx = xn - x0;
			int dy = yn - y0;
			int d = (dy + 2 * dx);
			int dS = 2 * dx;
			int dSE = 2 * (dx + dy);
			int x = x0;
			int y = y0;
            drawPixel(x, y);
			while (y > yn) {
				if (d < 0) {
					d += dS;
					y--;
				}
				else {
					d += dSE;
					x++; y--;
				}
                drawPixel(x, y);
			}
		}
}

   void drawLine(int x0, int y0, int xn, int yn){
    glColor3f(1,0.1,0.1); // rosu
    glBegin(GL_LINES);
        glVertex2f(-1.0 + 2.0 * x0 / rows, -1.0 + 2.0 * y0 / cols);
        glVertex2f(-1.0 + 2.0 * xn / rows, -1.0 + 2.0 * yn / cols);
    glEnd();
   }

   void convertMousePosition(int x, int y, int &x1, int &y1){
       x1 = x / (640 / cols);
       y1 = rows - y / (640 / rows);
   }

void drawCirclePoints(int x, int y, vector<pair<int, int>> &M) {
    // M.push_back(make_pair(x, y));
    // M.push_back(make_pair(-x, -y));
    // M.push_back(make_pair(-x, y));
    // M.push_back(make_pair(x, -y));
    if (x != y) {
        M.push_back(make_pair(y, x));
        //M.push_back(make_pair(-y, -x));
        M.push_back(make_pair(y, x+1));
        M.push_back(make_pair(y, x-1));
        M.push_back(make_pair(y+1, x));
        M.push_back(make_pair(y-1, x));

        // M.push_back(make_pair(-y, x));
        // M.push_back(make_pair(y, -x));
    }
}

  void drawCirclePixels(int R, vector<pair<int, int>> &M) {
    int x = 0, y = R;
    int d = 1 - R;
    int dE = 3, dSE = -2 * R + 5;
    M.clear();
    drawCirclePoints(x, y, M);
    while (y > x) {
        if (d < 0) {
            d += dE;
            dE += 2;
            dSE += 2;
        }
        else {
            d += dSE;
            dE += 2;
            dSE += 4;
            y--;
        }
        x++;
        drawCirclePoints(x, y, M);
    }
    for (auto p : M) {
        drawPixel(p.first, p.second);
    }
  }


};

void Display1() {
    CartesianGrid grid(6, 6);
    grid.draw();
    grid.drawPixel(2, 4);
    grid.drawPixel(2, 5);
    grid.drawPixel(4, 4);
    grid.drawPixel(4, 5);

    grid.drawPixel(1, 2);
    grid.drawPixel(2, 1);
    grid.drawPixel(3, 1);
    grid.drawPixel(4, 1);
    grid.drawPixel(5, 2);
    
}

void Display2() {
    CartesianGrid grid(50, 50);
    grid.draw();
    grid.drawAllPixels();
}

void Display3() {
    CartesianGrid grid(15, 15);
    grid.draw();
    grid.drawLinePixels(0,0, 15, 7);
    grid.drawLinePixels(0,15, 15, 10);

}

void Display4() {
    
    int size =15;
    int r=13;
    CartesianGrid grid(size, size);
    grid.draw();
    vector<pair<int, int>> M;
    glColor3f(1.0, 0.0, 0.0);
    grid.drawCircle(-1, -1, 2.0*r/size, 100, false);
    grid.drawCirclePixels(r, M);
}

void Display5() {

}

void Display6() {

}

void Display7() {

}

void Display8() {

}

void Init(void) {
   // specifica culoarea unui buffer dupa ce acesta
   // a fost sters utilizand functia glClear. Ultimul
   // argument reprezinta transparenta (1 - opacitate
   // completa, 0 - transparenta totala)
   glClearColor(1.0,1.0,1.0,1.0);

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

void Display(void) {
   printf("Call Display\n");

   // sterge buffer-ul indicat
   glClear(GL_COLOR_BUFFER_BIT);

   switch(prevKey) {
   case '1':
      Display1();
      break;
   case '2':
      Display2();
      break;
   case '3':
      Display3();
      break;
   case '4':
      Display4();
      break;
   case '5':
      Display5();
      break;
   case '6':
      Display6();
      break;
   case '7':
      Display7();
      break;
   case '8':
      Display8();
      break;
   default:
      break;
   }

   // forteaza redesenarea imaginii
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
   glViewport(0, 0, (GLsizei) w, (GLsizei) h);
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
      ((button == GLUT_RIGHT_BUTTON) ? "drept": "mijlociu"),
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
   glutInitWindowSize(640, 640);

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
   glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);

   // Functia int glutCreateWindow (char *name)
   // creeaza o fereastra cu denumirea data de argumentul
   // name si intoarce un identificator de fereastra.
   glutCreateWindow (argv[0]);

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
