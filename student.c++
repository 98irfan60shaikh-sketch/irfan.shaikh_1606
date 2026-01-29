#include<iostream>
#include<string>
#include<vector>
using namespace std;
class Student{
private:
 int rollno;
 string name;
 int age;
 string course;
 public:
Student(int r,string n,int a,string c){
 rollno=r;
 name=n;
 age=a;
 course=c;
}
void display(){
 cout<<"--------------"<<endl;
 cout<<"Roll no :-"<<rollno<<endl;
 cout<<"Name :-"<<name<<endl;
 cout<<"Age :-"<<age<<endl;
 cout<<"Course :-"<<course<<endl;
 cout<<"-------------"<<endl;
}
};
int main(){
int n;
cout<<"enter a number of student :-";
cin>>n;
vector<Student>students;
for(int i=0;i<n;i++){
int rollno;
string name;
int age;
string course;

cout<<"\nEnter details for student :-"<<i+1<<endl;
cout<<"Rollno :-"<<endl;
cin>>rollno;
cout<<"Name :-"<<endl;
cin>>name;
cout<<"age :-"<<endl;
cin>>age;
cout<<"Course :-"<<endl;
cin>>course;

students.push_back(Student(rollno,name,age,course));
}
cout<<"\n---student information---\n";
for(int i=0;i<n;i++){
students[i].display();
}
return 0;
}
