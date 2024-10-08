{
    "name": "OpenSPP User Roles",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Beta",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_registry_group",
        "g2p_programs",
        "spp_area",
        "spp_idqueue",
        "base_user_role",
        "spp_api",
    ],
    "data": ["data/local_roles.xml", "data/global_roles.xml", "data/ir_cron.xml", "views/role.xml", "views/user.xml"],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "summary": "Enhances user role management with local roles and area-based access control for improved data security and granularity in OpenSPP.",
}
