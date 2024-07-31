SPUIS is a 1D model for calculating flows in discharge sluices. See the [documentation](https://spuis.readthedocs.io/) for more details and theory.

### *Required Python packages* <br/>
To install the required packages, run the following command in the command window:
<pre>
pip install -r ./docs/requirements.txt
</pre>

### *Running a simulation* <br/>
Run 'runSpuis.py' (./SPUIS) to execute a simulation and postprocess the results. The input files have the extension ".in". Some example input files can be found in the folder "Tests". The output files (.uqh and .uws) and generated figures will be saved to the folder in which the corresponding input file was saved. 

### *Generating a new executable* <br/>
A new executable needs to be generated whenever developments are made to the code (./SPUIS/SPUIS401/). The script EXE.py can be used for this, which requires the pyInstaller package:

<pre>
pip3 install pyInstaller
</pre>

It is important to specify the changes made and supply a new version number in EXE.py. An independent executable will be made in the folder 'dist' upon running EXE.py. The executable will be copied alongside SPUIS401.py.