import logging
import miio

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    mdns = miio.Discovery().discover_mdns(timeout=2000)
    print(mdns)
