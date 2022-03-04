#ifndef UTIL_H
#define UTIL_H

#include <vector>
#include <string>
using namespace std;

class util {
	public:
		static vector<string> tokenize(const string  &str, const char delim);
		static vector<string> read_lines(const string &filename);
		static void trim_in_place(std::string &s);
};

#endif