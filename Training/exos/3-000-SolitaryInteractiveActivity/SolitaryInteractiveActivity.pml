<?xml version="1.0" encoding="UTF-8" ?>
<Package name="3-SolitaryInteractiveActivity" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="Interactive" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Solitary" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="NoNature" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Solitary2" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="applauncher" src="applauncher/applauncher.dlg" />
    </Dialogs>
    <Resources>
        <File name="elephant" src="Interactive/elephant.ogg" />
    </Resources>
    <Topics>
        <Topic name="applauncher_enu" src="applauncher/applauncher_enu.top" topicName="applauncher" language="en_US" />
        <Topic name="applauncher_frf" src="applauncher/applauncher_frf.top" topicName="applauncher" language="fr_FR" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_fr_FR" src="translations/translation_fr_FR.ts" language="fr_FR" />
    </Translations>
</Package>
