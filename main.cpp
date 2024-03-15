#include <iostream>
#include <cmath>
using namespace std;
const int field_size = 45;
const int fi = floor(field_size/2);
bool field[field_size*field_size] {};

void add_dot(int x, int y)
{
    
    field[x+((y+fi)*field_size)+fi]=1;
    
}
void add_function()
{
    int y;
    for(int x {-fi}; x <= fi; x++) {y = sin(x)*3; add_dot(x,y);}
}

void draw_field()
{
    int y = -1;
    for(int i {0}; i < field_size*field_size; i++)
    {
        if (i % field_size == 0)
        { 
            cout << "\n";
            y++;
        }
        
        if (field[i] == 0) 
        {
            if (y == fi and i - (y*field_size) == fi) {cout << "+ "; }
                else if (y == fi) {cout << "- "; }
                else if (i - (y*field_size ) == fi) { cout << "| "; }
                else
        {
            cout << ". ";
        }
           
        
        }
        if (field[i] == 1)
        {
            cout << "0 ";
        }
    
    }
    
    
}


int main()
{
    add_dot(0,0);
    add_function();
    draw_field();
    
    return 0;
}
