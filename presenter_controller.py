#!/usr/bin/env python
import argparse, os, sys, time
import pebble as libpebble

# -- based off the smarthomewatch example by makrco https://github.com/makrco/smarthomewatch
FORWARD = chr(29)
BACK = chr(28)

def music_control_handler(endpoint, resp):
    print "Button pressed", resp
    key = BACK
    if resp == 'NEXT':
        key = FORWARD

    cmd = """osascript -e 'tell application "System Events" to keystroke "%s"'""" % (key,)
    os.system(cmd)

def cmd_remote(pebble):
    pebble.register_endpoint("MUSIC_CONTROL", music_control_handler)
    print 'Waiting for control events...'
    try:
        while True:
            if pebble._ser.is_alive():
                time.sleep(2)
            else:
                print "Lost connection"
                break
    except KeyboardInterrupt:
        pass


def main():
    parser = argparse.ArgumentParser(description='a utility belt for pebble development')
    parser.add_argument('--pebble_id', type=str, help='the last 4 digits of the target Pebble\'s MAC address. \nNOTE: if \
                        --lightblue is set, providing a full MAC address (ex: "A0:1B:C0:D3:DC:93") won\'t require the pebble \
                        to be discoverable and will be faster')

    parser.add_argument('--lightblue', action="store_true", help='use LightBlue bluetooth API')
    parser.add_argument('--pair', action="store_true", help='pair to the pebble from LightBlue bluetooth API before connecting.')
    args = parser.parse_args()
    while True:
        try:
            pebble_id = args.pebble_id
            if pebble_id is None and "PEBBLE_ID" in os.environ:
                pebble_id = os.environ["PEBBLE_ID"]
            pebble = libpebble.Pebble(pebble_id, args.lightblue, args.pair)

            try:
                cmd_remote(pebble)
            except Exception as e:
                print 'error', e
                pebble.disconnect()
                raise e
                return

            pebble.disconnect()
            time.sleep(5)
        except:
            print 'error (2)'
            time.sleep(2)

if __name__ == '__main__':
    main()

