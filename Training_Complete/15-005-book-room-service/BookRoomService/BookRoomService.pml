<?xml version="1.0" encoding="UTF-8" ?>
<Package name="BookRoomService" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ReservationGroup" src="ReservationGroup/ReservationGroup.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
    </Resources>
    <Topics>
        <Topic name="ReservationGroup_enu" src="ReservationGroup/ReservationGroup_enu.top" topicName="ReservationGroup" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_fr_FR" src="translations/translation_fr_FR.ts" language="fr_FR" />
    </Translations>
</Package>
