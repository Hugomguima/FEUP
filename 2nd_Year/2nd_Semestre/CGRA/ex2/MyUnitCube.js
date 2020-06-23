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
			0, 0, 0,	//0
			1, 0, 0,	//1
			0, 0, 1,	//2
            1, 0, 1	,	//3
            0, 1, 0,	//4
			1, 1, 0,	//5
			0, 1, 1,	//6
			1, 1, 1 	//7
		];

		//Counter-clockwise reference of vertices
		this.indices = [
            0, 1, 2,
            1, 3, 2,

            2, 3, 6,
            3, 7, 6,

            3, 1, 7,
            1, 5, 7,

            6, 7, 4,
            7, 5, 4,

            4, 1, 0,
            5, 1, 4,
            
            6, 0, 2,
			4, 0, 6
		];

		//The defined indices (and corresponding vertices)
		//will be read in groups of three to draw triangles
		this.primitiveType = this.scene.gl.TRIANGLES;

		this.initGLBuffers();
	}
}

