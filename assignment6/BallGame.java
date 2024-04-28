/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science: An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments: 1 basic 0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

class Player {
    private int score;
    private int basicHits;
    private int shrinkHits;
    private int bounceHits;
    private int splitHits;

    public Player() {
        score = 0;
        basicHits = 0;
        shrinkHits = 0;
        bounceHits = 0;
        splitHits = 0;
    }

    public void addScore(int points) {
        score += points;
    }

    public void incrementBasicHits() {
        basicHits++;
    }

    public void incrementShrinkHits() {
        shrinkHits++;
    }

    public void incrementBounceHits() {
        bounceHits++;
    }

    public void incrementSplitHits() {
        splitHits++;
    }

    public int getScore() {
        return score;
    }

    public int getBasicHits() {
        return basicHits;
    }

    public int getShrinkHits() {
        return shrinkHits;
    }

    public int getBounceHits() {
        return bounceHits;
    }

    public int getSplitHits() {
        return splitHits;
    }
}

public class BallGame {
    public static ArrayList<BasicBall> balls;
    public static int numBallsinGame;

    public static void addBall(BasicBall ball) {
        balls.add(ball);
        numBallsinGame++;
    }

    public static void incrementBallCount() {
        numBallsinGame++;
    }

    public static void main(String[] args) {
        // number of bouncing balls
        int numBalls = Integer.parseInt(args[0]);
        //ball types
        String ballTypes[] = new String[numBalls];
        //sizes of balls
        double ballSizes[] = new double[numBalls];
        
        //retrieve ball types
        int index =1;
        for (int i=0; i<numBalls; i++) {
            ballTypes[i] = args[index];
            index = index+2;
        }
        //retrieve ball sizes
        index = 2;
        for (int i=0; i<numBalls; i++) {
            ballSizes[i] = Double.parseDouble(args[index]);
            index = index+2;
        }
     
        // create a Player object and initialize the player game stats
        Player player = new Player();
        
        //number of active balls
        numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();
    
        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);
    
        // create colored balls 
        balls = new ArrayList<>();
        for (int i = 0; i < numBalls; i++) {
            BasicBall ball;
            if (ballTypes[i].equals("basic")) {
                ball = new BasicBall(ballSizes[i], Color.RED);
            } else if (ballTypes[i].equals("shrink")) {
                ball = new ShrinkBall(ballSizes[i], Color.GREEN);
            } else if (ballTypes[i].equals("bounce")) {
                ball = new BounceBall(ballSizes[i], Color.BLUE);
            } else if (ballTypes[i].equals("split")) {
                ball = new SplitBall(ballSizes[i], Color.ORANGE);
            } else {
                continue;
            }
            balls.add(ball);
        }
        numBallsinGame = numBalls;
        
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {
    
            // move all balls
            for (BasicBall ball : balls) {
                ball.move();
            }
    
            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                // check whether a ball is hit. Check each ball.
                for (BasicBall ball : balls) {
                    if (ball.isHit(x,y)) {
                        // Update player statistics based on ball type
                        if (ball instanceof ShrinkBall) {
                            player.addScore(ball.getScore());
                            player.incrementShrinkHits();
                        } else if (ball instanceof BounceBall) {
                            player.addScore(ball.getScore());
                            player.incrementBounceHits();
                        } else if (ball instanceof SplitBall) {
                            player.addScore(ball.getScore());
                            player.incrementSplitHits();
                        } else {
                            player.addScore(ball.getScore());
                            player.incrementBasicHits();
                        }
                    }
                }
            }
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            // check each ball and see if they are still visible
            for (BasicBall ball : balls) {
                if (!ball.isOut) { 
                    ball.draw();
                    numBallsinGame++;
                }
            }
            
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            StdDraw.text(-0.65, 0.80, "Current Score: " + player.getScore());
    
            StdDraw.show();
            StdDraw.pause(20);
        }
        
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            
            font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(0, -0.2, "Final Score: " + player.getScore());
            StdDraw.text(0, -0.3, "Basic Hits: " + player.getBasicHits());
            StdDraw.text(0, -0.4, "Shrink Hits: " + player.getShrinkHits());
            StdDraw.text(0, -0.5, "Bounce Hits: " + player.getBounceHits());
            StdDraw.text(0, -0.6, "Split Hits: " + player.getSplitHits());
            
            StdDraw.show();
            StdDraw.pause(10);           
        }
    }
}