<?xml version="1.0" encoding="UTF-8" ?>
<Package name="ShakeHand" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="test" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ShakeHands" src="ShakeHands/ShakeHands.dlg" />
    </Dialogs>
    <Resources>
        <File name="HandShakeService" src="HandShakeService.py" />
    </Resources>
    <Topics>
        <Topic name="ShakeHands_enu" src="ShakeHands/ShakeHands_enu.top" topicName="ShakeHands" language="en_US" />
        <Topic name="ShakeHands_ged" src="ShakeHands/ShakeHands_ged.top" topicName="ShakeHands" language="de_DE" />
        <Topic name="logic" src="ShakeHands/logic.top" topicName="" language="" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_de_DE" src="translations/translation_de_DE.ts" language="de_DE" />
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
