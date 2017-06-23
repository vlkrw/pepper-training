<?xml version="1.0" encoding="UTF-8" ?>
<Package name="8-002-example-dialogs" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Topic" src="My Examples Topic/Topic.dlg" />
        <Dialog name="test" src="Conditions and caracters in input/test.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="Topic_enu" src="My Examples Topic/Topic_enu.top" topicName="Topic" language="en_US" />
        <Topic name="test_enu" src="Conditions and caracters in input/test_enu.top" topicName="test" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
