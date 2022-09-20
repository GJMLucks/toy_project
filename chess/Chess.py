
# 파이썬 문법을 이용한 체스 만들기 프로젝트

class Chess():

    def __init__(self): # __init__ 은 생성자(Constructor). 클래스 생성시 실행
        # 0 = none,  1 = pawn, 2 = rook, 3 = knight, 4 = bishop, 5 = queen, 6 = king
        self.dict_PieceKind = { 0 : "_", 1 : "P", 2 : "R", 3 : "N", 4 : "B", 5 : "Q", 6 : "K"};

        # 1bit(Team) + 3bit(kind)
        # 0 = white, 1 = black
        # ex) 1001 = black pawn

        self.inital_Position = (10,11,12,13,14,12,11,10, # 고정 초기값
                                 9, 9, 9, 9, 9, 9, 9, 9,
                                 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0,
                                 1, 1, 1, 1, 1, 1, 1, 1,
                                 2, 3, 4, 5, 6, 4, 3, 2);

        self.position   = list(self.inital_Position);
        self.round      = 0;

        # 2bit(castling flag) + 3bit(en passant flag)
        # 11000 = invalid all castling, noting at en passant
        self.special_Mov_flag = [0, 0];


    def _Initial(self): # 초기화
        self.position   = list(self.inital_Position);
        self.round      = 0;


    def _CountUp(self): self.round += 1;    # 턴 넘기기


    def _PrintPiece(self, Pos): # 기물 출력
        team = self.position[Pos]//8;
        kind = self.position[Pos]% 8;

        print("| ", end="");

        Temp = self.dict_PieceKind.get(kind);

        if Temp: print(Temp, end="");
        else   : 
            print("Piece Print err");
            return;

        # "." mean black piece
        if team: print(".", end="");
        else   : print(" ", end="");


    def _PrintChess(self):  # 체스 출력
        print("  *===============================*");

        for i in range(8):
            print(8-i, end=" ");

            for j in range(8): self._PrintPiece( i*8 + j );

            print("|");
            if i == 7: break;
            print("  ---------------------------------");

        print("  *===============================*");
        print("    a   b   c   f   e   f   g   h ");
        print("   (1) (2) (3) (4) (5) (6) (7) (8)");


    def _Moving(self, Pos, Mov_Pos):    # 기물 옮기기
        self.position[Mov_Pos]  = self.position[Pos];
        self.position[Pos]      = 0;


    def _Changing(self, Pos, Piece):    # function for promotion 
        if self.position[Pos]: self.position[Pos] = Piece;
        else                 : print("Change err");


    def _RouteCheck(self, Pos, Mov_Pos):    # 이동가능한 경로인가?
        x_dis = Mov_Pos% 8 - Pos% 8;
        y_dis = Mov_Pos//8 - Pos//8;
        offset        = 0;

        if not x_dis or not y_dis:
            if   x_dis:
                if x_dis > 0: offset =  1;
                else        : offset = -1;
            elif y_dis:
                if y_dis > 0: offset =  8;
                else        : offset = -8;
        elif abs(x_dis) == abs(y_dis):
            if x_dis > 0:
                if y_dis > 0: offset =  9;
                else        : offset = -7;
            else        :
                if y_dis > 0: offset =  7;
                else        : offset = -9;
                
        if not offset: 
            print("? err");
            return False;

        for i in range(Pos + offset, Mov_Pos, offset):
            if self.position[i]:
                if abs(offset) == 1: 
                    print(i,"--- err");
                    return False;
                if abs(offset) == 8: 
                    print(i,"| err");
                    return False; 
                print(i,"X err");
                return False;

        return True;


    def _IsCheck(self, Pos, Team = 2):  # 2 = none
        CheckingPiece = [];

        if Pos < 0 or Pos > 63:
            print("Pos err");
            return CheckingPiece;

        if Team == 2 and self.position[Pos]: Team = self.position[Pos]//8;

        x_Pos = Pos% 8;
        y_pos = Pos//8;

        for x_sign in [-1, 0, 1]:
            for y_sign in [-1, 0, 1]:
                if not x_sign and not y_sign: continue;

                for i in (1, 2):
                    if not x_sign or not y_sign: break;

                    X = x_Pos + x_sign*(3-i);
                    Y = y_pos + y_sign*i;

                    if X < 0 or X > 7 or Y < 0 or Y > 7 : continue;
                    pos = Y*8 + X;

                    if self.position[pos]% 8 == 3 and self.position[pos]//8 != Team: CheckingPiece.append(pos);

                for i in range(1,8):
                    X = x_Pos + x_sign*i;
                    Y = y_pos + y_sign*i;

                    if X < 0 or X > 7 or Y < 0 or Y > 7 : continue;
                    pos = Y*8 + X;

                    if not self.position[pos]   : continue;

                    opp_team = self.position[pos]//8;
                    if opp_team == Team         : break;

                    opp_kind = self.position[pos]% 8;
                    Checked  = False;

                    if opp_kind == 1:
                        if   Team != 2 and Team*2 - y_sign == 1 and i == 1 and x_sign: Checked = True;
                        elif Team == 2 and opp_team*2 + y_sign == 1:
                            if not x_sign:
                                if   i == 1: Checked = True;
                                elif i == 2 and 6 - opp_team*5 == Y: Checked = True;
                                else : break;
                            elif i == 1 and x_sign and 2 + opp_team*3 == Y and self.special_Mov_flag[opp_team] == X: Checked = True;
                            else : break;
                        else : break;

                    if opp_kind == 2:
                        if not x_sign*y_sign: Checked = True;
                        else                : break;

                    if opp_kind == 4:
                        if x_sign*y_sign: Checked = True;
                        else            : break;

                    if opp_kind == 5: Checked = True;

                    if opp_kind == 6:
                        if i == 1: Checked = True;
                        else     : break;

                    if Checked:
                        CheckingPiece.append(pos);
                        break;
        
        for i in range(len(CheckingPiece)): print(CheckingPiece[i]);

        return CheckingPiece;

    
    def _IsCheckMate(self, Pos):
        CheckingPieces = self._IsCheck(Pos);
        Team = self.position[Pos]//8;

        x_Pos = Pos% 8;
        y_pos = Pos//8;

        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                if x_offset or y_offset: pass;
                else                   : continue;

                X = x_Pos + x_offset;
                Y = y_pos + y_offset;

                if X < 0 or X > 7 or Y < 0 or Y > 7 : continue;
                pos = Y*8 + X;

                if self.position[pos]//8 == Team: continue;
                if self._IsCheck(pos, Team)     : continue;

                return False;

        if len(CheckingPieces) == 1:

            opp_Pos = CheckingPieces[0];
            opp_CheckingPieces = self._IsCheck(opp_Pos, abs(1-Team));

            if opp_CheckingPieces:
                if len(opp_CheckingPieces) == 1 and self.position[opp_CheckingPieces[0]]%8 == 6: return True;
                return False;

            basic_offsets = {-1, 1,-8, 8,-9,-7, 7, 9};
            offset        = 0;

            if Pos//8 == opp_Pos//8:
                if opp_Pos > Pos: offset =  1;
                else            : offset = -1;
            else:
                for i in range(2,8):
                    if (opp_Pos - Pos)%basic_offsets[i] == 0: offset = basic_offsets[i];

            if offset == 0: return True;

            for i in range(Pos + offset, opp_Pos, offset):
                if self._IsCheck(i, abs(1-Team)): return False;

        return True;


    def _MovCheck(self, Pos, mov_Pos):
        if Pos < 0 or Pos > 63: return False;
        if mov_Pos < 0 or mov_Pos > 63: return False;

        print(Pos    % 8, Pos    //8);
        print(mov_Pos% 8, mov_Pos//8);

        piece     = self.position[Pos];
        opp_piece = self.position[mov_Pos];

        if not piece                             : print("there is no piece");
        if piece//8 != (self.round)%2            : print("Round err");
        if opp_piece and piece//8 == opp_piece//8: print("Team err");

        Kind = piece% 8;
        Team = piece//8;

        x_itval = mov_Pos% 8 - Pos% 8;
        y_itval = mov_Pos//8 - Pos//8;

        if Kind == 3:
            if not ((abs(abs(x_itval) - abs(y_itval))) == 1 and abs(abs(x_itval) + abs(y_itval)) == 3):
                print("N err");
                return False;
            return True;

        if not self._RouteCheck(Pos, mov_Pos):
            print("Block err");
            return False

        if Kind == 1:
            if abs(x_itval) + abs(y_itval - Team*2 + 1) > 1:
                print("P err");
                return False;
            if y_itval == 2 and Pos//8 != (6 - Team*5):
                print("P2 err");
                return False;
            if x_itval == y_itval and not opp_piece:
                if Pos//8 == 3 + Team and Pos% 8 == self.special_Mov_flag[Team]%8: return True;
                print("P3 err");
                return False;
        
        elif Kind == 6:
            if not(abs(x_itval) < 2 and abs(y_itval) < 2):
                print("K err");
                return False;

        elif Kind == 2:
            if x_itval*y_itval:
                print("R err");
                return False;

        elif Kind == 4:
            if abs(x_itval) != abs(y_itval):
                print("B err");
                return False;

        elif Kind == 5:
            if x_itval*y_itval and abs(x_itval) != abs(y_itval):
                print("Q err");
                return False;
        
        return True;

    
    def _IsEnd(self):
        Turn = self.round%2;
        count = 0;

        for i in range(64):
            if self.position[i]% 8 == 6:
                count += 1;
                if self._IsCheck(i):
                    if Turn: print("Black", end="");
                    else   : print("White", end="");

                    if self._IsCheckMate(i):
                        print(" is CheckMate!");
                        return True;
                    else: print(" is Check!");

                elif self._IsCheck(i):
                    print("End game err");
                    return True;

        if count != 2:
            print("End game err");
            return True;
        
        return False;

# ======== main ======== #

chess = Chess();

chess._PrintChess();

dict_PieceKind = {"P" : 1, "R" : 2, "N" : 3, "B" : 4, "Q" : 5, "K" : 6};

while(chess._IsEnd() == False):
    Round = chess.round;

    print("\nRound :", Round+1, "\n");
    chess._PrintChess;

    INPUT     = input();
    err_input = False;
    pos       = [-1, 0];
    kind      = 0;
    castling  = 0;

    if len(INPUT) == 3:
        if 'PRNBQKprnbqk'.count(INPUT[0]):
            kind = dict_PieceKind.get(INPUT[0].upper(), 0);
            INPUT = INPUT[1:];
        else: err_input = True;

    if len(INPUT) == 2:
        if 'ABCDEFGHabcdefgh12345678'.count(INPUT[0]) and '12345678'.count(INPUT[1]):
            X_pos = 0;
            Y_pos = 8-int(INPUT[1]);

            if '12345678'.count(INPUT[0]): X_pos = int(INPUT[0])-1;
            else                         : X_pos = int(ord(INPUT[0].upper()) - ord('A'));

            pos[1] = X_pos + Y_pos*8;

            if kind: possible_pieces = list(filter(lambda x: chess.position[x]//8 == Round%2 and chess.position[x]% 8 == kind, chess._IsCheck(pos[1])));
            else   : possible_pieces = list(filter(lambda x: chess.position[x]//8 == Round%2, chess._IsCheck(pos[1])));
            
            if possible_pieces:
                if len(possible_pieces) > 1: print("둘수 있는 말이 2개 이상입니다.");
                else:
                    possible_pos = possible_pieces[0];
                    print(possible_pos% 8, possible_pos//8);
                    pos[0] = possible_pos;
            else: print("둘수 있는 말이 없습니다.");

            if pos[0] == -1: err_input = True;

        elif INPUT.isalpha() and kind == 0:
            if INPUT[1].upper() == 'C' and chess.special_Mov_flag[Round%2]&8:
                if 'RK'.count(INPUT[1].upper()): castling = 2;
                if 'LQ'.count(INPUT[1].upper()): castling = 1;

                if castling:
                    if castling == 1: sign = -1;
                    else            : sign =  1;

                    for i in range(3):
                        if i and chess.position[4+1*sign + 56*((Round+1)%2)]:
                            castling = 0;
                            break;
                        if chess._IsCheck(4+1*sign + 56*((Round+1)%2), Round%2):
                            castling = 0;
                            break;

                else: err_input = True;
            else: err_input = True;
        
        elif len(INPUT) == 4 and INPUT.isdigit() and not INPUT.count('9'):
            pos[0] = (int(INPUT[0]) - 1) + (8 - int(INPUT[1]))*8
            pos[1] = (int(INPUT[2]) - 1) + (8 - int(INPUT[3]))*8

        else: err_input = True;

        if err_input:
            print("input err");
            continue;

        if castling:
            if castling == 2: sign = 1;
            else            : sign =-1;

            chess._Moving(4             , 7*(Round%2), 4 + 2*sign, 7*(Round%2));
            chess._Moving(7*(castling-1), 7*(Round%2), 4 + 1*sign, 7*(Round%2));
            chess.special_Mov_flag[Round%2] = 0;
            chess._CountUp();

        elif chess._MovCheck(pos[0], pos[1]):

            if chess.special_Mov_flag[Round%2]:
                if pos[0] ==     56*((Round+1)%2) or pos[1] ==     56*((Round+1)%2):
                    chess.special_Mov_flag[Round%2] &= 23;
                if pos[0] == 7 + 56*((Round+1)%2) or pos[1] == 7 + 56*((Round+1)%2):
                    chess.special_Mov_flag[Round%2] &= 15;
                if pos[0] == 4 + 56*((Round+1)%2):
                    chess.special_Mov_flag[Round%2] &= 7;
            
            chess._Moving(pos[0], pos[1]);

            for i in range(64):
                if chess.position[i] == 6 + (Round%2)*8 and chess._IsCheck(i): err_input = True;

            if err_input:
                chess._Moving(pos[1], pos[0]);
                print("체크로 불가한 이동입니다.");
                continue;

            chess._CountUp;
            print('(', pos[0]%8 + 1, 8 - pos[0]//8, ') --> (', pos[1]%8 + 1, 8 - pos[1]//8, ')');

        else:
            print("Fatal err");
            continue;

        if chess.position[pos[0]]%8 == 1 and abs(pos[1] - pos[0]) == 16: chess.special_Mov_flag[(Round+1)%2] |= (pos[0]%8);
        else: 
            chess.special_Mov_flag[(Round+1)%2] &= 24;
            chess.special_Mov_flag[ Round   %2] &= 24;

    chess._PrintChess();
    chess._CountUp();

if chess.round%2 == 0: print("흰팀 승리");
else                 : print("검팀 승리");