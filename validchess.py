def valid_chess_board(chessboard: dict)-> bool:
    """Checks the validity of a chessboard dictionary"""
    valid_template_chessboard= {
        '1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',
        '2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
        '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
        '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
        '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
        '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
        '7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
        '8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': '',
    }

    chess_pieces=['rook', 'king', 'queen', 'pawn', 'knight', 'bishop']

    for k,v in chessboard.items():
        if not valid_template_chessboard.get(k):
            return False
        if not v.startswith('w') or v.startswith('b'):
            return False

        for piece in chess_pieces:
            is_present=v.rfind(piece) 
            if is_present ==1 or is_present ==-1:
                continue
            else:
                return False
        
    return True
    
    
    
