import os
import sys
import time
import ctypes as ct

if sys.version_info >= (3,0):
    import urllib.parse

cur_dir = os.path.abspath(os.path.dirname(__file__))
ximc_dir = os.path.join(cur_dir, "ximc")
ximc_package_dir = os.path.join(ximc_dir, "crossplatform", "wrappers", "python")
sys.path.append(ximc_package_dir)

if sys.platform in ("win32", "win64"):
    libdir = os.path.join(ximc_dir, sys.platform)
    os.environ["Path"] = libdir + ";" + os.environ["Path"]

try: 
    from pyximc import *
    from pyximc import MicrostepMode
except ImportError as err:
    print ('Can not import pyximc module.')
    exit()
except OSError as err:
    print ('Can not load libximc library.')
    exit()

def loop_set_pos_calb(device_id):
	wnd1 = 10
	calb = calibration_t()
	calb.A = ct.c_double(0.04)
	calb.MicrostepMode = 1
	dif = 0
	while 1:
		print("First window number: ")
		wnd1 = int(input()) - 1
		print("Second window number: ")
		wnd2 = int(input()) - 1

		if dif != 0:
			print("Setting initial state...")
			spin = 8
			lib.command_move_calb(att_id, ct.c_float(spin), byref(calb))
			lib.command_wait_for_stop(att_id, 10)
			# if dif < 0:
			# 	print("SECOND SPIN++++++++++++++++++++++++")
			# 	lib.command_move_calb(att_id, ct.c_float(spin), byref(calb))
			# 	lib.command_wait_for_stop(att_id, 10)
			lib.command_zero(att_id)
			lib.command_wait_for_stop(att_id, 10)
			print(" Done\n")
		dif = wnd2 - wnd1

		print("Setting position...")
		lib.command_move_calb(att_id, ct.c_float(wnd2), byref(calb))
		lib.command_wait_for_stop(att_id, 10)
		if wnd1 > wnd2:
			wnd1 = wnd1 - 8
		lib.command_move_calb(att_id, ct.c_float(wnd1), byref(calb))
		print(" Done\n")


if __name__ == "__main__":
   
	att_id = lib.open_device(b'xi-com:\\\\.\\COM63')
	print("ID: ", att_id)
	print("Calibration...")
	lib.command_homezero(att_id)
	lib.command_wait_for_stop(att_id, 10)
	print(" Done\n")
	loop_set_pos_calb(att_id)