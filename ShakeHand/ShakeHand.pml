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
        <Topic name="HandShakeLogic_enu" src="ShakeHands/HandShakeLogic_enu.top" topicName="HandShakeLogic" language="en_US" />
        <Topic name="HandShakeLogic_ged" src="ShakeHands/HandShakeLogic_ged.top" topicName="HandShakeLogic" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_de_DE" src="translations/translation_de_DE.ts" language="de_DE" />
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
