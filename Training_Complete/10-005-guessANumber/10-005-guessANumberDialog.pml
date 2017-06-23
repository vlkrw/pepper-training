<?xml version="1.0" encoding="UTF-8" ?>
<Package name="10-005-guessANumberDialog" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="1- guess" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="0 - random" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="2- bounds with parameters" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="1- guess/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="randomGame" src="0 - random/randomGame/randomGame.dlg" />
        <Dialog name="GuessANumber" src="2- bounds with parameters/GuessANumber/GuessANumber.dlg" />
    </Dialogs>
    <Resources />
    <Topics>
        <Topic name="ExampleDialog_enu" src="1- guess/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="ExampleDialog_frf" src="1- guess/ExampleDialog/ExampleDialog_frf.top" topicName="ExampleDialog" language="fr_FR" />
        <Topic name="randomGame_enu" src="0 - random/randomGame/randomGame_enu.top" topicName="randomGame" language="en_US" />
        <Topic name="GuessANumber_enu" src="2- bounds with parameters/GuessANumber/GuessANumber_enu.top" topicName="GuessANumber" language="en_US" />
        <Topic name="GuessANumber_frf" src="2- bounds with parameters/GuessANumber/GuessANumber_frf.top" topicName="GuessANumber" language="fr_FR" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_fr_FR" src="translations/translation_fr_FR.ts" language="fr_FR" />
    </Translations>
</Package>
