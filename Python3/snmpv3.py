from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
     cmdgen.UsmUserData('usr-sha-aes128', 'authkey1', 'privkey1',
                       authProtocol=cmdgen.usmHMACSHAAuthProtocol,
                       privProtocol=cmdgen.usmAesCfb128Protocol),
    cmdgen.UdpTransportTarget(('demo.snmplabs.com', 161)),
    '1.3.6.1.2.1.1.6.0'
)

# Check for errors and print out results
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
