cmake_minimum_required(VERSION 3.16)
project(buildproj C)
set(CMAKE_C_STANDARD 11)
add_executable(app
  src/main.c
  src/parser.c
  src/config.c
  src/cache.c
  src/log.c
  src/tables.c)
target_include_directories(app PRIVATE src)
