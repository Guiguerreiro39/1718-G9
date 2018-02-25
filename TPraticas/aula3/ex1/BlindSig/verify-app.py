# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# verifySignature-app.py
#
# Cripto-7.4.1 - Commmad line app to exemplify the usage of verifySignature
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that receives signer's public key from file and Data, Signature, Blind Components and
prComponents from STDIN and writes a message to STDOUT indicating if the signature is valid..
"""

import sys, os
from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils

def printUsage():
    print("Usage: python verify-app.py -cert <certificado do assinante> -msg <mensagem original a assinar> -sDash<Signature> -f <ficheiro do requerente>")

def parseArgs():
    if (len(sys.argv) == 9 and sys.argv[1] == "-cert" and sys.argv[3] == "-msg"):
        # Para a linha de cima não ficar demasiado grande
        if(sys.argv[5] == "-sDash" and sys.argv[7] == "-f"):
            eccPublicKeyPath = sys.argv[2]
            with open(sys.argv[4], "r") as msg:
                data = msg.read()
            with open(sys.argv[6], "r") as sig:
                signature = sig.read()
            for filename in os.listdir(sys.argv[8]):
                if (filename == "pRComponents"):
                    with open(sys.argv[8] + "/" + filename, "r") as pRc:
                        pRComponents = pRc.read()
                elif (filename == "blindComponents"):
                    with open(sys.argv[8] + "/" + filename, "r") as blindC:
                        blindComponents = blindC.read()
            main(eccPublicKeyPath, data, signature, blindComponents, pRComponents)
    else:
        printUsage()

def showResults(errorCode, validSignature):
    print("Output")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPublicKeyPath, data, signature, blindComponents, pRComponents):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

if __name__ == "__main__":
    parseArgs()
