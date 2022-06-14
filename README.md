Setting up your Python Environment with VSCode and Anacoda

A. Install VSCode, Python and Anacoda
   1. Install VSCode: https://code.visualstudio.com/docs/setup/windows
   2. Install Python: 3.9.x: https://www.python.org/downloads/
   3. Install Anaconda: 4.13.x: https://anaconda.cloud/installers

B. Configure Anacoda Environments
    - Do not use "base" for your development environment,
    - Create a new environment and download packages you'll need for the project.

C. Configure VSCode to work with Anacoda: Resolving PS the following error: 
        PS C:\Users\gong_yi_tan_pi\File> conda activate base
        conda : The term 'conda' is not recognized as the name of a cmdlet, function, 
        script file, or operable program. Check the spelling of the name, or if a     
        path was included, verify that the path is correct and try again.
        At line:1 char:1
        Ref: https://stackoverflow.com/questions/54828713/working-with-anaconda-in-visual-studio-code
    1. Search for "Windows PowerShell" and run as Administrator,
    2. Set the execution policy to remote signed: set-ExecutionPolicy RemoteSigned
    3. Choose [A]Yes to All
    4. Add the Anaconda path to your PC's systems path: C:\ProgramData\Anaconda3. 
        - Maybe different on your system. To find out, launch the "Anaconda Prompt", type "path" 
          at the prompt
    5. Open an Anaconda Prompt and run "conda init powershell" which will add Conda related startup 
       to a Powershell profile.ps1 somewhere in your user's profile.
    6. Enter the same path as in step 4. above to VSCode's File->preferences->Settings->Python->"Conda Path"

