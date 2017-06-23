<?xml version="1.0" encoding="UTF-8" ?>
<Package name="8-006-dialog-pcall-scall" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="topic" src="topic/topic.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="topic_enu" src="topic/topic_enu.top" topicName="topic" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
