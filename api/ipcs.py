# avax-python : Python tools for the exploration of the Avalanche AVAX network.
# Author: https://github.com/ojrdevcom/
# License MIT

import avaxpython
import jsrpc

caller = avaxpython.get_caller()

def publishBlockchain(blockchainID):

    data = {
        "blockchainID": blockchainID
    }

    return caller("ipcs.publishBlockchain", data)


def unpublishBlockchain(blockchainID):

    data = {
        "blockchainID": blockchainID
    }

    return caller("ipcs.unpublishBlockchain", data)
