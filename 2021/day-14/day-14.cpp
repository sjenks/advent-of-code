#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <set>
#include <unordered_map>
#include "util.h"

using namespace std;

string replace_all(string& in, vector<pair<string, string>>& rules);
string matches_rule(string& couplet, vector<pair<string, string>>& rules);
unordered_map<char, int> letter_freq(string& str);

int main(void) {
	//string filename( "small.txt");
	string filename( "input.txt");
	string polymer("CKFFSCFSCBCKBPBCSPKP");
	//string polymer("NNCB");

	auto lines = util::read_lines(filename);
	vector<pair<string, string>> rules;
	for(auto line : lines) {
		auto tokens = util::tokenize(line, ',');
		rules.push_back(pair<string, string>(tokens[0], tokens[1]));
	}

	int num_steps = 10;
	for(int i = 0; i < num_steps; i++){
		polymer = replace_all(polymer, rules);
		//cout << polymer << endl;
	}
	auto freq = letter_freq(polymer);
	int most_common = INT32_MIN;
	int least_common = INT32_MAX;
	for(auto ele : freq) {
		cout << (int)ele.first << " " << ele.second << endl;
		if(ele.second > most_common) {
			most_common = ele.second;
		}
		if(ele.second < least_common) {
			least_common = ele.second;
		}
	}
	cout << "diff is " << most_common - least_common << endl;
	return 0;
}

string replace_all(string& in, vector<pair<string, string>>& rules) {
	string next;

	for(int i = 0; i < in.length() - 1; i++){
		string couplet = string(1, in[i]);
		couplet += in[i+1];

		string rule_match = matches_rule(couplet, rules);
		string suffix = in[i] + rule_match;
		next.append(string(suffix));
	}
	char last = in[in.length()-1];
	string lastAppend({last, '\0'});
	next.append(lastAppend);

	return next;
}

string matches_rule(string& couplet, vector<pair<string, string>>& rules){
	for(auto rule : rules) {
		if(couplet.compare(rule.first) == 0) {
			return rule.second;
		}
	}
	return "";
}

unordered_map<char, int> letter_freq(string& str) {
	unordered_map<char, int> freq;
	for(int i = 0; i < str.length(); i++) {
		char c = str[i];
		if((int)c == 0) {
			continue;
		}
		if(freq.find(c) == freq.end()) {
			freq[c] = 1;
		} else {
			freq[c] = freq[c] + 1;
		}
	}
	return freq;
}