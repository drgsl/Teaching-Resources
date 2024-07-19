#include <GL/freeglut_std.h>
#include <GL/freeglut.h>
unsigned char prevKey;

class Vector3
{
public:
  double x, y, z, w;

  Vector3() : Vector3(0, 0, 0, 1) {}
  Vector3(double _x, double _y = 0, double _z = 0, double _w = 0) : x(_x), y(_y), z(_z), w(_w) {}
};

class object
{
public:
  Vector3 position;
  Vector3 speed;
  Vector3 scale;

  bool collides(object& other) 
  {
      // Calculate half-widths and half-heights of both squares
      double halfWidthA = scale.x / 2.0;
      double halfHeightA = scale.y / 2.0;
      double halfWidthB = other.scale.x / 2.0;
      double halfHeightB = other.scale.y / 2.0;

      // Calculate the absolute difference between the x and y coordinates of the centers
      double deltaX = abs(position.x - other.position.x);
      double deltaY = abs(position.y - other.position.y);

      // Calculate the sum of half-widths and half-heights of both squares
      double sumHalfWidths = halfWidthA + halfWidthB;
      double sumHalfHeights = halfHeightA + halfHeightB;

      // Check if the absolute difference is less than or equal to the sum of half-widths and half-heights
      bool collisionX = deltaX <= sumHalfWidths;
      bool collisionY = deltaY <= sumHalfHeights;

      // If both axes have collisions, squares intersect
      return collisionX && collisionY;
  }
};

object dvd;

object vWalls[2];
object hWalls[2];

void rect(Vector3 center, Vector3 size)
{
  Vector3 topLeft    (center.x - size.x / 2, center.y + size.y / 2, 0.0, 1.0);
  Vector3 topRight   (center.x + size.x / 2, center.y + size.y / 2, 0.0, 1.0);
  Vector3 bottomRight(center.x + size.x / 2, center.y - size.y / 2, 0.0, 1.0);
  Vector3 bottomLeft (center.x - size.x / 2, center.y - size.y / 2, 0.0, 1.0);

  glBegin(GL_POLYGON);
      glVertex4f(bottomLeft.x, bottomLeft.y, bottomLeft.z, bottomLeft.w);
      glVertex4f(bottomRight.x, bottomRight.y, bottomRight.z, bottomRight.w);
      glVertex4f(topRight.x, topRight.y, topRight.z, topRight.w);
      glVertex4f(topLeft.x, topLeft.y, topLeft.z, topLeft.w);
  glEnd();
}

void display(void)
{
  glutSwapBuffers();
  glFlush();
  glutPostRedisplay();

  //background(0);
  glClearColor(0,0,0,0);
  glClear(GL_COLOR_BUFFER_BIT);

  //dvd.transform.position += dvd.rigidbody.velocity;
  dvd.position.x += dvd.speed.x;
  dvd.position.y += dvd.speed.y;

  //dvd.show()
  rect(dvd.position, dvd.scale);


  for (object& wall : vWalls)
  {
    rect(wall.position, wall.scale);
    if(wall.collides(dvd))
    {
      dvd.speed.x = - dvd.speed.x;
    }
  }

  for (object& wall : hWalls)
  {
    rect(wall.position, wall.scale);
    if(wall.collides(dvd))
    {
      dvd.speed.y = - dvd.speed.y;
    }
  }
}

void reshape(int w, int h)
{
  glViewport(0,0,(GLsizei) w, (GLsizei) h);
}

void keyboard(unsigned char key, int x, int y) 
{
  if (key == 27)
      exit(0);
  if (key == 'r')
      dvd.position = Vector3(0,0);
}

void keyUp(unsigned char key, int x, int y) {}

void mouse(int button, int state, int x, int y) {}

int main (int argc, char** argv)
{
  glutInit(&argc, argv);
  glutInitWindowSize(480, 480); // 480x640
  glutInitWindowPosition(0,0);
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA);
  glutCreateWindow("Canvas");

  glutReshapeFunc(reshape);
  glutDisplayFunc(display);
  glutKeyboardFunc(keyboard);
  glutKeyboardUpFunc(keyUp); // Register key release event
  glutMouseFunc(mouse);

  dvd.position   = Vector3(0,0);
  dvd.speed      = Vector3(0.01, 0.001);
  dvd.scale      = Vector3(1, 1);

  vWalls[0].position  = Vector3(-1,  0);
  vWalls[0].scale     = Vector3(0.01, 2);
  
  vWalls[1].position  = Vector3( 1,  0);
  vWalls[1].scale     = Vector3(0.01, 2);

  hWalls[0].position  = Vector3( 0, -1);
  hWalls[0].scale     = Vector3(2, 0.01);
  
  hWalls[1].position  = Vector3( 0,  1);
  hWalls[1].scale     = Vector3(2, 0.01);

  glutMainLoop();
}
