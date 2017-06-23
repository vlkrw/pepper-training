<?xml version="1.0" encoding="UTF-8" ?>
<Package name="ChestColor" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="DetectObject" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="main" src="main.py" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src=".vscode" />
        <Path src=".vscode/settings.json" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
