# Demonstrate how to customize logging output

import logging

extData = {
    'username' : "hatyham@example.com",
    'userage'  : 23
}

# TODO: add another function to log from
def anotherFunction():
    logging.debug("This is a debug-level message", extra=extData)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "User: %(username)s with Age: %(userage)d operating at %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    datstr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datstr )

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    main()
