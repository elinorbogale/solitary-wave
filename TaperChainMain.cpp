//ORIGINAL CREDITS GRANTED TO: Adam Sokolow - 1/31/14
//The newest TaperChain code 08/2025
//Parse input from specified file (drag and drop ok)
//Tthen setup simulation
//Then run sim.

#include <iostream>
#include <fstream>
#include "Simulation.h"


using namespace std;


bool readFile(const string &filename,ofstream &out,Simulation &sim);

int main(int argc, char* argv[])
{
    string loadFromFile = "parameters.txt";
    Simulation mySim; //Simulation Parameters and Variables
    ofstream out_file;
    //Checks to see if the user entered a file name
    //defaults to using parameters.txt
    if(argc > 1)
    {
        loadFromFile = argv[1];
        out_file.open(("READ_"+loadFromFile).c_str());

        if(!readFile(loadFromFile,out_file,mySim)&&!mySim.shouldWeHault())
        {
                mySim.executeCommands();
                if(!mySim.shouldWeHault())
                {
               if(!mySim.isSilent())
                    cout<<mySim<<endl;//not silent, so it echoes to the command line

                out_file<<mySim<<endl;
                out_file.close();

                    mySim.runSimulation();
                }//execute if
        }
        else
        {
            out_file.close();
            cout<<"There were errors found! Check readme file for help and/or the command line."<<endl;
        }

    }
    else
        mySim.printHelp();

    return 0;
}

bool readFile(const string &filename,ofstream &out,Simulation &sim)
{
    out<<"**********************************************************"<<endl;
    out<<"\t\tThe Taper Chain Program  "<<endl<<endl;
    out<<"\t\tVersion 1-31-14 "<<endl<<endl;
    out<<"\t\tVersion 3-08-14 : corrected file read issues for cygwin"<<endl<<endl;
    out<<"**********************************************************"<<endl;
    out<<"\tWelcome to the Readme File"<<endl;
    out<<"\tI will first spray everything I read in."<<endl;
    out<<"\tThen I will decode this and tell you what I found."<<endl;
    out<<"\tThen I will begin the simulations and keep some output here."<<endl;
    out<<"**********************************************************"<<endl;
    out<<"Getting all my setup from file : "<<filename<<endl<<endl;

    string line;int count =1;
    pair<bool,string> result;
    bool parseError = false;

    ifstream in_file;

    in_file.open(filename.c_str());
    do{
        in_file>>line;
        }while(!in_file.fail()&&!in_file.eof());
    in_file.close();
    if(sim.toLowerCase(sim.removeWhiteSpace(line))!="end" && sim.toLowerCase(sim.removeWhiteSpace(line))!="end:")
    {
         cout<<sim.toLowerCase(sim.removeWhiteSpace(line))<<endl;
            out<<"*******************PARSE ERROR START************************"<<endl;
            out<<"end the parameter input file with the word \"end\" "<<endl;
            out<<"*******************PARSE ERROR END  ************************"<<endl;
            cout<<"*******************PARSE ERROR START************************"<<endl;
            cout<<"end the parameter input file with the word \"end\" "<<endl;
            cout<<"*******************PARSE ERROR END  ************************"<<endl;

            return true;
    }

    in_file.open(filename.c_str());
    getline(in_file,line);
    while(!in_file.eof() && !in_file.fail())
       {
           if(!sim.isSilent())
           cout<<"Read line "<<count<<": "<<line<<endl;
           out<<"Read line "<<count<<": "<<line<<endl;
            result = sim.parseString(line);
            if(!result.first)
            {
                parseError =true;
                out<<"*******************PARSE ERROR START************************"<<endl;
                out<<result.second<<endl;
                out<<"*******************PARSE ERROR END  ************************"<<endl<<endl;
            if(!sim.isSilent())
            {
                cout<<"*******************PARSE ERROR START************************"<<endl;
                cout<<result.second<<endl;
                cout<<"*******************PARSE ERROR END  ************************"<<endl<<endl;
            }
            }
            getline(in_file,line);count++;
       }

        in_file>>line;
        if(!sim.isSilent())
           cout<<"Read line "<<count<<": "<<line<<endl;
           out<<"Read line "<<count<<": "<<line<<endl;

    in_file.close();
    return parseError;
}

