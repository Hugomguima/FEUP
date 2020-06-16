#pragma once
#include <vector>
#include "Position.h"

class Ship {
public:
	Ship(unsigned int identifier, char symbol,
		Position position, char direction,
		size_t size);
	unsigned int id() const; //returns identifier
	Position pos() const; //returns position   
	char dir() const;  //returns direction  
	size_t size() const; //returns size
	// ... OTHER METHODS
private:
	unsigned int identifier; // ship id number
	// ... OTHER ATTRIBUTES AND/OR METHODS
};
