#include <vector>
#include <string>
#include <fstream>
#include "util.h"
using namespace std;

vector<string> util::tokenize(const string &str, const char delim)
{
	size_t start;
	size_t end = 0;
	vector<string> out;
	while ((start = str.find_first_not_of(delim, end)) != string::npos)
	{
		end = str.find(delim, start);
		out.push_back(str.substr(start, end - start));
	}
	return out;
}

vector<string> util::read_lines(const string filename) {
	ifstream input_stream;
	input_stream.open(filename);
	string line;
	
	vector<string> output;
	while(getline(input_stream, line)) {
		output.push_back(line);
	}
	return output;
}