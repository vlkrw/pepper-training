<?xml version="1.0" encoding="UTF-8" ?>
<Package name="10-004-request_example" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="__init__" src="httplib2/__init__.py" />
        <File name="cacerts" src="httplib2/cacerts.txt" />
        <File name="iri2uri" src="httplib2/iri2uri.py" />
        <File name="socks" src="httplib2/socks.py" />
        <File name="__init__" src="httplib2/test/__init__.py" />
        <File name="socket" src="httplib2/test/brokensocket/socket.py" />
        <File name="test_proxies" src="httplib2/test/functional/test_proxies.py" />
        <File name="miniserver" src="httplib2/test/miniserver.py" />
        <File name="other_cacerts" src="httplib2/test/other_cacerts.txt" />
        <File name="smoke_test" src="httplib2/test/smoke_test.py" />
        <File name="test_no_socket" src="httplib2/test/test_no_socket.py" />
        <File name="" src=".metadata" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src="translations" />
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
