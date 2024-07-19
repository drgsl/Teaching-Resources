#include <Adafruit_NeoPixel.h>


struct RubiksCube{
  Adafruit_NeoPixel strips[3];
};

RubiksCube cube;

void setup()
{
  cube.strips[0] = 
  Adafruit_NeoPixel(9,11,NEO_GRB + NEO_KHZ800);
  cube.strips[0].begin();
  
  cube.strips[1] = 
  Adafruit_NeoPixel(9,10,NEO_GRB + NEO_KHZ800);
  cube.strips[1].begin();
  
  cube.strips[2] = 
  Adafruit_NeoPixel(9,9,NEO_GRB + NEO_KHZ800);
  cube.strips[2].begin();
  
}

void loop()
{
  for(int idx = 0; idx <=2; idx++){
    
    for(int i =0; i<=9; i++){
      cube.strips[idx].setPixelColor(i,255,0,0);
      cube.strips[idx].show();
    }
  }
}

void showSolvedCube(){
  
}