#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from Device import Device


class Console(Device):


    def createDevice(self):
        from journal.devices.Console import Console
        return Console()


    def __init__(self):
        Device.__init__(self, "console")
        return


# version
__id__ = "$Id: Console.py,v 1.1.1.1 2006-11-27 00:09:35 aivazis Exp $"

# End of file 
