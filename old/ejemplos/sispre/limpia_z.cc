#include <iostream.h>
void main(void)
  {
    while(cin.ipfx(1))
      {
        int c= cin.get();
        if(c==26)
          {
            cin.get(); cin.get();
            continue;
          }
        cout << char(c);
      }
  }
