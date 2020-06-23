attribute vec3 aVertexPosition;
attribute vec3 aVertexNormal;
attribute vec2 aTextureCoord;

uniform mat4 uMVMatrix;
uniform mat4 uPMatrix;
uniform mat4 uNMatrix;

uniform sampler2D waterMap;
uniform sampler2D waterTex;
uniform float timeFactor;

varying vec2 vTextureCoord;
varying vec3 offset;

void main() {

  vec3 offset=vec3(0.0,0.0,0.0);

  vec4 filter = texture2D(waterMap, aTextureCoord + timeFactor*(0.01,0.01));

  if(filter.b > 0.5)
    offset = 0.045 * aVertexNormal;

	gl_Position = uPMatrix * uMVMatrix * vec4(aVertexPosition + offset, 1.0);

  vTextureCoord = aTextureCoord;
}
