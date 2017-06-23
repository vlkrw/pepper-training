<?xml version="1.0" encoding="UTF-8" ?>
<Package name="8-002-example-dialogs" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Demo" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="DemoBehavior" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Topic" src="My Examples Topic/Topic.dlg" />
        <Dialog name="test" src="Conditions and caracters in input/test.dlg" />
        <Dialog name="StayInScope" src="StayInScope/StayInScope.dlg" />
        <Dialog name="InteractionNotSpeakNotUnderstood" src="InteractionNotSpeakNotUnderstood/InteractionNotSpeakNotUnderstood.dlg" />
        <Dialog name="DemoTopic" src="DemoTopic/DemoTopic.dlg" />
        <Dialog name="MyNewTopic" src="MyNewTopic/MyNewTopic.dlg" />
        <Dialog name="PARIS170321" src="PARIS170321/PARIS170321.dlg" />
        <Dialog name="simple" src="simple/simple.dlg" />
    </Dialogs>
    <Resources>
        <File name="epicsax" src="behavior_1/epicsax.ogg" />
    </Resources>
    <Topics>
        <Topic name="Topic_enu" src="My Examples Topic/Topic_enu.top" topicName="Topic" language="en_US" />
        <Topic name="test_enu" src="Conditions and caracters in input/test_enu.top" topicName="test" language="en_US" />
        <Topic name="StayInScope_enu" src="StayInScope/StayInScope_enu.top" topicName="StayInScope" language="en_US" />
        <Topic name="Topic_frf" src="My Examples Topic/Topic_frf.top" topicName="Topic" language="fr_FR" />
        <Topic name="InteractionNotSpeakNotUnderstood_enu" src="InteractionNotSpeakNotUnderstood/InteractionNotSpeakNotUnderstood_enu.top" topicName="InteractionNotSpeakNotUnderstood" language="en_US" />
        <Topic name="DemoTopic_enu" src="DemoTopic/DemoTopic_enu.top" topicName="DemoTopic" language="en_US" />
        <Topic name="MyNewTopic_enu" src="MyNewTopic/MyNewTopic_enu.top" topicName="MyNewTopic" language="en_US" />
        <Topic name="PARIS170321_enu" src="PARIS170321/PARIS170321_enu.top" topicName="PARIS170321" language="en_US" />
        <Topic name="simple_enu" src="simple/simple_enu.top" topicName="simple" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src="translations" />
        <Path src="translations/translation_en_US.ts" />
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_fr_FR" src="translations/translation_fr_FR.ts" language="fr_FR" />
    </Translations>
</Package>
