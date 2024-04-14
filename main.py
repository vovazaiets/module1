from fastapi import FastAPI
from fastapi.responses import JSONResponse , HTMLResponse
from Board import board
from Database.database import Base,engine


app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/board_list", response_class=JSONResponse)
async def get_board():
    json_board = []
    for position, piece in board.board.items():
        if piece:
            json_piece = {
                "symbol": piece.symbol,
                "color": piece.color,
                "position": position
            }
            json_board.append(json_piece)
    return json_board


@app.get("/board", response_class=HTMLResponse)
async def get_board_view():
    board_state = board.print_board()
    html_board = "<table border='5' style='border-collapse: collapse;'>"
    for row in board_state:
        html_board += "<tr>"
        html_board += "".join(f"<td style='width: 30px; height: 30px; text-align: center;'>{cell}</td>" for cell in row)
        html_board += "</tr>"
    html_board += "</table>"
    return html_board



@app.put("/move/{from_pos}/{to_pos}")
async def move_piece(from_pos: str, to_pos: str):
    board.move_piece(from_pos, to_pos)
    return {"message": "Piece moved successfully"}


@app.get("/piece/{position}")
async def get_piece(position: str):
    piece = board.board.get(position)
    if piece:
        print(piece)
        return piece
    else:
        return {"error": "No piece at specified position"}
