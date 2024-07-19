class RubiksCube {

    public static Piece[][][] cube = new Piece[3][3][3];

    public static void main(String[] args) {

        int color = 0;

        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++) {
                    cube[i][j][k] = new Piece();
                    cube[i][j][k].setCol(color);
                }
            }
            color++;
        }

        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++) {
                    System.out.print(cube[i][j][k].col + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
}