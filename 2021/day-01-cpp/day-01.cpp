#include <iostream>
#include <vector>
#include <string>
#include <fstream>


using namespace std;

int main()
{
    vector<int> input;
	ifstream inputStream;
	inputStream.open("input.txt");
	string line;
	while(getline(inputStream, line)) {
		input.push_back(stoi(line));
	}
	int increase = 0;
	int last = input[0];

	for(int i = 0; i < input.size(); i++){
		if(input[i] > last) {
			increase++;
		}
		last = input[i];
	}
	cout << increase << endl;
}