#version 430

out vec4 color;

void main(void)
{ 
//color = vec4(0.0, 0.0, 1.0, 1.0);

if (gl_FragCoord.x < 295) 
	color = vec4(1.0, 0.0, 0.0, 1.0); 
else 
	color = vec4(0.0, 0.0, 1.0, 1.0);
}