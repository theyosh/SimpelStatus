# NOTICE:
#
# Application name defined in TARGET has a corresponding QML filename.
# If name defined in TARGET is changed, the following needs to be done
# to match new name:
#   - corresponding QML filename must be changed
#   - desktop icon filename must be changed
#   - desktop filename must be changed
#   - icon definition filename in desktop file must be changed
#   - translation filenames have to be changed

# The name of your application
TARGET = SimpelStatus

CONFIG += sailfishapp

SOURCES += src/SimpelStatus.cpp

OTHER_FILES += qml/SimpelStatus.qml \
    qml/cover/CoverPage.qml \
    rpm/SimpelStatus.spec \
    rpm/SimpelStatus.yaml \
    translations/*.ts \
    SimpelStatus.desktop

SAILFISHAPP_ICONS = 86x86 108x108 128x128 256x256

# to disable building translations every time, comment out the
# following CONFIG line
CONFIG += sailfishapp_i18n

# German translation is enabled as an example. If you aren't
# planning to localize your app, remember to comment out the
# following TRANSLATIONS line. And also do not forget to
# modify the localized app name in the the .desktop file.
TRANSLATIONS += translations/SimpelStatus-de.ts

DISTFILES += \
    qml/pages/About.qml \
    qml/pages/Home.qml \
    qml/pages/Account.qml \
    qml/pages/Settings.qml \
    qml/pages/History.qml \
    qml/pages/Options.qml \
    qml/python/SimpelScraper.py \
    qml/python/MockData.py \
    qml/python/Encryption.py \
    qml/images/mijn_simpel.png \
    rpm/SimpelStatus.changes \
    translations/SimpelStatus-nl.ts \
    qml/pages/Contract.qml \
    qml/images/SimpelStatus.png \
    qml/pages/EditOptions.qml \
    qml/pages/FieldListElement.qml

