/**
 * MyUnitCube
 * @constructor
 * @param scene - Reference to MyScene object
 */
class MyUnitCube extends CGFobject {
	constructor(scene) {
		super(scene);
		this.initBuffers();
	}
	initBuffers() {
		this.vertices = [
			/*
			*
			*
			*
			*  [18,19,20], [15, 16, 17]      						 + + + + + + +
			*					      							   +  +        + +
			*					    							 +   +      +    +
			*	 [21,22,23], [12, 13, 14] 						+ + + + + +      +
			*					   								+    +    +      +
			*	 [6,7,8], [3,4,5]  								+    +    +      +
			*					   								+    +  + +  + + +
			*					   								+ +       +   +
	    	*   [9, 10, 11], [0,1,2]							+ + + + + +
			*
			*/

			// Baixo
      		0.5, 0.5, -0.5,
			0.5, 0.5, -0.5,
			0.5, 0.5, -0.5,

      		-0.5, 0.5, -0.5,
			-0.5, 0.5, -0.5,
			-0.5, 0.5, -0.5,

      		-0.5, -0.5, -0.5,
			-0.5, -0.5, -0.5,
			-0.5, -0.5, -0.5,

			0.5, -0.5, -0.5,
			0.5, -0.5, -0.5,
			0.5, -0.5, -0.5,

			// Cima
			0.5, 0.5, 0.5,
			0.5, 0.5, 0.5,
			0.5, 0.5, 0.5,

			-0.5, 0.5, 0.5,
			-0.5, 0.5, 0.5,
			-0.5, 0.5, 0.5,

			-0.5, -0.5, 0.5,
			-0.5, -0.5, 0.5,
			-0.5, -0.5, 0.5,

			0.5, -0.5, 0.5,
			0.5, -0.5, 0.5,
			0.5, -0.5, 0.5,
		];

		//Counter-clockwise reference of vertices
		this.indices = [
			//Part 1
			//Face 0
			0, 3, 15,
			15, 12, 0,

			//Face 2
			4, 6, 18,
			18, 16, 4,

			//Face 3
			7, 9, 21,
			21, 19, 7,

			//Face 4
			10, 1, 13,
			13, 22, 10,

			//Face 5
			5, 2, 11,
			11, 8, 5,

			//Face 6
			23 , 14, 17,
			17, 20, 23,
		];



		this.normals = [
			 0,  1,  0,  // 0
			 1,  0,  0,  // 1
			 0,  0, -1,  // 2
			 0,  1,  0,  // 3
			-1,  0,  0,  // 4
			 0,  0, -1,  // 5
			-1,  0,  0,  // 6
			 0, -1,  0,  // 7
			 0,  0, -1,  // 8
			 0, -1,  0,  // 9
			 1,  0,  0,  // 10
			 0,  0, -1,  // 11
			 0,  1,  0,  // 12
			 1,  0,  0,  // 13
			 0,  0,  1,  // 14
			 0,  1,  0,  // 15
			-1,  0,  0,  // 16
			 0,  0,  1,  // 17
			-1,  0,  0,  // 18
		 	 0, -1,  0,  // 19
			 0,  0,  1,  // 20
			 0, -1,  0,  // 21
			 1,  0,  0,  // 22
			 0,  0,  1   // 23
		];


		this.primitiveType = this.scene.gl.TRIANGLES;
		this.initGLBuffers();
	}
}
