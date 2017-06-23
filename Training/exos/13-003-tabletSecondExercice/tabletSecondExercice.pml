<?xml version="1.0" encoding="UTF-8" ?>
<Package name="tabletSecondExercice" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="tabletDialog" src="tabletDialog/tabletDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="jquery.min" src="html/jquery.min.js" />
    </Resources>
    <Topics>
        <Topic name="tabletDialog_enu" src="tabletDialog/tabletDialog_enu.top" topicName="tabletDialog" language="en_US" />
        <Topic name="tabletDialog_frf" src="tabletDialog/tabletDialog_frf.top" topicName="tabletDialog" language="fr_FR" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
