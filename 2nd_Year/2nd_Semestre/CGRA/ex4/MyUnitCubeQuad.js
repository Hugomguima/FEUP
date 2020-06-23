/**
 * MyUnitCubeQuad
 * @constructor
 * @param scene - Reference to MyScene object
 */
class MyUnitCubeQuad extends CGFobject {
	constructor(scene) {
		super(scene);
		this.quad = new MyQuad(scene);
		this.minecraftTexture = new CGFappearance(this.scene);
		this.minecraftTexture.setAmbient(0.1, 0.1, 0.1, 1);
		this.minecraftTexture.setDiffuse(0.9, 0.9, 0.9, 1);
		this.minecraftTexture.setSpecular(0.1, 0.1, 0.1, 1);
		this.minecraftTexture.setShininess(10.0);
		this.minecraftTexture.loadTexture('images/earth.jpg');
		this.minecraftTexture.setTextureWrap('REPEAT', 'REPEAT');
		this.top = new CGFtexture(this.scene,'images/earth.jpg');
    	this.bottom = new CGFtexture(this.scene,'images/earth.jpg');
    	this.side = new CGFtexture(this.scene,'images/earth.jpg');
		}
		textureTop() {
			this.minecraftTexture.setTexture(this.top);
		}
		textureSide() {
			this.minecraftTexture.setTexture(this.side);
		}
		textureBottom() {
			this.minecraftTexture.setTexture(this.bottom);
		}
		display() {
			// Side
			this.textureSide();
			this.minecraftTexture.apply();
	    	this.scene.gl.texParameteri(this.scene.gl.TEXTURE_2D, this.scene.gl.TEXTURE_MAG_FILTER, this.scene.gl.NEAREST);
			//Side 1
			this.scene.pushMatrix();
			this.scene.rotate(-Math.PI/2, 0,1,0);
			this.scene.translate(0,0,0.5);
	    this.quad.display();
	    this.scene.popMatrix();
			//Side 2
	    this.scene.pushMatrix();
			this.scene.translate(0,0,0.5);
	    this.quad.display();
	    this.scene.popMatrix();
			//Side 3
			this.scene.pushMatrix();
			this.scene.rotate(Math.PI/2, 0,1,0);
			this.scene.translate(0,0,0.5);
			this.quad.display();
			this.scene.popMatrix();
			//Side 4
			this.scene.pushMatrix();
			this.scene.rotate(Math.PI, 0,1,0);
			this.scene.translate(0, 0,0.5);
			this.quad.display();
			this.scene.popMatrix();

			// Bottom
			this.textureBottom();
			this.minecraftTexture.apply();
	    this.scene.gl.texParameteri(this.scene.gl.TEXTURE_2D, this.scene.gl.TEXTURE_MAG_FILTER, this.scene.gl.NEAREST);
	    this.scene.pushMatrix();
	    this.scene.rotate(Math.PI/2, 1,0,0);
			this.scene.translate(0,0,0.5);
	    this.quad.display();
	    this.scene.popMatrix();

			// Top
			this.textureTop();
			this.minecraftTexture.apply();
	    this.scene.gl.texParameteri(this.scene.gl.TEXTURE_2D, this.scene.gl.TEXTURE_MAG_FILTER, this.scene.gl.NEAREST);
	    this.scene.pushMatrix();
			this.scene.rotate(-Math.PI/2, 1,0,0);
			this.scene.translate(0,0,0.5);
	    this.quad.display();
	    this.scene.popMatrix();


		}
}
