#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <deque>
#include <unordered_map>

using namespace std;

vector<string> tokenize(string const &str, const char delim) {
    size_t start;
    size_t end = 0;
	vector<string> out;
    while ((start = str.find_first_not_of(delim, end)) != string::npos) {
        end = str.find(delim, start);
        out.push_back(str.substr(start, end - start));
    }
	return out;
}

void add_element(unordered_map<string, vector<string> >& paths, string left, string right){
	if (paths.find(left) == paths.end()) {
		vector<string> *v = new vector<string>;
		auto pr = pair<string, vector<string> >(left, *v);
		paths.insert(pr);
	} 
	auto path_vec_iter = paths.find(left);
	(*path_vec_iter).second.push_back(right);
}
 
bool should_visit(deque<string> visited, string ele) {
	if(isupper(ele.c_str()[0])){ // can always visit big caves
		return true;
	}
	for(auto iter = visited.begin(); iter != visited.end(); iter++ ) {
		if(*iter == ele){ // do not visit small visited caves
			return false;
		}
	}
	return true;
}	
int main() {
	ifstream input_stream;
	string filename = "input.txt";
	input_stream.open(filename);
	string line;
    unordered_map<string, vector<string> > paths;
	
	// read map
	while(getline(input_stream, line)) {
		auto tokens = tokenize(line, '-');
		add_element(paths, tokens[0], tokens[1]);
		add_element(paths, tokens[1], tokens[0]);
	}

	// traverse path
	deque<pair<string, deque<string> > > working;
	deque<string> v;
	int num_paths = 0;

	working.push_front(make_pair("start", v));
	while(!working.empty()) {
		auto working_ele = working.front();
		auto ele = working_ele.first;
		auto visited = working_ele.second;
		working.pop_front();

		if(ele == "end"){
			for(auto iter = visited.begin(); iter != visited.end(); iter++ ) {
				cout << *iter << " ";
			}
			num_paths++;
			cout << endl;
			continue;
		}

		auto possible_paths_iter = paths.find(ele);
		auto possible_paths_vec = (*possible_paths_iter).second;

		visited.push_back(ele);

		for(int i = 0; i < possible_paths_vec.size(); i++){
			string s = possible_paths_vec[i];
			if(should_visit(visited, s)){
				auto visit_copy = visited;
				working.push_back(make_pair(s, visit_copy));
			}
		}
	}
	cout << "total paths " << num_paths << endl;

	return 0;
}

