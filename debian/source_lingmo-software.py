import apport.packaging

def add_info(report, ui):
    report["InstalledPlugins"] = apport.hookutils.package_versions(
        'lingmo-software-plugin-flatpak',
        'lingmo-software-plugin-snap')
