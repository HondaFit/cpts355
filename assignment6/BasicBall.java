/******************************************************************************
 *  Compilation:  javac ColoredBall.java
 *  Execution:    java ColoredBall
 *  Dependencies: StdDraw.java
 *
 *  Implementation of a 2-d ball moving in square with coordinates
 *  between -1 and +1. Bounces off the walls upon collision.
 *  
 *
 ******************************************************************************/

 import java.awt.Color;

 public class BasicBall { 
     protected double rx, ry;         // position
     protected double vx, vy;         // velocity
     protected double radius;   // radius
     protected final Color color;     // color
     public boolean isOut;
     
 
     // constructor
     public BasicBall(double r, Color c) {
         rx = 0.0;
         ry = 0.0;
         vx = StdRandom.uniform(-0.01, 0.01);
         vy = StdRandom.uniform(-0.01, 0.01);
         radius = r;
         color = c;
         isOut = false;
     }
    
    
     // move the ball one step
     public void move() {
         rx = rx + vx;
         ry = ry + vy;
         if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
             isOut = true;
     }
 
     // draw the ball
     public void draw() { 
         if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
             StdDraw.setPenColor(color);
             StdDraw.filledCircle(rx, ry, radius);
         } else
             isOut = true;
         
     }
 
     public int reset() {
         rx = 0.0;
         ry = 0.0;   
         vx = StdRandom.uniform(-0.01, 0.01); // assign a random speed in x direction
         vy = StdRandom.uniform(-0.01, 0.01); // assign a random speed in y direction
         return 1;
     }
     
     public boolean isHit(double x, double y) {
         if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) {
             reset(); // reset the ball position and assign new random speeds
             return true;
         }
         else return false; 
 
     }
     public int getScore() {
         return 25;
     }
     
     public double getRadius() {
         return radius;
     }
 
 
 }
 
 class ShrinkBall extends BasicBall {
     private double initialRadius;
 
     public ShrinkBall(double r, Color c) {
         super(r, c);
         initialRadius = r;
     }
 
     @Override
     public boolean isHit(double x, double y) {
         if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) {
             radius *= 0.67; // reduce the size by 33%
             if (radius <= 0.25 * initialRadius) {
                 radius = initialRadius; // reset to original size
             }
             reset(); // reset the ball position and assign new random speeds
             return true;
         }
         else return false;
     }
 
     @Override
     public int getScore() {
         return 20;
     }
 }
 
 class BounceBall extends BasicBall {
     private int bounceCount;
 
     public BounceBall(double r, Color c) {
         super(r, c);
         bounceCount = 0;
     }
 
     @Override
     public void move() {
         rx = rx + vx;
         ry = ry + vy;
         if (Math.abs(rx) > 1.0) {
             vx = -vx; // reverse x direction
             bounceCount++;
         }
         if (Math.abs(ry) > 1.0) {
             vy = -vy; // reverse y direction
             bounceCount++;
         }
         if (bounceCount >= 3) {
             isOut = true;
         }
     }
 
     @Override
     public boolean isHit(double x, double y) {
         if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) {
             reset(); // reset the ball position and assign new random speeds
             return true;
         }
         else return false;
     }
 
     @Override
     public int getScore() {
         return 15;
     }
 }
 
 class SplitBall extends BasicBall {
 
     public SplitBall(double r, Color c) {
         super(r, c);
     }
 
     @Override
     public boolean isHit(double x, double y) {
         if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius)) {
             // create two new split balls with the same radius
             SplitBall ball1 = new SplitBall(radius, color);
             SplitBall ball2 = new SplitBall(radius, color);
             // add the new split balls to the game (assuming a method addBall exists in the game class)
             BallGame.addBall(ball1);
             BallGame.addBall(ball2);
             reset(); // reset the ball position and assign new random speeds
             return true;
         }
         else return false;
     }
 
     @Override
     public int getScore() {
         return 10;
     }
 }