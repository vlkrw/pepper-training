<?xml version="1.0" encoding="UTF-8" ?>
<Package name="6-002-calculs-dialog" format_version="4">
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
        <Topic name="AskForOperation_frf" src="AskForOperation/AskForOperation_frf.top" topicName="AskForOperation" language="fr_FR" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
