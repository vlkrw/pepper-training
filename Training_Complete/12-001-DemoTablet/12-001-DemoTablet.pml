<?xml version="1.0" encoding="UTF-8" ?>
<Package name="12-001-DemoTablet" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="stl" src="html/stl.css" />
        <File name="index-video" src="html/index-video.html" />
        <File name="videoutils" src="html/videoutils.js" />
        <File name="gr" src="html/media/gr.png" />
        <File name="video" src="html/media/video.mp4" />
        <File name="robot-pepper" src="html/media/robot-pepper.png" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
