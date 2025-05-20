#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

struct Student {
    int id;
    std::string name, roll_no, grade;
};

std::vector<Student> readCSV(const std::string& filename) {
    std::vector<Student> students;
    std::ifstream file(filename);
    std::string line;

    std::getline(file, line); // Skip header
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        Student s;
        std::string temp;
        std::getline(ss, temp, ','); s.id = std::stoi(temp);
        std::getline(ss, s.name, ',');
        std::getline(ss, s.roll_no, ',');
        std::getline(ss, s.grade, ',');
        students.push_back(s);
    }
    file.close();
    return students;
}

void generateReport(const std::vector<Student>& students) {
    std::ofstream file("report.csv");
    file << "name,grade\n";
    for (const auto& s : students) {
        file << s.name << "," << s.grade << "\n";
    }
    file.close();
}

int main() {
    auto students = readCSV("students.csv");
    generateReport(students);
    std::cout << "Report generated: report.csv\n";
    return 0;
}