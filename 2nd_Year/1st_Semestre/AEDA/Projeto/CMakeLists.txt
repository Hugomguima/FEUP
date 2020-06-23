cmake_minimum_required(VERSION 3.15)
project(Projeto)

set(CMAKE_CXX_STANDARD 14)

include_directories(feup-aeda-project)

add_executable(Projeto
        feup-aeda-project/main.cpp
        feup-aeda-project/menus.cpp
        feup-aeda-project/menus.h
        feup-aeda-project/person.cpp
        feup-aeda-project/person.h
        feup-aeda-project/player.cpp
        feup-aeda-project/player.h
        feup-aeda-project/staff.cpp
        feup-aeda-project/staff.h feup-aeda-project/Game.h feup-aeda-project/Game.cpp)
