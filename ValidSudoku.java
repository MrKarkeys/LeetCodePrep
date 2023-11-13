class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> seenRow = new HashSet<String>();
        HashSet<String> seenCol = new HashSet<String>();
        HashSet<String> seenMatrix = new HashSet<String>();
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board.length; j++){
                if(board[i][j] != '.'){
                    String valRow = "<"+board[i][j]+i+">";
                    String valCol = "<"+board[i][j]+j+">";
                    String valMatrix = "<"+ board[i][j]+i/3+j/3+">";
                    if(seenRow.contains(valRow) || seenCol.contains(valCol) || seenMatrix.contains(valMatrix)){
                        return false;
                    }
                    else{
                        seenRow.add(valRow);
                        seenCol.add(valCol);
                        seenMatrix.add(valMatrix);
                    }
                }
            }
        }
        return true;
    }
}