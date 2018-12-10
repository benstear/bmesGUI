Final Code folder contains all the final, individual functions for the entire project which includes 
ECGplot.py, fnirplot.py, mainwindow.py, test.py, utilities.py, videowidget.py
- ECGplot.py reads the ECG data, and displays it on the GUI
- Fnirsplot.py reads the fnirs data, and displays It on the GUI
- Mainwindow.py creates the structure of the GUI, the buttons, and can save the data into the Code logfile. It also holds and displays the fNIRS and ECG data.
- Test.py puts the entire program together, playing the video simultaneously with the gui.
- Utilities.py creates the database, and shows the database.
- Videowidget.py plays the video which is stored remotely. 

Working Code folder contains all the individual functions that were being changed for the entire project which includes 
ECGplot.py, fnirplot.py, mainwindow.py, test.py, utilities.py, videowidget.py
- ECGplot.py reads the ECG data, and displays it on the GUI
- Fnirsplot.py reads the fnirs data, and displays It on the GUI
- Mainwindow.py creates the structure of the GUI, the buttons, and can save the data into the Code logfile. It also holds and displays the fNIRS and ECG data.
- Test.py puts the entire program together, playing the video simultaneously with the gui.
- Utilities.py creates the database, and shows the database.
- Videowidget.py plays the video which is stored remotely.

PWC44 folder contains movisens data which includes acc.csv, ecg.csv PWC44_Oxy.txt
- acc.csv contains the accerlerometry data (64Hz) (3 planes)
- ecg.csv contains the heart rate data (1024Hz)
- PWC44_Oxy.txt contains the fNIRS data oxygenated Hb at 7.81Hz (each column is each 
channel)

Code logfile contains the information produced by the overall gui/inputs

Design.pptx contains the flowchart/ project design showing the user interaction.
Design.xlsx contains the listed functions, purposes, main authors, inputs, outputs, etc.
Example Data.xlsx has the biometric information, the sync start times, The current timings of 
each circuit/movisens, and current errors.
GUI Sketch.pptx contains the original sketch of the GUI, before it was converted to Sketch.jpg
Presentation.pptx contains the presentation for class
Report.docx contains the written report of the project
Sketch.jpg contains the original sketch 
Thumb.png contains the thumbnail
index.yml contains the abstract of the gui/project


Python Packages necessary to run the GUI:

-numpy
-pandas
-PyQt5
-PyQtGui
-PyQtGraph
-cv2
-os
-sys


Our program has been tested on MacOS (Mojave) running on a 2.7 GHz Intel Core i5 processor.



  
