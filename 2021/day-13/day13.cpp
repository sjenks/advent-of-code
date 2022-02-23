#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <set>
#include "util.h"

using namespace std;

pair<int, int> fold_point(pair<int, int>& point, pair<string, int>& fold);
vector<pair<int, int>> dedupe(vector<pair<int, int>>& in);

int main(void) {
	string filename( "input.txt");
	auto point_strs = util::read_lines(filename);

	string fold_name = "input-fold.txt";
	auto fold_strs = util::read_lines(fold_name);

	vector<pair<int, int> > points;
	for(auto pair : point_strs) {
		auto point = util::tokenize(pair, ',');
		auto x = stoi(point.at(0));
		auto y = stoi(point.at(1));
		auto point_pair = std::pair<int, int>(x,y);
		points.push_back(point_pair);
	}

	vector<pair<string, int> > folds;
	for(auto fold_str : fold_strs) {
		auto f = util::tokenize(fold_str, '=');
		auto axis = f.at(0);
		auto mag = stoi(f.at(1));
		auto fold_pair = std::pair<string, int>(axis, mag);
		
		folds.push_back(fold_pair);
	}

	for(auto fold : folds) {
		vector<pair<int, int> > next_points;
		auto first_fold = folds.at(0);
		for(auto point : points) {
			auto folded_point = fold_point(point, fold);

			next_points.push_back(folded_point);
		}
		points = dedupe(next_points);
	}

	///// print
	char plot[100][100];
	for(int x = 0; x < 100; x++) {
		for(int y = 0; y < 100; y++) {
			plot[y][x] = ' ';
		}
	}
	for(auto point : points) {
		//cout << point.first << " " << point.second << endl;
		plot[point.second][point.first] = 'X';
	}

	for(int x = 70; x >= 0; x--) {
		for(int y = 20; y >= 0; y--) {
			cout << plot[y][x];
		}
		cout << endl;
	}

	return 0;
}

vector<pair<int, int>> dedupe(vector<pair<int, int>>& in) {
	set<pair<int, int> > point_set;
	for(auto point : in){
		point_set.insert(point);
	}
	vector<pair<int, int>> res;
	for(auto point : point_set) {
		res.push_back(point);
	}
	return res;
}

pair<int, int> fold_point(pair<int, int>& point, pair<string, int>& fold) {
	pair<int, int> new_point;
	if(fold.first == "x") {
		// fold position - x point
		int distance = point.first - fold.second;
		if(distance <= 0){ // do nothing for left side
			new_point = std::pair<int, int>(point.first, point.second);
		} else {
			int new_x = fold.second - distance;
			new_point = std::pair<int, int>(new_x,  point.second);
		}
	} else {
		int distance = point.second - fold.second;
		if(distance <= 0){ // do nothing for left side
			new_point = std::pair<int, int>(point.first, point.second);
		} else {
			int new_y = fold.second - distance;
			new_point = std::pair<int, int>(point.first,  new_y);
		}
	}
	return new_point;
}
