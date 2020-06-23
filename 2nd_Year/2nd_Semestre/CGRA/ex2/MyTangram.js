/**
 * MyTangram
 * @constructor
 * @param scene - Reference to MyScene object
 */
class MyTangram extends CGFobject {
	constructor(scene) {
		super(scene);

        //Initialize scene objects
        this.diamond = new MyDiamond(scene);
        this.triangle = new MyTriangle(scene);
        this.parallelogram = new MyParallelogram(scene);
        this.fig5 = new MyFigura5(scene);
        this.fig6 = new MyFigura6(scene);
    }

    display(){
        // ---- BEGIN Primitive drawing section

				//Diamond (Green)
        this.scene.pushMatrix();
        this.scene.rotate(Math.PI/4,0,0,1);
				this.scene.setDiffuse(0, 1, 0, 1);
        this.diamond.display();
        this.scene.popMatrix();

				//Small Triangle (Purple)
        this.scene.pushMatrix();
        this.scene.translate(0,Math.sqrt(2)/2 + Math.sqrt(2)/2,0);
        this.scene.rotate(3*Math.PI/4,0,0,1);
				this.scene.setDiffuse(149/255, 79/255, 191/255, 1);
        this.fig5.display();
        this.scene.popMatrix();

				//Small Triangle (Red)
        this.scene.pushMatrix();
        this.scene.translate(0,4*Math.sqrt(2)/2,0);
        this.scene.rotate(Math.PI/4,0,0,1);
				this.scene.setDiffuse(1, 27/255, 28/255, 1);
        this.fig5.display();
        this.scene.popMatrix();

				//Triangle (Pink)
        this.scene.pushMatrix();
        this.scene.translate(Math.sqrt(2)/2,3/2*Math.sqrt(2),0);
        this.scene.rotate(7*Math.PI/4,0,0,1);
				this.scene.setDiffuse(1, 155/255, 207/255, 1);
        this.triangle.display();
        this.scene.popMatrix();

				//Triangle (Blue)
        this.scene.pushMatrix();
        this.scene.translate(0,1+5*Math.sqrt(2)/2,0);
        this.scene.rotate(Math.PI,0,0,1);
				this.scene.setDiffuse(0/255, 155/255, 255/255, 1);
        this.triangle.display();
        this.scene.popMatrix();

				//Triangle (Orange)
        this.scene.pushMatrix();
        this.scene.translate(0,1+5*Math.sqrt(2)/2,0);
				this.scene.setDiffuse(255/255, 155/255, 0/255, 1);
        this.triangle.display();
        this.scene.popMatrix();

				//Parallelogram (Yellow)
        this.scene.pushMatrix();
        this.scene.translate(-2 + Math.sqrt(2), 0.1 + 5 + 5*Math.sqrt(2)/2, 0);
        this.scene.rotate(-Math.PI/2 + Math.PI/6, 0, 0, 1);
        this.scene.scale(1, -1, 1);
				this.scene.setDiffuse(1, 1, 0, 1);
        this.parallelogram.display();
        this.scene.popMatrix();

				this.scene.setDefaultAppearance();

        // ---- END Primitive drawing section
    }
}
