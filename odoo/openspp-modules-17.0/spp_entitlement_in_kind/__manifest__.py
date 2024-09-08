# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP In-Kind Entitlement",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_programs",
        "spp_programs",
        "product",
        "stock",
        "spp_service_points",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/entitlement_manager_view.xml",
        "wizard/create_program_wizard.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "summary": "Manages the distribution of in-kind entitlements within social protection programs, handling inventory, service points, and beneficiary redemption.",
}
