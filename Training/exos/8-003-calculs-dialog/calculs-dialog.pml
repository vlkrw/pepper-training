<?xml version="1.0" encoding="UTF-8" ?>
<Package name="calculs-dialog" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="AskForOperation" src="AskForOperation/AskForOperation.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="AskForOperation_enu" src="AskForOperation/AskForOperation_enu.top" topicName="AskForOperation" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
        <Path src="translations/translation_en_US.ts" />
        <Path src="translations" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
