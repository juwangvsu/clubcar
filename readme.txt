------10/5/21 adafruit ds1841 test --------------------
Documents/clubcar/readme.txt                                                                                            test i2c and board connection:
        i2cdetec -y 1
        it should show an address 0x28-0x2a valid

install python package:
pip3 install adafruit-circuitpython-ds1841
ingnore the CircuitePython stuff since we are using full python package.

test examples:
circuitpython boundle zip file contain examples to test.
         python3 ds1841_blinka_simpletest.py
        ds1841 = adafruit_ds1841.DS1841(i2c, address=0x2a)
        use address 0x2a since our board showup on address 0x2a.

to use different address, connect a0 a1 pin accordingly to vcc or gnd?

issue: put a1 to gnd crash the pi computer.

