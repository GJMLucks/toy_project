public class App {
    public static final byte none = 0x00;

    public static final byte pawn = 0x01;
    public static final byte bishop = 0x02;
    public static final byte knight = 0x03;
    public static final byte rook = 0x04;
    public static final byte queen = 0x05;
    public static final byte king = 0x06;

    public static final byte white = 0x10;
    public static final byte black = 0x20;

    public static final byte whitepawn = 0x11;
    public static final byte whitebishop = 0x12;
    public static final byte whiteknight = 0x13;
    public static final byte whiterook = 0x14;
    public static final byte whitequeen = 0x15;
    public static final byte whiteking = 0x16;
    public static final byte blackpawn = 0x21;
    public static final byte blackbishop = 0x22;
    public static final byte blackknight = 0x23;
    public static final byte blackrook = 0x24;
    public static final byte blackqueen = 0x25;
    public static final byte blackking = 0x26;

    public static final byte[][] defaultChessPostion = {
            { whiterook, whiteknight, whitebishop, whitequeen, whiteking, whitebishop, whiteknight, whiterook },
            { whitepawn, whitepawn, whitepawn, whitepawn, whitepawn, whitepawn, whitepawn, whitepawn },
            { none, none, none, none, none, none, none, none },
            { none, none, none, none, none, none, none, none },
            { none, none, none, none, none, none, none, none },
            { none, none, none, none, none, none, none, none },
            { blackpawn, blackpawn, blackpawn, blackpawn, blackpawn, blackpawn, blackpawn, blackpawn },
            { blackrook, blackknight, blackbishop, blackqueen, blackking, blackbishop, blackknight, blackrook }
    };

    public byte[][] ChessPosition = defaultChessPostion;
    public int enpassantPosition = 0x00;

    public static String byteToStringPiece(byte bytePiece) {
        switch (bytePiece) {
            case whitepawn:
                return "WP";
            case whitebishop:
                return "WB";
            case whiteknight:
                return "WN";
            case whiterook:
                return "WR";
            case whitequeen:
                return "WQ";
            case whiteking:
                return "WK";

            case blackpawn:
                return "BP";
            case blackbishop:
                return "BB";
            case blackknight:
                return "BN";
            case blackrook:
                return "BR";
            case blackqueen:
                return "BQ";
            case blackking:
                return "BK";

            default:
                return "  ";
        }
    }

    public void printChess() {
        String[] tempString;

        System.out.println("=========================================");

        for (byte[] chessRow : ChessPosition) {
            tempString = new String[8];
            for (int index = 0; index < chessRow.length; index++) {
                tempString[index] = byteToStringPiece(chessRow[index]);
            }

            System.out.println("| " + String.join(" | ", tempString) + " |");
            System.out.println("=========================================");
        }
    }

    public void movePiece(byte initPosition, byte postPosition) {
        if ((initPosition >> 6) + (postPosition >> 6) != 0) {
            System.err.println("movePiece : out of range");
            return;
        }

        ChessPosition[postPosition >> 3][postPosition & 0x07] = ChessPosition[initPosition >> 3][initPosition | 0x07];
        ChessPosition[initPosition >> 3][initPosition & 0x07] = none;
    }

    public boolean isPieceBlocked(byte initPosition, byte postPosition) {
        /**
         * Precondition :
         * move is horizontal, vertical or diagonal move
         */

        int initPosRow = initPosition >> 3;
        int initPosCol = initPosition & 0x7;
        int postPosRow = postPosition >> 3;
        int postPosCol = postPosition & 0x7;

        if (initPosRow == postPosRow) { // horizontal move
            int startIndex = (initPosCol < postPosCol) ? initPosCol : postPosCol;
            int endIndex = (initPosCol > postPosCol) ? initPosCol : postPosCol;

            for (int i = startIndex + 1; i < endIndex; i++) {
                if (ChessPosition[initPosRow][i] != none) {
                    return true;
                }
            }
            return false;
        }

        if (initPosCol == postPosCol) { // vertical move
            int startIndex = (initPosRow < postPosRow) ? initPosRow : postPosRow;
            int endIndex = (initPosRow > postPosRow) ? initPosRow : postPosRow;

            for (int i = startIndex + 1; i < endIndex; i++) {
                if (ChessPosition[i][initPosCol] != none) {
                    return true;
                }
            }
            return false;
        }

        // diagonal move
        int rowIncrement = (initPosRow < postPosRow) ? 1 : -1;
        int colIncrement = (initPosCol < postPosCol) ? 1 : -1;
        int rowIndex = initPosRow;
        int colIndex = initPosCol;

        while ((rowIndex != postPosRow) || (colIndex != postPosCol)) {
            rowIndex += rowIncrement;
            colIndex += colIncrement;

            if (ChessPosition[rowIndex][colIndex] != none) {
                return true;
            }
        }

        return false;
    }

    public boolean isLegalMove(byte initPosition, byte postPosition) {
        if (initPosition == postPosition) {
            System.err.println("isLegalMove : init and post position are same");
            return false;
        }
        if ((initPosition >> 6) + (postPosition >> 6) != 0) {
            System.err.println("isLegalMove : out of range");
            return false;
        }

        int initPosRow = initPosition >> 3;
        int initPosCol = initPosition & 0x7;
        int postPosRow = postPosition >> 3;
        int postPosCol = postPosition & 0x7;

        byte initPiece = ChessPosition[initPosRow][initPosCol];
        byte postPiece = ChessPosition[postPosRow][postPosCol];

        int initPieceKind = initPiece & 0x0F;
        int initTeam = (initPiece >> 4) & 0x0F;
        int postPieceKind = postPiece & 0x0F;
        int postTeam = (postPiece >> 4) & 0x0F;

        if (initTeam == none) {
            System.err.println("isLegalMove : moving piece is nonexistent");
            return false;
        }
        if (initTeam == postTeam) {
            System.err.println("isLegalMove : same team piece is blocking");
            return false;
        }

        int rowDistance = (initPosRow > postPosRow) ? (initPosRow - postPosRow) : (postPosRow - initPosRow);
        int colDistance = (initPosCol > postPosCol) ? (initPosCol - postPosCol) : (postPosCol - initPosCol);

        if (rowDistance + colDistance > 3
                && rowDistance != 0
                && colDistance != 0
                && rowDistance != colDistance) {
            return false;
        }

        switch (initPieceKind) {
            case pawn:
                if ((initTeam == black ? (postPosRow > initPosRow) : (postPosRow < initPosRow))
                        || rowDistance == 0
                        || rowDistance + colDistance > 2) {
                    return false;
                }

                if (rowDistance == 2
                        && (initTeam == black ? (initPosRow != 6) : (initPosRow != 1))) {
                    return false;
                }
                if (colDistance == 1
                        && enpassantPosition != postPosition
                        && postPieceKind == none) {
                    System.err.println("isLegalMove : there is no opponent piece");
                    return false;
                }

                if (rowDistance == 2) {
                    enpassantPosition = (initTeam == black ? initPosition + 8 : initPosition - 8);
                }

                // collision test
                return true;

            case bishop:
                if (rowDistance == colDistance) {
                    // collision test
                    return true;
                }
                return false;

            case knight:
                if (rowDistance + colDistance != 3
                        || rowDistance == 0
                        || colDistance == 0) {
                    return false;
                }
                return true;

            case rook:
                if (rowDistance == 0
                        || colDistance == 0) {
                    // collision test
                    return true;
                }
                return false;

            case queen:
                if (rowDistance == 0
                        || colDistance == 0
                        || rowDistance == colDistance) {
                    // collision test
                    return true;
                }
                return false;

            case king:
                if (rowDistance > 1
                        || colDistance > 1) {
                    return false;
                }
                // check test
                return true;
            default:
                break;
        }

        return true;
    }

    public static void main(String[] args) {
        App chess = new App();
        chess.printChess();
    }
}
