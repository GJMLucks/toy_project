package main

import (
	"fmt"
)

const (
	blank = 0
	black = 0
	white = 8
)	// color

const (
	blackPawn = black + iota + 1
	blackRook
	blackKnight
	blackBishop
	blackQueen
	blackKing
)	// black pieces

const (
	whitePawn = white + iota + 1
	whiteRook
	whiteKnight
	whiteBishop
	whiteQueen
	whiteKing
)	// white pieces

var defaultPieceSetup = [64]int{
	blackRook, blackKnight, blackBishop, blackQueen, blackKing, blackBishop, blackKnight, blackRook,
	blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, 
	blank, blank, blank, blank, blank, blank, blank, blank,  
	blank, blank, blank, blank, blank, blank, blank, blank,  
	blank, blank, blank, blank, blank, blank, blank, blank,  
	blank, blank, blank, blank, blank, blank, blank, blank,
	whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, 
	whiteRook, whiteKnight, whiteBishop, whiteQueen, whiteKing, whiteBishop, whiteKnight, whiteRook
}

type chess struct {
	board [64]int
	moveCount int
}

func (_ chess) printPiece(piece int) error {
	// err checking
	if piece < 0 || piece > 16 {
		return fmt.Errorf("%d is out of range", piece)
	}
	
	print("|")
	
	// blank
	if piece == 0 {
		print (" _ ")
		return nil
	}
	// color
	if piece / 8 == 0 {
		print(".")
	} else {
		print(" ")
	}
	// piece
	switch {
	case piece % 8 == 1 :
		print("P")

	case piece % 8 == 2 :
		print("R")

	case piece % 8 == 3 :
		print("N")

	case piece % 8 == 4 :
		print("B")

	case piece % 8 == 5 :
		print("Q")

	case piece % 8 == 6 :
		print("K")
		
	default :
		return fmt.Errorf("%d is non-exist piece", piece)
	}

	print(" ")

	return nil
}

func (c *chess) reset() {
	c.board = defaultPieceSetup
	c.moveCount = 0
}

func (c chess) printBoard() {
	println("  *===============================*")

	for row = 0; row < 8; row++ {
		print(8-row, " ")
	
		for col = 0; col < 8; col++ {
			c.printPiece( c.board[i*8 + j] );
		}

		print("|")

		if i == 7 {
			break
		}
		
		print("  ---------------------------------");

	}

	print("  *===============================*");
	print("    a   b   c   f   e   f   g   h ");
	print("   (1) (2) (3) (4) (5) (6) (7) (8)");
}

func (c chess) teamToMove() string {
	return "White" if c.moveCount % 2 == 0 else "Black"
}

func (c chess) turn() int {
	return ( c.moveCount / 2 ) + 1	
}

func main()	{

	chess := [64]int{}


}