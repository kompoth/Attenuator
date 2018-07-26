## Read me

In this project several simple examples of using LibXIMC protocol with 8SMC5-USB controller were implemented. A rotating optical attenuator was used as a controlled device. Code samples were written on Python 3.4 and also in LabVIEW programming environment. Both LabVIEW and Python realizations include a simple linear and more complexed cyclical algorithms. Keep in mind that all examples imply presetting device using XILab and ".cfg" file, which is added to this project as well as all necessary LibXIMC files.

Python files can be launched with cmd from "Python_example" directory. Both simple.py and loop.py take as an argument a COM-port of the device: e.g. 'python loop.py COM63'

LabVIEW project does not include files of XILab -- you need to add them first. However it is much easier just to copy files of the example (simple.vi, ex_loop.vi and att.lvproj) to the directory "examples" from XIMC Software package -- most likely you have already [downloaded it](https://doc.xisupport.com/en/8smc5-usb/8SMCn-USB/Files/Software.html), since you are using LibXIMC.

You also need to enter a COM-port number of your attenuator device in VI's block diagram -- predetermined might be incorrect. You can easily modify simple.vi and ex_loop.vi diagrams, using examples from Software package, so that device selection would be more adequate.


