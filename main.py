import argparse
import serial

def main():
    # parse command line arguments
    parser = argparse.ArgumentParser(description="Read from Arduino serial communication and log it to standard output and optionally a file.")
    parser.add_argument("--file", type=str, default=None, required=False, help="Optional output file for logging.")
    parser.add_argument("--baud", type=int, default=9600, required=False, help="Baud rate for communication with the Arduino.")
    parser.add_argument("--port", type=str, default=None, required=True, help="Port for communication with the Arduino.")
    args = parser.parse_args()

    # open the file for writing
    fd = None
    if not args.file is None:
        fd = open(args.file, "w")
    
    # open the serial port
    ser = serial.Serial(args.port, args.baud)

    # endless loop for logging
    while True:
        # read from the serial port
        line = ser.readline().decode("ascii").rstrip("\n\r")

        # write to standard output
        print(line)

        # write to the file if available
        if not fd is None:
            fd.write(line + "\n")
            fd.flush()


if __name__ == "__main__":
    main()
