<?xml version="1.0" encoding="UTF-8" ?>
<Package name="8-007-dialog-launch-dance-animation" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="Dance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Demo" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Dialog4Animation" src="Dialog4Animation/Dialog4Animation.dlg" />
    </Dialogs>
    <Resources>
        <File name="epicsax" src="Dance/epicsax.ogg" />
    </Resources>
    <Topics>
        <Topic name="Dialog4Animation_enu" src="Dialog4Animation/Dialog4Animation_enu.top" topicName="Dialog4Animation" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
