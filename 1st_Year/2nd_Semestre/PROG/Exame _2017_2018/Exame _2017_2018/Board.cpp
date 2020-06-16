#include "Board.h"

Board::Board(size_t numLines, size_t numColumns)
{
	for (size_t i = 0; i < numLines; i++)
		for (size_t j = 0; j < numColumns; j++)
			board[i][j] = -1;
}

bool Board::putShip(const Ship & s)
{
	if (canPutShip(s.pos(),s.dir(),s.size()) == false) return false;

	switch (s.dir())
	{
	case 'H':

		for (size_t i = s.pos().col; i < s.pos().col + s.size(); i++)
		{
			board[s.pos().lin][i] = s.id();
		}

		break;

	case 'V':

		for (size_t i = s.pos().lin; i < s.pos().lin + s.size(); i++)
		{
			board[i][s.pos().col] = s.id();
		}
		
		break;
	}
	return true;
}

bool Board::canPutShip(Position pos, char dir, size_t size)
{
	switch (dir)
	{
	case 'H':

		if (pos.lin < numLines && pos.col + size < numColumns)
		{
			for (size_t i = pos.col; i < pos.col + size; i++)
			{
				if (board[pos.lin][i] != -1) return false;
			}
		}
		else return false;
		break;

	case 'V':

		if (pos.lin + size < numLines && pos.col < numColumns)
		{
			for (size_t i = pos.lin; i < pos.lin + size; i++)
			{
				if (board[i][pos.col] != -1) return false;
			}
		}
		else return false;
		break;
	}

	return true;
}
