cmake_minimum_required(VERSION 3.9)
project(tiny-dnn LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#set(CMAKE_CXX_COMPILER /usr/bin/clang++)

set(CMAKE_CXX_FLAGS "-pthread --std=c++14")
#set(CMAKE_CXX_FLAGS_M2S "-pthread -DNDEBUG -m32 -static -march=pentium-m -O2 -D DEBUG")

include_directories(${PROJECT_SOURCE_DIR}/src)
include_directories(./)

add_executable(tinyMnist src/mnist.cpp)
add_executable(tinyCifar src/cifar.cpp)

