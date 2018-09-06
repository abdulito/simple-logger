import os
import time
import logging
import sys
import traceback

########################################################################################################################
# Main
########################################################################################################################


def main(args):
    frequency_in_seconds = 1
    if os.environ.get("LOG_FREQUENCY_SECONDS"):
        frequency_in_seconds = int(os.environ.get("LOG_FREQUENCY_SECONDS"))

    #
    # setup logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(levelname)8s | %(asctime)s | %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    count = 0
    while True:
        count += 1
        logger.info("Log message %s"% count)
        time.sleep(frequency_in_seconds)

########################################################################################################################
# Bootstrap
########################################################################################################################


if __name__ == '__main__':
    try:

        main(sys.argv[1:])
    except (SystemExit, KeyboardInterrupt) , e:
        if hasattr(e, 'code') and e.code == 0:
            pass
        else:
            raise
    except:
        traceback.print_exc()
        raise